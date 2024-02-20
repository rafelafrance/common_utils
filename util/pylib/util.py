from typing import Any

import ftfy
import regex as re


def shorten(text: str) -> str:
    """Collapse all whitespace in a string."""
    return " ".join(text.split())


def compress(text: str) -> str:
    """Collapse whitespace in a string but keep lines."""
    text = [" ".join(ln.split()) for ln in text.splitlines()]
    return "\n".join(ln for ln in text if ln)


def to_positive_float(value: Any) -> float | None:
    """Convert a string to a float stripping bad characters from the string first."""
    if isinstance(value, str):
        value = re.sub(r"[^\d./]", "", value) if value else ""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def to_positive_int(value: Any) -> int | None:
    """Convert a string to an int stripping bad characters from the string first."""
    if isinstance(value, str):
        value = re.sub(r"[^\d./]", "", value) if value else ""
        value = re.sub(r"\.$", "", value)
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def clean_text(
    text: str,
    trans: dict[int, str] | None = None,
    replace: dict[str, str] | None = None,
    *,
    eol_hyphens: bool = False,
) -> str:
    """Clean text before trait extraction."""
    text = text if text else ""

    # Handle uncommon mojibake
    if trans:
        text = text.translate(trans)

    if replace:
        for old, new in replace.items():
            text = text.replace(old, new)

    text = compress(text)  # Space normalize

    # Join hyphenated words when they are at the end of a line
    if eol_hyphens:
        text = re.sub(r"([a-z])-\s+([a-z])", r"\1\2", text, flags=re.IGNORECASE)

    text = ftfy.fix_text(text)  # Handle common mojibake

    text = re.sub(r"\p{Cc}+", " ", text)  # Remove control characters

    text = re.sub(r"\xc2\xad", "", text)  # Remove soft-hyphens

    return text

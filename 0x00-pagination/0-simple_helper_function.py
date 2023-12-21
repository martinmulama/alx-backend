#!/usr/bin/env python3
"""Function to generate index."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """Cal the first and last index an list

    Args:
        page (int): number of pag
        page_size (int): item per pag

    Returns:
        Tuple[int]: Tuple first and last index
    """
    first_index = 0
    last_index = page * page_size
    if page > 1:
        first_index = (page - 1) * page_size
    return (first_index, last_index)

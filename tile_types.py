from typing import Tuple

import numpy as np

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_td = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool_),  # True if this tile is walkable
        ("transparent", np.bool_),  # True if this tile doesn't block FOV
        ("dark", graphic_td),  # Graphics for when tile is not in FOV
        ("light", graphic_td),  # Graphics for ehwn the tile  is in FOV
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """helper function for defining individual tile types"""
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


SHROUD = np.array(
    (ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_td
)  # represents unexplored, unseen tiles


floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
    light=(ord(" "), (255, 255, 255), (200, 180, 50)),
)

wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
    light=(ord(" "), (255, 255, 255), (130, 110, 50)),
)

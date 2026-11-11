"""Bubble sort implementation.

Bubble sort repeatedly steps through the list, compares adjacent items and
swaps them if they are in the wrong order.  It is simple but has O(n^2) worst
case and average case time complexity, so it is best suited for small lists or
teaching purposes.
"""


def bubble_sort(values):
    """Return a new list with ``values`` sorted in ascending order.

    The input sequence is not modified.  The sort is stable, so items that
    compare equal keep their original relative order.

    Args:
        values: Any iterable of mutually comparable items.

    Returns:
        A new list containing the items of ``values`` in ascending order.
    """
    items = list(values)
    length = len(items)

    for end in range(length - 1, 0, -1):
        swapped = False
        for index in range(end):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swapped = True
        if not swapped:
            # The list is already sorted, so stop early.
            break

    return items


if __name__ == "__main__":
    sample = [5, 2, 9, 1, 5, 6]
    print(bubble_sort(sample))

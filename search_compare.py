import random
import time


SEARCH_TARGET = 99999999
LIST_SIZES = (500, 1000, 5000)
TRIALS = 100


def get_me_random_list(n):
    a_list = list(range(1, n + 1))
    random.shuffle(a_list)
    return a_list


def sequential_search(a_list, item):
    start = time.perf_counter()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found, time.perf_counter() - start


def ordered_sequential_search(a_list, item):
    start = time.perf_counter()
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found, time.perf_counter() - start


def binary_search_iterative(a_list, item):
    start = time.perf_counter()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found, time.perf_counter() - start


def binary_search_recursive(a_list, item):
    start = time.perf_counter()
    found = _binary_search_recursive(a_list, item)
    return found, time.perf_counter() - start


def _binary_search_recursive(a_list, item):
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            return True
        else:
            if item < a_list[midpoint]:
                return _binary_search_recursive(a_list[:midpoint], item)
            else:
                return _binary_search_recursive(a_list[midpoint + 1:], item)


def main():
    searches = (
        ('Sequential Search', sequential_search),
        ('Ordered Sequential Search', ordered_sequential_search),
        ('Binary Search Iterative', binary_search_iterative),
        ('Binary Search Recursive', binary_search_recursive),
    )

    for size in LIST_SIZES:
        totals = {name: 0.0 for name, _ in searches}

        for _ in range(TRIALS):
            a_list = get_me_random_list(size)

            _, time_taken = sequential_search(a_list, SEARCH_TARGET)
            totals['Sequential Search'] += time_taken

            a_list.sort()

            for name, search in searches[1:]:
                _, time_taken = search(a_list, SEARCH_TARGET)
                totals[name] += time_taken

        print(f'List size: {size}')
        for name, _ in searches:
            time_taken = totals[name] / TRIALS
            print(f'{name} took {time_taken:10.7f} seconds to run, on average')
        print()


if __name__ == '__main__':
    main()

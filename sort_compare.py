import random
import time


LIST_SIZES = (500, 1000, 5000)
TRIALS = 100


def get_me_random_list(n):
    a_list = list(range(1, n + 1))
    random.shuffle(a_list)
    return a_list


def insertion_sort(a_list):
    start = time.perf_counter()

    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    return a_list, time.perf_counter() - start


def shell_sort(a_list):
    start = time.perf_counter()
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

    return a_list, time.perf_counter() - start


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    start = time.perf_counter()
    a_list.sort()
    return a_list, time.perf_counter() - start


def main():
    sorts = (
        ('Insertion Sort', insertion_sort),
        ('Shell Sort', shell_sort),
        ('Python Sort', python_sort),
    )

    for size in LIST_SIZES:
        totals = {name: 0.0 for name, _ in sorts}

        for _ in range(TRIALS):
            a_list = get_me_random_list(size)

            for name, sort in sorts:
                _, time_taken = sort(a_list[:])
                totals[name] += time_taken

        print(f'List size: {size}')
        for name, _ in sorts:
            time_taken = totals[name] / TRIALS
            print(f'{name} took {time_taken:10.7f} seconds to run, on average')
        print()


if __name__ == '__main__':
    main()

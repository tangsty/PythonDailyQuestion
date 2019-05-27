# coding=utf-8


__author__ = 'jianqiang.liu'


def calc_fraction_sum(cnt: int) -> float:
    numerator, denominator = 2, 1
    result = 0.0
    for i in range(cnt):
        result += numerator / denominator
        denominator, numerator = numerator, numerator + denominator
    return result


def get_n() -> int:
    try:
        while True:
            str_n = input('Please input the number of fraction sequence: ')
            try:
                int_n = int(float(str_n))
                if int_n >= 1:
                    return int_n
            except ValueError:
                print('\n    INVALID number, input again!\n')
                continue

            print('  number should be greater than 1 !')
            continue
    except KeyboardInterrupt:
        return -1


if __name__ == "__main__":
    n = get_n()
    if n >= 1:
        total = calc_fraction_sum(n)
        print('Summary of First {} Fractional Sequences is {:.4f}'
              .format(n, total))
    else:
        print('\nNo need to calculate the summary of fractional sequence')

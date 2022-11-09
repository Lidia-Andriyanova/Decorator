import datetime
import time


def cacher(func):
    cach = []

    def wrapper(*args):
        start = time.perf_counter_ns()

        n = args[0]
        if n not in cach:
            res = func(n)
            max_cach_elem = len(cach) - 1
            for i in range(max_cach_elem + 1, n + 1):
                cach.append(res[i])
        else:
            res = cach[:n+1]

        finish = time.perf_counter_ns()
        return finish - start, res

    return wrapper


def logger(func):

    def wrapper(*args):

        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        res = func(*args)
        time_ns = res[0]
        lst = res[1]
        log_msg += f"Возвращаемый список из {len(lst)} элементов получен за {time_ns} нс\t"
        log_msg += f'результат: {lst}\n'
        with open('log_file.log', 'a', encoding='utf-8') as fp:
            fp.write(log_msg)
        return res

    return wrapper


@logger
@cacher
def seq(n):
    lst = []
    for i in range(0, n + 1):
        lst.append((1 + i) ** i)
    return lst


def main():
    print(seq(20))
    print(seq(15))
    print(seq(10))
    print(seq(12))
    print(seq(30))
    print(seq(10))


if __name__ == '__main__':
    main()

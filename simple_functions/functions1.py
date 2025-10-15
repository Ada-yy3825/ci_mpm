from functools import cache

__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot

# @cache：这是 Python 3.9+ 中 functools 模块提供的装饰器，用于缓存函数的返回值，避免重复计算，提高效率。
# 递归计算阶乘时，使用缓存可以显著减少计算时间，尤其是对于较大的输入值。
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

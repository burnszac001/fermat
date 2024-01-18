from random import randint
from math import floor


# This is main function that is connected to the Test button. You don't need to touch it.
def prime_test(N, k):
    return fermat(N, k), miller_rabin(N, k)


# You will need to implement this function and change the return value.
def mod_exp(x, y, N):
    if y == 0:
        return 1
    z = mod_exp(x, floor(y / 2), N)
    if y % 2 == 0:
        return pow(z, 2, N)
    return (x * pow(z, 2)) % N

print(mod_exp(3, 24, 97))


# You will need to implement this function and change the return value.   
def fprobability(k: int):
    return 1 - pow(2, -k)


# You will need to implement this function and change the return value.   
def mprobability(k):
    return 1 - pow(0.25, k)


# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likely want to use
# random.randint(low,hi) which gives a random integer between low and
# high, inclusive.
def fermat(N: int, k: int) -> str:
    exp = N - 1
    mod = N

    for i in range(k):
        base = randint(1, N - 1)
        if mod_exp(base, exp, mod) != 1:
            return 'composite'

    return 'prime'


# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likely want to use
# random.randint(low,hi) which gives a random integer between low and
#  high, inclusive.
def miller_rabin(N, k):
    mod = N
    for _ in range(k):
        exp = N - 1
        base = randint(2, N - 1)
        while exp < 2:
            result = mod_exp(base, exp, mod)
            if result == 1:
                exp = floor(exp / 2)
                continue
            elif result == (N - 1):
                break

            return 'composite'

    return 'prime'
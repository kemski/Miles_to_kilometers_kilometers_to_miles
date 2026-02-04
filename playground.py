def sum(*args):
    sum = 0
    for n in args:
        sum +=n
    return sum

print(sum(1,2,3,5, 1, 10, 32, 33))

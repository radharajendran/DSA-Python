def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be integer'
    if n == 0:
        return 0
    else:
        return  int(n % 10) + sumOfDigits(int(n/10))

print(sumOfDigits(12345))
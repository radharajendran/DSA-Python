def decimalToBinary(n):
    assert int(n) == n, 'The number must be integer'
    if n  == 0:
        return  0
    else:
        return  decimalToBinary(int(n/2))  * 10 + n % 2

print(decimalToBinary(10))
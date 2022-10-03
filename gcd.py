def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The number must be integer'

    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if b == 0:
        return a
    else:
        return  gcd(b, a%b)

print(gcd(15, 96))
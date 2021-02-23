from itertools import product


def sum_digits(digit):
    return sum(int(x) for x in digit if x.isdigit())

def a():
    for i in range(0,367):
        for z in range(2,96):
            for x in product('01234567', repeat=7):
                if (i < 100):
                    if(i < 10):
                        w = ''.join(x)
                        w = list(w)
                        w[0] = 0
                        w = [str(x) for x in w]
                        w = ''.join(w)
                        if(sum_digits(w) % 7 == 0):
                            s = "00" + str(i) + str(z) + "-OEM-" + str(w) + "1234567"
                    else:
                        w = ''.join(x)
                        if sum_digits(w) % 7 == 0:
                            s = "0" + str(i) + str(z) + "-OEM-" + str(w) + "1234567"
                else:
                    w = ''.join(x)
                    if sum_digits(w) % 7 == 0:
                        s = str(i) + str(z) + "-OEM-" + str(w) + "1234567"
                print(s)

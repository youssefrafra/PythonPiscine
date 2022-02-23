def binary():
    num = int (input ("Enter your number: "))
    binary = []
    while(num > 0):
        remainder = num % 2
        binary.append(remainder)
        num = num//2
    binary.reverse()
    print(f'binary:{"".join([str(i) for i in binary])}')
# coding=<encoding UTF-8>
# Calculating factorial in two ways


def recursion(number):
    if(number < 0):
        return 0
    if(number <= 1):
        return 1
    return recursion(number-1)*number


def procedural(number):
    result = 1
    if(number < 0):
        return 0
    for i in range(1, number+1):
        result *= i
    return result


# main
number = -1
while number<0:
    number = int(input("Choose an integer: "))
print(recursion(number))
print(procedural(number))

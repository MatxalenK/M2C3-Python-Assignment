def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
        return n


for x in range(1, 47 + 1):
    fizzbuzz(x)

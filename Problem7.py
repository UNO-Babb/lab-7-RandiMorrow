#Problem4=7.py
#Project Euler problem 7


from NumberTests import isPrime
from NumberTests import isEven


def getPrime(n):
    count = 0
    num = 1

    while count < n:
        num += 1
        if isPrime(num):
            count += 1

    return num 

def main():
    num_prime = 10001
    result = getPrime(num_prime)
    print(result)

if __name__ == '__main__':
  main()

"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list=[]
    count = 0
    primenumber = 2;

    while(count<number_of_primes):
        primeCheck = True

        for i in range(2,primenumber):
            if(primenumber % i ==0):
                primeCheck=False

        if primeCheck:
            list.append(primenumber)
            count += count
        primenumber+=primenumber

    return list

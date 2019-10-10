#a function that accepts an exponent p and returns a mersenne number
def mersenne_number(p):
    return (2 ** p) - 1

#testing the function
mersenne_number(5)

#a function to test if a number is a prime number
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

#a function that gets all the prime numbers between a and b        
def get_primes(a, b):
    prime_list = []
    for j in range(a, b):
        if is_prime(j):
            prime_list.append(j)
    return prime_list

#testing the get_primes function ...            
primes = get_primes(3, 65)

#creating a mersenne list ...
mersenne_list = [mersenne_number(prime) for prime in primes]

#printing the mersenne list and its length ...
print(mersenne_list)
print(len(mersenne_list))

#a dummy solution that condenses the tests ...
n_start = 3
n_end = 65
mersennes = []
for number in range(n_start, n_end):
    if is_prime(number):
        mersenne_number = (2 ** number) - 1
        mersennes.append(mersenne_number)
print(mersennes)
print(len(mersennes))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 2
prime_count = 0
primes = []

while prime_count < 3000:
    if is_prime(n):
        primes.append(n)
        prime_count += 1
    n += 1

print(primes)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
primes = numbers.copy()
primes.remove(1)
not_primes = []
for number in numbers:
  for i in range(2, number):
    if number % i == 0:
      not_primes.append(number)
      primes.remove(number)
      break
print('Primes: ',primes)
print('Not_primes: ',not_primes)

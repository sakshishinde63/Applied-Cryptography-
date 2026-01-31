class Solution:

    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def phi(self, n):
        result = n
        p = 2
        temp = n
        while p * p <= temp:
            if temp % p == 0:
                while temp % p == 0:
                    temp //= p
                result -= result // p
            p += 1
        if temp > 1:
            result -= result // temp
        return result

    def twoSum(self, nums, target):

        # ===== Assignment demonstration =====
        a = 7
        b = 11
        mod = 5
        base = 2

        print("Prime check:")
        print(a, ":", self.isPrime(a))
        print(b, ":", self.isPrime(b))

        g = self.gcd(a, b)
        print("GCD:", g)

        if g == 1:
            print("Co-prime: Yes")
            phi_a = self.phi(a)
            phi_b = self.phi(b)
            print("Phi(", a, "):", phi_a)
            print("Phi(", b, "):", phi_b)

            if self.isPrime(a):
                print("Fermat Theorem:", pow(base, a - 1, a))

            print("Euler Theorem:", pow(base, phi_a, a))
        else:
            print("Co-prime: No")

        print("Modular Addition:", (a + b) % mod)
        print("Modular Multiplication:", (a * b) % mod)
        print("Modular Exponentiation:", pow(a, b, mod))

        # ===== Correct Two Sum solution =====
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

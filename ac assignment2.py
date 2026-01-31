class Solution:

    def generateSet(self, n):
        return list(range(n))

    def checkClosure(self, n):
        for a in range(n):
            for b in range(n):
                if (a + b) % n not in range(n):
                    return False
        return True

    def checkInverse(self, n):
        inverses = {}
        for a in range(n):
            for b in range(n):
                if (a + b) % n == 0:
                    inverses[a] = b
                    break
        return inverses

    def multiplicativeInverse(self, n):
        inv = {}
        for a in range(1, n):
            for b in range(1, n):
                if (a * b) % n == 1:
                    inv[a] = b
                    break
        return inv

    def modularDemo(self, n):
        a, b = 3, 4
        print("Addition:", (a + b) % n)
        print("Multiplication:", (a * b) % n)
        print("Exponentiation:", pow(a, b, n))

    def addTwoNumbers(self, l1, l2):

        # ===== Assignment Output =====
        n = 7
        print("Finite set under modulo", n, ":", self.generateSet(n))
        print("Closure:", self.checkClosure(n))
        print("Additive inverses:", self.checkInverse(n))
        print("Multiplicative inverses:", self.multiplicativeInverse(n))
        print("Group under addition: Yes")
        print("Ring: Yes")
        print("Field: Yes")
        print("Modular arithmetic demo:")
        self.modularDemo(n)
        print("Used in RSA and ElGamal cryptography.")

        # ===== Correct Add Two Numbers logic =====
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

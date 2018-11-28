class Palindrome:
    def __init__(self, n):
        if int(n) < n:
            n = int(n) + 1
        self.n = list(str(int(n)))
        if not self.is_palindrome(): self.correct()
    def is_palindrome(self):
        for i in range(len(self.n) / 2):
            if self.n[i] != self.n[-1-i]: return False
        return True
    def correct(self):
        l = len(self.n) / 2
        carry = 0
        for i in range(l):
            if carry == 1:
                if self.n[-1-i] == '9': self.n[-1-i] = '0'
                else: self.n[-1-i] = str(int(self.n[-1-i]) + 1)
            if self.n[i] == self.n[-1-i]: continue
            if self.n[i] < self.n[-1-i]: carry = 1
            self.n[-1-i] = self.n[i]
        if carry == 1: self.n[l-1] = str(int(self.n[l-1]) + 1)
        if not self.is_palindrome(): self.correct()
    def get_next_palindrome(self):
        l = len(self.n)/2
        if len(self.n) % 2 == 1: l += 1
        for i in range(l-1,-1,-1):
            if self.n[i] < '9':
                self.n[i] = str(int(self.n[i]) + 1)
                self.n[-1-i] = self.n[i]
                return Palindrome(int(''.join(self.n)))
            self.n[i] = '0'
            self.n[-1-i] = self.n[i]
        return Palindrome(int('1' + '0' * (len(self.n) - 1) + '1'))
    def squared(self):
        return palindrome(self.num() ** 2)
    def num(self): return int(''.join(self.n))
        
def palindrome(a):
    d = str(a)
    i = 0
    while i < len(d)/2:
        if d[i] != d[-1-i]: return False
        i += 1
    return True

def get_fair_and_square(A,B):
    a = A ** 0.5
    a = Palindrome(a)
    c = 0
    while a.num() <= B ** 0.5:
        if a.squared(): c += 1
        a = a.get_next_palindrome()
    return c

def main():
	T = input()
	for x in range(T):
		A,B = tuple([int(i) for i in raw_input().split()])
		y = get_fair_and_square(A,B)
		print "Case #%d: %d" % (x+1, y)

if __name__ == '__main__': main()

# Python standard library imports made available with the core language.
import collections
import fileinput
import functools
import itertools
import operator

class Quaternion(collections.namedtuple('Quaternion', 'sign value')):
    MULTIPLICATION_TABLE = {('1', '1'): ('+', '1'),
                            ('1', 'i'): ('+', 'i'),
                            ('1', 'j'): ('+', 'j'),
                            ('1', 'k'): ('+', 'k'),
                            ('i', '1'): ('+', 'i'),
                            ('j', '1'): ('+', 'j'),
                            ('k', '1'): ('+', 'k'),
                            ('i', 'i'): ('-', '1'),
                            ('i', 'j'): ('+', 'k'),
                            ('j', 'i'): ('-', 'k'),
                            ('j', 'j'): ('-', '1'),
                            ('j', 'k'): ('+', 'i'),
                            ('k', 'j'): ('-', 'i'),
                            ('k', 'k'): ('-', '1'),
                            ('i', 'k'): ('-', 'j'),
                            ('k', 'i'): ('+', 'j')}

    def __mul__(self, other):
        if not isinstance(other, Quaternion):
            return NotImplemented
        quaternion = self.MULTIPLICATION_TABLE[(self.value, other.value)]
        sign = '+' if self.sign == other.sign else '-'
        sign = '+' if sign == quaternion[0] else '-'
        return Quaternion(sign, quaternion[1])

    def __rmul__(self, other):
        if not isinstance(other, Quaternion):
            return NotImplemented
        quaternion = self.MULTIPLICATION_TABLE[(other.value, self.value)]
        sign = '+' if self.sign == other.sign else '-'
        sign = '+' if sign == quaternion[0] else '-'
        return Quaternion(sign, quaternion[1])

    def __pow__(self, other, z=None):
        if not isinstance(other, int):
            return NotImplemented
        power = Quaternion(self.sign, self.value)
        if z:
            for i in range(0, (other - 1) % z):
                power *= self
        else:
            for i in range(0, other - 1):
                power *= self
        return power

    def __neg__(self):
        if self.sign == '-':
            return Quaternion('+', self.value)
        else:
            return Quaternion('-', self.value)

    def __str__(self):
        return self.sign + self.value
    __repr__ = __str__

quaternion = functools.partial(Quaternion, '+')


if __name__ == '__main__':
    f = fileinput.input()
    cases = int(next(f))

    for i in range(1, cases + 1):
        _, x = map(int, next(f).strip().split())
        quaternions = list(map(quaternion, next(f).strip()))
        # print(x, x * len(quaternions)) # quaternions, 

        # From the cycle graph of the quaternion group, I know that the
        # maximum period of any element of the quaternion group is four. A
        # necessary condition for a quaternion to equal 'ijk' is that it
        # equals -1.
        partial_product = functools.reduce(operator.mul, quaternions)
        product = pow(partial_product, x)
        # print(partial_product, product)
        if product != Quaternion('-', '1') or x * len(quaternions) < 3:
            print('Case #%i: NO' % i)
            continue

        # Since a given sequence always represents some quaternion, if I
        # haven't found +i in the first four repeats, I won't ever find
        # it, and likewise for +k at the end.
        k_start = (x - min(x, 4))*len(quaternions)
        for m, q in enumerate(itertools.accumulate(itertools.chain.from_iterable(itertools.repeat(quaternions, min(x, 4))), operator.mul)):
            # print(m, q)
            if q == Quaternion('+', 'i'):
                i_end = m + 1
                k_product = functools.reduce(operator.mul, itertools.chain.from_iterable(itertools.repeat(quaternions, min(x, 4))))
                for n, r in enumerate(itertools.chain.from_iterable(itertools.repeat(quaternions, min(x, 4)))):
                    # print(i_end, q, k_start + n, k_product)
                    if k_start + n > i_end:
                        if k_product == Quaternion('+', 'k'):
                            if functools.reduce(operator.mul, itertools.islice(itertools.chain.from_iterable(itertools.repeat(quaternions, x)), i_end, k_start + n)) == Quaternion('+', 'j'):
                                print('Case #%i: YES' % i)
                                break
                    k_product = -r * k_product
                else:
                    continue
                break
        else:
            print('Case #%i: NO' % i)

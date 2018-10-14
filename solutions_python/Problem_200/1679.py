class Solver(object):
    def run(self):
        self.T = int(input())
        for i in range(self.T):
            N = int(input())
            ans = self.last_tidy_before(N)
            self.assert_tidy(ans)
            print('Case #%s: %s' % (i+1, ans))

    def last_tidy_before(self, N):
        l = self.int_to_list(N)
        inflection1 = -1
        inflection2 = -1
        for i in range(len(l) - 1):
            if l[i] >= l[i+1] and inflection1 == -1:
                inflection1 = i
            if inflection1 != -1 and l[i] > l[i+1]:
                inflection2 = i
                break
        if inflection2 == -1:
            return N
        if l[inflection1] == 1:
            return self.list_to_int([9] * (len(l) - 1))
        else:
            l[inflection1] = l[inflection1] - 1
            for i in range(inflection1 + 1, len(l)):
                l[i] = 9
        return self.list_to_int(l)

    def int_to_list(self, N):
        return [int(char) for char in str(N)]

    def list_to_int(self, l):
        ret = 0
        for i in range(len(l)):
            ret *= 10
            ret += l[i]
        return ret

    def assert_tidy(self, N):
        l = self.int_to_list(N)
        for i in range(len(l) - 1):
            if l[i] > l[i+1]:
                assert False

Solver().run()

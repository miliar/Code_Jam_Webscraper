

class TidyNumbers:
    @staticmethod
    def solve(s):
        return TidyNumbers.get_tidy_numbers(s)

    @staticmethod
    def is_tidy(s_int):
        s_str = str(s_int)
        if s_str == ''.join(sorted(s_str)):
            return True
        return False

    @staticmethod
    def cut_and_return(s_int):
        s_str = str(s_int)
        s_list = list(s_str)
        s_len = len(s_list)
        for i in range(0, s_len):
            for j in range(i + 1, s_len):
                if s_list[i] > s_list[j]:
                    s_int = int(s_int) - int(s_int) % (10 ** (s_len-j))
        return s_int - 1

    @staticmethod
    def get_tidy_numbers(s_int):
        tidy = s_int
        while not TidyNumbers.is_tidy(tidy):
            tidy = TidyNumbers.cut_and_return(tidy)
        return tidy

    @staticmethod
    def main():
        t = int(input())
        for i in range(0, t):
            s = input()
            print('Case #%s: %s' % (i+1, TidyNumbers.solve(int(s))))

if __name__ == "__main__":
    TidyNumbers.main()

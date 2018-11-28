#include <cstddef>
#include <cstdint>
#include <iostream>

using namespace std;

#define MAXDIGITS 18

class Number
{
public:
    Number(uint64_t n)
    {
        size_t i = 0;
        while (n != 0) {
            digits[i] = n % 10;
            n /= 10;
            ++i;
        }
        for (; i < MAXDIGITS; ++i) {
            digits[i] = 0;
        }
    }

    operator uint64_t() const {
        uint64_t n = 0;
        uint64_t mul = 1;
        for (size_t i = 0; i < MAXDIGITS; ++i) {
            n += mul*digits[i];
            mul *= 10;
        }
        return n;
    }

    void makeTidy() {
        while (true) {
            size_t vi = firstViolationIndex();
            if (vi == MAXDIGITS) {
                return;
            }
            for (size_t i = 0; i <= vi; ++i) {
                digits[i] = 0;
            }
            decrease();
        }
    }

private:
    size_t firstViolationIndex() const {
        size_t i = MAXDIGITS;
        while ((i > 0) && (digits[i - 1] == 0)) {
            --i;
        }
        if (i == 0) {
            return MAXDIGITS;
        }
        --i;
        char last = digits[i];
        while (i > 0) {
            --i;
            char curr = digits[i];
            if (curr < last) {
                return i;
            }
            last = curr;
        }
        return MAXDIGITS;
    }

    void decrease() {
        size_t i = 0;
        while (digits[i] == 0) {
            digits[i] = 9;
            ++i;
        }
        --digits[i];
    }

private:
    char digits[MAXDIGITS];
};


int main()
{
    size_t t;
    cin >> t;
    for (size_t i = 1; i <= t; ++i) {
        uint64_t u;
        cin >> u;
        Number n(u);
        n.makeTidy();
        cout << "Case #" << i << ": " << n << endl;
    }
}
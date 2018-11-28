
/*
 * Michael V. Antosha
 * 2017
 * Michael.Antosha@gmail.com
 * http://mivael.in.ua
 */

#include <iostream>
using std::endl;
// using std::clog;

#include <cstdint>

#include <cassert>

typedef int64_t num_t;

static constexpr int MAX_BASE10_EXPONENT = 18;
static constexpr int MAX_BASE10_EXPONENT_CACHE = MAX_BASE10_EXPONENT + 1;

static num_t pow10[1 + MAX_BASE10_EXPONENT_CACHE];

static inline bool isTidy(num_t num)
{
    num_t last_dig = 10;
    for (;;)
    {
        const num_t dig = num % 10;
        if (dig > last_dig)  return false;
        last_dig = dig;

        num /= 10;
        if (num == 0)  break;
    }
    return true;
}

static inline num_t getdig(const num_t num, const int exp)
{
    return (num / pow10[exp]) % 10;
}

static inline void decr(num_t& num, const int exp)
{
    assert(pow10[exp] <= num);
    num -= pow10[exp];
}

static inline void setdig(num_t& num, const int exp, const num_t digit)
{
    // clog << "num = " << num << ", exp = " << exp << ", digit = " << digit << "." << endl;
    // clog << "pow10: " << pow10[exp+1] << ", " << pow10[exp] << "." << endl;
    num =
        num / pow10[exp+1] * pow10[exp+1]
        + (num % pow10[exp+1]) % pow10[exp]
        + digit * pow10[exp];
    // clog << "\t\t""num = " << num << "." << endl;
}

static num_t lastTidy(const num_t N)
{
    num_t fixed_num = N;
    for (;;)
    {
        bool is_fixed = false;
        for (int exp = MAX_BASE10_EXPONENT;  exp > 0;  --exp)
        {
            if (getdig(fixed_num, exp) <= getdig(fixed_num, exp-1))  continue;

            decr(fixed_num, exp);
            for (int e2 = 0;  e2 < exp;  ++e2)  setdig(fixed_num, e2, 9);
            is_fixed = true;
            break;
        }

        if (!is_fixed)  break;
    }
    return fixed_num;
}

int main(void)
{
    using std::cin;
    std::ios_base::sync_with_stdio(false);  cin.tie(0);

    pow10[0] = 1;
    for (int exp = 1;  exp <= MAX_BASE10_EXPONENT_CACHE;  ++exp)
        pow10[exp] = 10 * pow10[exp-1];

    int T;  cin >> T;
    for (int tc = 1;  tc <= T;  ++tc)
    {
        num_t N;  cin >> N;

        std::cout << "Case #" << tc << ": " << lastTidy(N) << endl;
    }
    return 0;
}

#include <iostream>

bool is_tidy(unsigned long long n)
{
    auto k = n;
    auto last_digit = 9LL;

    while(k)
    {
        auto digit = k % 10;

        if(digit > last_digit)
            return false;

        k /= 10;
        last_digit = digit;
    }

    return true;
}

int main()
{
    int t;
    unsigned long long n;

    std::cin >> t;

    for(int test = 1; test <= t; ++test)
    {
        for(std::cin >> n; n > 0; --n)
        {
            if(is_tidy(n))
            {
                std::cout << "Case #" << test << ": " << n << '\n'; 
                break;
            }
        }
    }
}

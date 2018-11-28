#include <iostream>

typedef unsigned long long int ll;

bool tidy(ll n)
{
    int a, b;

    if(n % 10 == 0)
        return false;

    do
    {
        a = n % 10;
        n /= 10;
        b = n % 10;

        if(a < b)
            return false;
    } while (n);

    return true;
}
int main()
{
    int t;
    std::cin >> t;
    
    for(int i = 1; i <= t; ++i)
    {
        std::cout << "Case #" << i << ": ";
        ll n;
        std::cin >> n;
        while(n)
        {
            if(tidy(n))
            {
                std::cout << n << '\n';
                break;
            }

            --n;
        }
    }
}
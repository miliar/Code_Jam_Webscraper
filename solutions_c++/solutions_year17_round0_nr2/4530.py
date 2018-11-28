#include <iostream>
#include <string>

using namespace std;

unsigned long long int lastTydiNumber(unsigned long long int n)
{
    unsigned long long int i = 10;

    while((n / i) > 0)
    {
        unsigned long long int current = (n % i) / (i / 10);
        unsigned long long int next    = (n % (i * 10)) / i;

        if(current < next)
        {
            n -= (n % i) + 1;
        }

        i *= 10;
    }

    return n;
}

int main()
{
    int t; cin >> t;

    for(int i = 0; i < t; i++)
    {
        unsigned long long int n; cin >> n;

        cout << "Case #" << (i + 1) << ": " << lastTydiNumber(n) << endl;
    }
}
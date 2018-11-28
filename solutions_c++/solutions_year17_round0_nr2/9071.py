#include <iostream>
#include <string>
#include <vector>

using namespace std;

unsigned long long getTidy(unsigned long long a)
{
    unsigned long long b = a;
    unsigned long long c = 10;
    while(b >= 10)
    {
        if(b % 10 < (b / 10) % 10)
            a -= a % c + 1;
        b = a / c;
        c *= 10;
    }
    return a;
}

int main()
{
    int t;
    unsigned long long a;
    cin >> t;
    for(int i = 0; i < t; ++i)
    {
        cin >> a;
        cout << "Case #" << (i + 1) << ": " << getTidy(a) << endl;
    }
}

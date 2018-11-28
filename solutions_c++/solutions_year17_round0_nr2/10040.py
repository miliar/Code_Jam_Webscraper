#include <iostream>
using namespace std;

bool tidy(long long x) 
{
    int prev = 10;
    while(x > 0)
    {
        int digit = x % 10;
        if(prev < digit)
        {
            return false;
        }
        x /= 10;
        prev = digit;
    }
    return true;
}

int main(int argc, char *argv[])
{
    int t;
    cin >> t;

    for(int i = 0; i < t; ++i)
    {
        long long n;
        cin >> n;

        for(long long x = n; x >= 0; --x)
        {
            if(tidy(x))
            {
                cout << "Case #" << i + 1 << ": " << x << endl;
                break;
            }
        }
    }
}

#include <iostream>
using namespace std;

bool IsTidy(unsigned long n)
{
    if (n < 10) return true;
    unsigned long s = n/10;
    int r = n % 10;
    int rs = s % 10;
    if (r < rs) return false;
    return IsTidy(s);
}

void Process(unsigned long n)
{
    while (n >= 1)
    {
        if (IsTidy(n))
        {
            cout << n << endl;
            return;
        }
        else
        {
            n--;
        }
    }
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i<=T; i++)
    {
        unsigned long n;
        cin >> n;
        cout << "Case #" << i << ": ";
        Process(n);
    }
}

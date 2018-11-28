#include <iostream>
using namespace std;

typedef long long ll;
int T;

int main()
{
    ll n, k;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> n >> k;
        cout << "Case #" << t << ": ";
        ll cursize = n, curnum1 = 1, curnum2 = 0 /*num of cursize+1*/;
        ll nextsize, nextnum1, nextnum2;
        ll lastint;
        while (k > 0)
        {
            nextsize = (cursize - 1) / 2;
            if (cursize & 1)
            {
                nextnum1 = 2 * curnum1 + curnum2;
                nextnum2 = curnum2;
            }
            else
            {
                nextnum1 = curnum1;
                nextnum2 = curnum1 + 2 * curnum2;
            }

            if (curnum2)
            {
                k -= curnum2;
                lastint = cursize + 1;
            }

            if (k > 0 && curnum1)
            {
                k -= curnum1;
                lastint = cursize;
            }

            cursize = nextsize;
            curnum1 = nextnum1;
            curnum2 = nextnum2;
        }
        cout << lastint / 2 << " " << (lastint - 1) / 2 << endl;
    }
    return 0;
}


#include <iostream>
#include <string>
#include <cmath>

using namespace std;
typedef long long ll;
typedef long double ld;

ll GetNumberOfDigits(ll i)
{
    return i > 0 ? (ll)log10((ld)i) + 1 : 1;
}

void calc(ll n)
{
    // get the first and second digits and counting

    int lastKnownDigit, num = GetNumberOfDigits(n);
    if (num == 0)
    {
        cout << 0;
        return;
    }
    if (num == 1)
    {
        cout << n;
        return;
    }
    ll temp = n;
    lastKnownDigit = 0;
    // cout << num << endl;
    for (int i = 0; i < num - 1; i++)
    {
        ld temp = ld(n) / ld(pow(10, num - i - 1));
        int firstDigit = long(temp) % 10;
        int secondDigit = long(temp * 10) % 10;
        // cout << "temp: " << temp <<"f: " << firstDigit << " second: " << secondDigit<< endl;
        if (firstDigit < secondDigit)
        {
            lastKnownDigit = i + 1;
            // cout << "lastKnownDigit: " << lastKnownDigit << endl;
        }
        if (firstDigit > secondDigit)
        {
            lastKnownDigit++;
            // cout << " i:" << i << " f:"<< temp / pow(10, num -i -2) << ":" << secondDigit << endl;
            temp = ld(n) / ld(pow(10, num - lastKnownDigit));
            // cout << ll(temp )<< pow(10, num -lastKnownDigit) << endl;
            // cout << ll(temp)*pow(10, num -lastKnownDigit) << endl;
            // cout << ll(temp)*pow(10, num -lastKnownDigit) -1 << endl;
            if (ll(temp) > 1)
            {
                cout << ll(temp) - 1;
            }
            for (int t = 0; t < num - lastKnownDigit; t++)
            {
                cout << 9;
            }

            // return (ll(temp)*pow(10, num -lastKnownDigit)) -1;
            return;
        }
    }
    cout << n;
    return;
}

int main()
{
    int T, i;
    ll n;
    cin >> T;
    i = T;
    while (i-- > 0)
    {
        cin >> n;
        cout << "Case #" << T - i << ": ";
        calc(n);
        cout << endl;
    }
}
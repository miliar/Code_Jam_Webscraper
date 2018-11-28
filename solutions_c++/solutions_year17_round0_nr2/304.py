#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        long long n;
        cin >> n;

        for (int z = 0; z < 21; z++)
        {
            long long p = 1;
            for (; p < n; p *= 10);

            for (; p >= 1; p /= 10)
                if (n / p % 10 < n / p / 10 % 10)
                {
                    n -= n % (p * 10);
                    n--;
                    break;
                }
        }

        cout << "Case #" << tt << ": " << n << endl;
    }

    return 0;
}

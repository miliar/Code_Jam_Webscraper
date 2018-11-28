#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int t;

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("out.txt");
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
    cout.precision(16);

    cin >> t;
    for (int z = 0; z < t; z++)
    {
        int n;
        long double d, ans = 0;

        cin >> d >> n;
        for (int i = 0; i < n; i++)
        {
            long double k, s;
            cin >> k >> s;
            ans = max(ans, (d - k) / s);
        }

        cout << "Case #" << z + 1 << ": " << d / ans << '\n';
    }
    return 0;
}

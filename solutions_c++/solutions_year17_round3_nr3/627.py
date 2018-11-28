#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int t;

int main()
{
    ifstream cin("C-small-1-attempt0.in");
    ofstream cout("out.txt");
    ios_base::sync_with_stdio(false), cin.tie(nullptr);
    cout.precision(16);

    cin >> t;
    for (int step = 1; step <= t; step++)
    {
        int n, k;
        double u, ans = 1.0;
        vector <double> v;

        cin >> n >> k >> u;
        v.resize(n);
        for (int i = 0; i < n; i++)
            cin >> v[i];

        sort(v.begin(), v.end());

        double l = 0.0, m, r = 1.0;
        for (int z = 0; z < 300; z++)
        {
            double now = u;
            m = (l + r) / 2;
            for (int i = n - 1; i >= n - k; i--)
            {
                if (v[i] < m)
                    now -= m - v[i];

                if (now < 0.0)
                {
                    r = m;
                    break;
                }
                if (i == n - k)
                    l = m;
            }
        }

        for (int i = n - 1; i >= n - k; i--)
            ans *= max(v[i], l);

        cout << "Case #" << step << ": ";
        cout << ans << endl;
    }
    return 0;
}

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        int n, k;
        double u;
        cin >> n >> k >> u;

        vector<double> a(n);
        for (int i = 0; i < n; i++)
            cin >> a[i];

        sort(a.begin(), a.end());
        a.push_back(1);
        for (k = 1; k <= n; k++)
        {
            if ((a[k] - a[k - 1]) * k > u)
                break;

            u -= (a[k] - a[k - 1]) * k;
        }

        for (int i = 0; i < k; i++)
            a[i] = a[k - 1] + u / k;

        double p = 1;
        for (int i = 0; i < n; i++)
            p *= a[i];

        cout.setf(ios::fixed);
        cout.precision(13);
        cout << "Case #" << tt << ": " << p << endl;
    }

    return 0;
}

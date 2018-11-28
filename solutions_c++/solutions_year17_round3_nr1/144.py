#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

const double pi = acos(-1.0);

int main()
{
    int t;
    cin >> t;

    for (int tt = 1; tt <= t; tt++)
    {
        int n, k;
        cin >> n >> k;

        vector<pair<double, double> > c(n);
        for (int i = 0; i < n; i++)
        {
            cin >> c[i].second >> c[i].first;
            c[i].first *= 2 * c[i].second;
            c[i].second *= c[i].second;
        }

        sort(c.begin(), c.end());
        reverse(c.begin(), c.end());

        double a = 0;
        for (int i = 0; i < n; i++)
        {
            double v = c[i].second + c[i].first;

            for (int j = 0, t = 1; j < n && t < k; j++)
                if (j != i && c[j].second <= c[i].second)
                {
                    v += c[j].first;
                    t++;
                }

            a = max(a, v);
        }

        cout.setf(ios::fixed);
        cout.precision(13);
        cout << "Case #" << tt << ": " << a * pi << endl;
    }

    return 0;
}

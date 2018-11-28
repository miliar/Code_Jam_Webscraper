#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t; cin >> t;

    for(int i = 0; i < t; i++)
    {
        int d, n; cin >> d >> n;

        double maxT = 0;
        for(int j = 0; j < n; j++)
        {
            int k, s; cin >> k >> s;

            double t = (d - k) / (double)s;

            maxT = max(maxT, t);
        }

        double speed = d / maxT;

        cout << "Case #" << (i+1) << ": " <<  fixed << setprecision(6) << speed << endl;
    }
}

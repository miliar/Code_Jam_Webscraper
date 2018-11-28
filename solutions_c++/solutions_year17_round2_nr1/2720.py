/**
 * http://code.google.com/codejam/contest/8294486/dashboard#s=p0
 */

#include <bits/stdc++.h>

using namespace std;


int main()
{
    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t)
    {
        int D, N;
        cin >> D >> N;

        double max_t = 0;
        for (int i = 0; i < N; ++i)
        {
            int Ki, Si;
            cin >> Ki >> Si;

            assert(Si);
            max_t = max(max_t, double(D - Ki) / Si);
        }

        double cruise_speed = D / max_t;

        cout << "Case #" << t << ": " << std::fixed << std::setprecision(6) << cruise_speed << '\n';
    }

    return 0;
}

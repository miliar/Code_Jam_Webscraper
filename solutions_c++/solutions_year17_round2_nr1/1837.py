#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        double d, n;
        cin >> d >> n;
        double time = 0;
        for(int i = 0; i < n; ++i) {
            double k, s;
            cin >> k >> s;
            time = max(time, ((d-k)/s));
        }
        //cout.precision(6);
        cout << fixed << setprecision(6) << d/time << endl;
    }
    return 0;
}

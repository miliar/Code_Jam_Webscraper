#include <bits/stdc++.h>
using namespace std;

#define ifthen(x, y, z) (x ? y: z)
#define mp make_pair
#define mt make_tuple

const int INF = 1e9 + 1;
const double pi = acos(-1);

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.precision(20);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i+1 << ": ";
        int n, d;
        cin >> d >> n;
        double mx_t = 0;
        for (int j = 0; j < n; ++j) {
            int s, k;
            cin >> k >> s;
            double t = (d - k)/(double)s;
            if (t > mx_t)
                mx_t = t;
        }
        cout << d/mx_t << '\n';
    }
    return 0;
}

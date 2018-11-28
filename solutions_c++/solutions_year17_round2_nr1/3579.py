#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using ld = long double;

const ld kEps = 0.0000001;

int main(int argc, char **argv) {
    ios::sync_with_stdio(false);
    srand(time(0));

#ifdef HOME
    freopen("/home/acarus/Desktop/io/input.txt", "r", stdin);
    freopen("/home/acarus/Desktop/io/output.txt", "w", stdout);
//    /home/acarus/Desktop/io/output.txt
#endif

    int t;
    cin >> t;
    for (int test_case = 1; test_case <= t; ++test_case) {
        ld dest;
        int n;
        cin >> dest >> n;
        vector<pair<ld, ld>> v(n + 1);
        ld time = 0;
        for (int i = 1; i <= n; ++i) {
            cin >> v[i].first >> v[i].second;
            ld ct = (dest - v[i].first) / v[i].second;
            time = max(time, ct);
        }

        cout << "Case #" << test_case << ": ";
        cout << fixed << setprecision(7) << (time > 0 ? dest / time : 10e9);
        cout << endl;
    }
    return 0;
}
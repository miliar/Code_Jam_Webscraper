#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using ld = long double;

const ld PI = 3.141592653589793;

int main(int argc, char **argv) {
    ios::sync_with_stdio(false);
    srand(time(0));

#ifdef HOME
    freopen("/home/acarus/Desktop/io/input.txt", "r", stdin);
    freopen("/home/acarus/Desktop/io/output.txt", "w", stdout);
#endif

    int t;
    cin >> t;
    for (int test_case = 1; test_case <= t; ++test_case) {
        int n, k;
        cin >> n >> k;

        vector<pair<ld, ld>> v;

        ld r, h;
        for (int i = 0; i < n; ++i) {
            cin >> r >> h;
            v.push_back(make_pair(r ,h));
        }

        sort(begin(v), end(v), greater<pair<ld, ld>>());
        ld ans = 0;
        for (int i = 0; i + k - 1 < n; ++i) {
            ld local_ans = PI*v[i].first*v[i].first + 2*PI*v[i].first * v[i].second;
            multiset<ld> ss;
            for (int j = i + 1; j < n; ++j) {
                ss.insert(-(2*PI*v[j].first * v[j].second));
            }

            for (int j = 0; j < k - 1; ++j) {
                local_ans += -(*begin(ss));
                ss.erase(begin(ss));
            }
            ans = max(ans, local_ans);
        }
        cout << "Case #" << test_case << ": " << setprecision(10) << fixed <<    ans << endl;
    }
    return 0;
}
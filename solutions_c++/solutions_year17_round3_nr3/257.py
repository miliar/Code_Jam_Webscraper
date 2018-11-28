#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int n, k;
ld u;

int main()
{
    //freopen("C-small-1-attempt0.in", "r", stdin);
    //freopen("C-small-1-attempt0.out", "w", stdout);

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for (int ttt = 1; ttt <= T; ++ttt) {
        cin >> n >> k >> u;
        vector<ld> v;
        v.push_back(1);
        for (int i = 0; i < n; ++i) {
            ld x;
            cin >> x;
            v.push_back(x);
        }
        sort(v.begin(), v.end(), greater<ld>());
        for (int i = 1; i <= n && fabs(u) > 1e-9; ++i) {
            ld delta = v[v.size() - 2] - v.back();
            if (delta * i <= u) {
                u -= delta * i;
                v.pop_back();
            } else {
                v.back() += u / i;
                break;
            }
        }
        ld ans = powl(v.back(), n + 2 - v.size());
        v.pop_back();
        while (v.size())
            ans *= v.back(), v.pop_back();
        cout << "Case #" << ttt << ": " << setprecision(17) << fixed << ans << endl;
    }

    return 0;
}

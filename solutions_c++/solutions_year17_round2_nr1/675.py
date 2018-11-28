// Kappa 123
#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define FILE "file"

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

const int INF = numeric_limits<int>::max();
const ll LLINF = numeric_limits<ll>::max();
const ull ULLINF = numeric_limits<ull>::max();
const double PI = acos(-1.0);

pair<long long, long long> h[1010];

int main()
{
    freopen(FILE".in", "r", stdin);
    freopen(FILE".out", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int T;
    cin >> T;
    for(int tcase = 1; tcase <= T; tcase++)
    {
        long long d, n;
        cin >> d >> n;
        for(int i = 0; i < n; i++)
            cin >> h[i].first >> h[i].second;
        sort(h, h + n);
        double mx = 0;
        for(int i = n - 1; i >= 0; i--)
            mx = max(mx, 1.0 * (d - h[i].first) / (1.0 * h[i].second));
        cout << "Case #" << tcase << ": ";
        cout << setprecision(10) << fixed << d / mx << '\n';
    }
    return 0;
}

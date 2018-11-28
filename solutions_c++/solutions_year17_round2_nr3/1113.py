#include <bits/stdc++.h>

#define F first
#define S second
#define prev azaza
#define mp make_pair
#define pb push_back

using namespace std;
typedef long long ll;
typedef long double ld;

const int max_n = 101;
ld inf = 1e18;
int n;

ll d[max_n][max_n];
ll hdist[max_n];
ll hspeed[max_n];
ll dist[max_n];

map<pair<int, int>, ld> dp;

ld f(int city, int horse) {
    pair<int, int> p = mp(city, horse);
    if (dp.count(p)) {
        return dp[p];
    }
    if (city == n - 1) {
        return 0;
    }
    ll hd = dist[city] - dist[horse];
    ll needd = dist[city + 1] - dist[city];
    ll canh = hdist[horse] - hd;
    ld mint = inf;
    if (canh >= needd) {
        mint = min(mint, f(city + 1, horse) + 1.0 * needd / hspeed[horse]);
    }
    if (hdist[city] >= needd) {
        mint = min(mint, f(city + 1, city) + 1.0 * needd / hspeed[city]);
    }
    dp[p] = mint;
    return mint;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for (int I = 1; I <= T; ++I) {
        int q;
        dp.clear();
        cin >> n >> q;
        for (int i = 0; i < n; ++i) {
            cin >> hdist[i] >> hspeed[i];
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                cin >> d[i][j];
            }
        }
        dist[0] = 0;
        for (int i = 1; i < n; ++i) {
            dist[i] = dist[i - 1] + d[i - 1][i];
           // cout << dist[i] << endl;
        }
        int a;
        cin >> a >> a;
        cout << "Case #" << I << ": " << fixed << setprecision(9) << f(0, 0) << endl;
    }
    return 0;
}


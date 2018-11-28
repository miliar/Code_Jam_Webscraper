#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define INF (1 << 30)
#define SQR(a) ((a) * (a))

using namespace std;

const int N = 1111;

double f[N][N];

double calc_area(pair<double, double> p, int i) {
    double ans = 0;
    if (i == 1)
        ans += M_PI * p.first * p.first;
    ans += 2 * M_PI * p.first * p.second;
    return ans;
}

void solve() {
    int n, k;
    cin >> n >> k;
    vector<pair<int, int>> v;
    for (int i = 0; i < n; i++)  {
        int x, y;
        cin >> x >> y;
        v.push_back({x, y});
        //printf("calc %d %d = %f (%f)\n", x, y, calc_area({x, y}, 1), calc_area({x, y}, 0));
    }
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            f[i][j] = 0;
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            f[i][j] = f[i - 1][j];
            f[i][j] = max(f[i][j], f[i - 1][j - 1] + calc_area(v[i - 1], j));
            //cerr << i << " " << j << " " << f[i][j] << endl;
        }
    }

    printf("%.9f", f[n][k]);
}

int main()
{
    //freopen("input.txt", "r", stdin);
    
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }
        
    return 0;
}

#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <cmath>
#include <set>
#include <unordered_map>
#include <map>
#include <functional>
#include <iomanip>
#include <vector>
#include <utility>

using namespace std;

typedef long long ll;
typedef long double ld;

const bool debug = false;

/*
ld solve (){
    int n, q;
    cin >> n >> q;
    vector<pair<int, int>> hr(n);
    int i;
    for(i = 0; i < n; i++) {
        cin >> hr[i].first >> hr[i].second;
    }
    int dis[101][101];
    int j;
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            cin >> dis[i][j];
        }
    }
    vector<pair<int, int>> qr(n);
    for(i = 0; i < q; i++) {
        cin >> qr[i].first >> qr[i].second;
    }
    ld dp[101];
    dp[n - 1] = 0;
    for(i = n - 2; i >= 0; i--) {
        dp[i] = 1e14;
        ld tot_dis = 0;
        for(j = i + 1; j < n; j++) {
            tot_dis += dis[j - 1][j];
            if(tot_dis <= hr[i].first) {
                dp[i] = min(dp[i], tot_dis / ((ld)hr[i].second) + dp[j]);
            }
        }
    }
    return dp[0];


} */




void solve() {
    int n, q;
    cin >> n >> q;
    vector<pair<int, int>> hr(n);
    int i;
    for(i = 0; i < n; i++) {
        cin >> hr[i].first >> hr[i].second;
    }
    int dis[101][101];
    int j;
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            cin >> dis[i][j];
        }
    }
    vector<pair<int, int>> qr(q);
    for(i = 0; i < q; i++) {
        cin >> qr[i].first >> qr[i].second;
        qr[i].first--;
        qr[i].second--;
    }

    ll df[101][101];
    ll inf = 1e12;
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            df[i][j] = inf;
            if(dis[i][j] != -1) {
                df[i][j] = dis[i][j];
            }
        }
    }

    int k;
    for(k = 0; k < n; k++) {
        for(i = 0; i < n; i++) {
            for(j = 0; j < n; j++) {
                df[i][j] = min(df[i][j], df[i][k] + df[k][j]);
            }
        }
    }
    ld mt[101][101];

    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            mt[i][j] = inf;
            if(df[i][j] <= hr[i].first) {
                mt[i][j] = df[i][j] / ((ld)hr[i].second);
            }

        }
    }
    for(k = 0; k < n; k++) {
        for(i = 0; i < n; i++) {
            for(j = 0; j < n; j++) {
                mt[i][j] = min(mt[i][j], mt[i][k] + mt[k][j]);
            }
        }
    }
    for(auto pr: qr) {
        //cout << mt[pr.first][pr.second] << fixed << setprecision(7) << " ";
        cout << fixed << setprecision(7) << mt[pr.first][pr.second] << " ";
    }


}

int main() {
   ios_base::sync_with_stdio(false);
   if(!debug) {
        freopen("large.in", "r", stdin);
        freopen("large.out", "w", stdout);
    }
    int t;
    cin >> t;
    int i;
    for(i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';


        cerr << "Case " << i << '\n';
    }
    return 0;
}

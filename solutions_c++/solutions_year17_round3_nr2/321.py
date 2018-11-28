#include <bits/stdc++.h>
#define ll long long
#define int long long
#define F first
#define S second
using namespace std;

const int N = 1500;

pair <int, int> a[N], b[N];
int dp[N][(int)(N )][2], used1[N], used2[N];
int n, m;

void sol() {
    cin >> n >> m;
    memset(used1, 0, sizeof(used1));
    memset(used2, 0, sizeof(used2));
    for(int i = 1; i <= n; i++) {
        cin >> a[i].F >> a[i].S;
        a[i].S--;
        for(int j = a[i].F; j <= a[i].S; j++){
            used1[j]++;
        }
    }
    for(int i = 1; i <= m; i++) {
        cin >> b[i].F >> b[i].S;
        b[i].S--;
        for(int j = b[i].F; j <= b[i].S; j++){
            used2[j]++;
        }
    }
   /* for(int i = 1; i <= 1440; i++) {
        used1[i] += used1[i - 1];
        used2[i] += used2[i - 1];
    }*/
    memset(dp, 100, sizeof(dp));
    dp[0][0][0] = dp[0][0][1] = 0;
    for(int i = 0; i <= 1440; i++) {
        for(int j = 0; j <= 720; j++) {
            if(dp[i][j][0] <= 500) {
                for(int nx = i + 1; nx <= 1440; nx++) {
                    if(used1[nx - 1]) break;
                    //cout << i << ' ' << j << ' ' << nx << endl;
                    if(dp[nx][j + nx - i][1] <= dp[i][j][0] + 1) break;
                    dp[nx][j + nx - i][1] = min(dp[nx][j + nx - i][1], dp[i][j][0] + 1);
                }
            }
            if(dp[i][j][1] <= 500) {
                for(int nx = i + 1; nx <= 1440; nx++) {
                    if(used2[nx - 1]) break;
                    if(dp[nx][j][0] <= dp[i][j][1] + 1) break;
                    dp[nx][j][0] = min(dp[nx][j][0], dp[i][j][1] + 1);
                }
            }
        }
    }
    ll minl = min(dp[1440][720][0], dp[1440][720][1]);
    if(minl % 2 == 1) minl--;
    cout << minl;
}

main() {
    freopen("B-large (1).in", "r", stdin);
    freopen("output.txt", "w", stdout);
    //ios_base::sync_with_stdio(0);
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++) {
        cout << "Case #" << i << ": ";
        sol();
        cout << endl;
    }
}


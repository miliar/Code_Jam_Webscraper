#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <set>
#include <unordered_map>
#include <queue>
#include <sstream>
#include <iomanip>
using namespace std;

//#pragma comment(linker, "/STACK:102400000,102400000")

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, double> pid;
typedef pair<ll, ll> pll;

const int MAX = 111;

int E[MAX], S[MAX];
int D[MAX][MAX];

int N, Q;

double dis[MAX];
double dp[MAX];

void solve() {
    scanf("%d%d", &N, &Q);
    for (int i = 0; i < N; ++i) {
        scanf("%d%d", &E[i], &S[i]);
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            scanf("%d", &D[i][j]);
        }
    }
    for (int q = 0; q < Q; ++q) {
        int u, v;
        scanf("%d%d", &u, &v);
        
        for (int i = 0; i < N-1; ++i) {
            dis[i+1] = dis[i] + D[i][i+1];
        }
        
        for (int i = 1; i <= N; ++i) {
            dp[i] = 1e18;
        }
        
        for (int i = 0; i < N; ++i) {
            for (int j = i+1; j < N; ++j) {
                double cur = dis[j] - dis[i];
                if (cur > E[i]) continue;
                double val = dp[i] + cur/S[i];
                if (val < dp[j]) {
                    dp[j] = val;
                }
            }
        }
        
        printf("%.6lf\n", dp[N-1]);
    }
}

int main() {
    
    //freopen("/Users/zyeric/Desktop/workspace/workspace/in.txt", "r", stdin);
    
    ios::sync_with_stdio(false);
    cout << fixed << setprecision(16);
    
    int T;
    cin >> T;
    
    for (int kase = 1; kase <= T; ++ kase) {
        cout << "Case #" << kase << ": ";
        solve();
        cerr << "solved " << kase << endl;
    }
    
    return 0;
}

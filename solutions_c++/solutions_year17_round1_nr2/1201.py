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

const int MAX = 100;

int N, P;
int A[MAX];
int B[MAX][MAX];
int L[MAX][MAX];
int R[MAX][MAX];

//P 是否在 Q 的范围内
bool isOK(int P, int Q) {
    int low = Q - Q / 10;
    int high = Q + Q / 10;
    return low <= P && P <= high;
}

int dp[10][10];

void solve() {
    scanf("%d%d", &N, &P);
    for (int i = 0; i < N; ++i) {
        scanf("%d", &A[i]);
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < P; ++j) {
            scanf("%d", &B[i][j]);
        }
        sort(B[i], B[i]+P);
    }
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < P; ++j) {
            L[i][j] = -1;
            R[i][j] = -1;
        }
    }
    
    for (int i = 0; i < N; ++i) {
        int now = A[i];
        for (int j = 1;; ++j) {
            for (int k = 0; k < P; ++k) {
                bool flag = isOK(B[i][k], now);
                if (flag) {
                    if (L[i][k] == -1) {
                        L[i][k] = j;
                    }
                    R[i][k] = j;
                }
            }
            now += A[i];
            if (now >= 1200000) {
                break;
            }
        }
    }
    
    if (N == 1){
        int ans = 0;
        for (int i = 0; i < P; ++i) {
            if (L[0][i] != -1) {
                ans ++;
            }
        }
        printf("%d\n", ans);
        return;
    }
    
    for (int i = 0; i <= P; ++i) {
        for (int j = 0; j <= P; ++j) {
            dp[i][j] = 0;
        }
    }
    
    for (int i = 0; i < P; ++i) {
        for (int j = 0; j < P; ++j) {
            if (L[0][i] != -1 && L[1][j] != -1) {
                int tl = max(L[0][i], L[1][j]);
                int tr = min(R[0][i], R[1][j]);
                if (tl <= tr) {
                    dp[i+1][j+1] = dp[i][j] + 1;
                }
            }
            
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]);
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j]);
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1]);
        }
    }
    
    printf("%d\n", dp[P][P]);
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

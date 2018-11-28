#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <deque>
#include <cmath>
using namespace std;

deque<long long> label, num;
/*
void debug() {
    if(label.size() != num.size()) {
        cout << "size not same" << endl;
        return;
    }
    cout << "hehe" << endl;
    for(int i = 0;i < label.size();i ++) {
        cout << label.at(i) << " " << num.at(i) << endl;
    }
}
*/

#define pi acos(-1.0)

int dp[4];
int hehe[110][110][110];

inline int cal(int a, int b, int c) {
    int tt = a * 1 + b * 2 + c * 3;
    tt %= 4;
    if(tt == 0) return 1;
    else return 0;
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    int casenum;  scanf("%d", &casenum);
    for(int cs = 1; cs <= casenum; cs ++) {
        int N, P; scanf("%d%d", &N, &P);
        memset(dp, 0, sizeof(dp));
        for(int i = 0;i < N;i ++) {
            int tt; scanf("%d", &tt);
            dp[tt % P] ++;
        }
        int ans = dp[0];
        if(P == 2) {
            ans += (dp[1] + 1) / 2;
        } else if(P == 3) {
            int minr = min(dp[1], dp[2]);
            ans += minr;
            dp[1] -= minr;
            dp[2] -= minr;
            ans += (dp[1] + 2) / 3;
            ans += (dp[2] + 2) / 3;
        } else if(P == 4) {
            memset(hehe, 0, sizeof(hehe));
            hehe[0][0][0] = 0;
            hehe[1][0][0] = 1;
            hehe[0][1][0] = 1;
            hehe[0][0][1] = 1;
            hehe[1][1][0] = 1;
            hehe[1][0][1] = 1;
            hehe[0][1][1] = 1;
            for(int i = 0;i <= dp[1];i ++) {
                for(int j = 0;j <= dp[2];j ++) {
                    for(int k = 0;k <= dp[3];k ++) {
                        int t1 = 0;
                        int t2 = 0;
                        int t3 = 0;
                        if(k >= 1) {
                            t1 = hehe[i][j][k - 1] + cal(i, j, k - 1);
                        }
                        if(j >= 1) {
                            t2 = hehe[i][j - 1][k] + cal(i, j - 1, k);
                        }
                        if(i >= 1) {
                            t3 = hehe[i - 1][j][k] + cal(i - 1, j, k);
                        }
                        hehe[i][j][k] = max(t1, max(t2, t3));
                    }
                }
            }
            ans += hehe[dp[1]][dp[2]][dp[3]];
        }
        printf("Case #%d: %d\n", cs, ans);
    }
    return 0;
}

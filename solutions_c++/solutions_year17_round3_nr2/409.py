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
#define INF 0x3f3f3f3f
int table[1500];
int dp[1500][2][2][800];

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("out.out", "w", stdout);
    int casenum;  scanf("%d", &casenum);
    for(int cs = 1; cs <= casenum; cs ++) {
        memset(table, -1, sizeof(table));
        memset(dp, INF, sizeof(dp));
        int na, nb; scanf("%d%d", &na, &nb);
        for(int i = 0;i < na;i ++) {
            int st, ed; scanf("%d%d", &st, &ed);
            for(int j = st; j < ed;j ++) {
                table[j] = 0;
            }
        }
        for(int i = 0;i < nb;i ++) {
            int st, ed; scanf("%d%d", &st, &ed);
            for(int j = st; j < ed;j ++) {
                table[j] = 1;
            }
        }
        if(table[0] == -1) {
            dp[0][0][0][1] = 0;
            dp[0][1][1][0] = 0;
        }else if (table[0] == 0) {
            dp[0][0][0][1] = 0;
        } else {
            dp[0][1][1][0] = 0;
        }
        for(int i = 1;i < 1440;i ++) {
            for(int j = 0;j <= 720;j ++) {
                if(table[i] == -1) {
                    if(j > 0) {
                        dp[i][0][0][j] = min(dp[i-1][0][0][j-1], dp[i-1][1][0][j-1] + 1);
                        dp[i][0][1][j] = min(dp[i-1][0][1][j-1], dp[i-1][1][1][j-1] + 1);
                    }
                    dp[i][1][0][j] = min(dp[i-1][0][0][j] + 1, dp[i-1][1][0][j]);
                    dp[i][1][1][j] = min(dp[i-1][0][1][j] + 1, dp[i-1][1][1][j]);
                } else if (table[i] == 0) {
                    if(j > 0) {
                        dp[i][0][0][j] = min(dp[i-1][0][0][j-1], dp[i-1][1][0][j-1] + 1);
                        dp[i][0][1][j] = min(dp[i-1][0][1][j-1], dp[i-1][1][1][j-1] + 1);
                    }
                } else {
                    dp[i][1][0][j] = min(dp[i-1][0][0][j] + 1, dp[i-1][1][0][j]);
                    dp[i][1][1][j] = min(dp[i-1][0][1][j] + 1, dp[i-1][1][1][j]);
                }
            }
        }
        int ans = 100000000;
        for(int i = 0;i < 2;i ++) {
            for(int j = 0;j < 2;j ++) {
                if(i != j) {
                    ans = min(ans, dp[1439][i][j][720] + 1);
                } else {
                    ans = min(ans, dp[1439][i][j][720]);
                }
            }
        }
        printf("Case #%d: %d\n", cs, ans);
    }
    return 0;
}

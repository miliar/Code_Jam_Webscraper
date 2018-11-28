#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define PI acos(-1)
#define MOD 1000000007
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
const int M = 1450;
int dp[M][730][3];
bool have[3][M];
int n, k, start;
int calc(int i, int cur, bool turn) {
        if(i == 1440) {
                if(cur != 720) {
                        return 1e9;
                }
                return start != turn;
        }
        if(cur > 720) {
                return 1e9;
        }
        if(dp[i][cur][turn] != -1) {
                return dp[i][cur][turn];
        }
        int ans = 1e9;
        if(!turn) {
                if(have[0][i]) {
                        ans = min(ans, 1 + calc(i + 1, cur, 1));
                } else {
                        ans = min(ans, calc(i + 1, cur + 1, 0));
                        if(!have[1][i]) {
                                ans = min(ans, 1 + calc(i + 1, cur, 1));
                        }
                }
        } else {
                if(have[1][i]) {
                        ans = min(ans, 1 + calc(i + 1, cur + 1, 0));
                } else {
                        ans = min(ans, calc(i + 1, cur, 1));
                        if(!have[0][i]) {
                                ans = min(ans, 1 + calc(i + 1, cur + 1, 0));
                        }
                }
        }
        return dp[i][cur][turn] = ans;
}
int main()
{
        freopen("B-large.in", "r", stdin);
        freopen("out.txt", "w", stdout);
        int t, c = 0;
        scanf("%d", &t);
        while(t--) {
                memset(have, 0, sizeof have);
                c++;
                int AC, AJ;
                cin >> AC >> AJ;
                for(int i = 0; i < AC; i++) {
                        int c, d;
                        cin >> c >> d;
                        for(int j = c; j < d; j++) {
                                have[0][j] = 1;
                        }
                }
                for(int i = 0; i < AJ; i++) {
                        int c, d;
                        cin >> c >> d;
                        for(int j = c; j < d; j++) {
                                have[1][j] = 1;
                        }
                }
                memset(dp, -1, sizeof dp);
                start = 0;
                int x = calc(0, 0, 0);
                memset(dp, -1, sizeof dp);
                start = 1;
                int y = calc(0, 0, 1);
                printf("Case #%d: %d\n", c, min(x, y));
        }
        return 0;
}

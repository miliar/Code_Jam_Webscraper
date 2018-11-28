#include <bits/stdc++.h>
#define FOR(i, l, r) for (int i = int(l), __border_right##i = int(r); i < __border_right##i; i++)
#define STRUCT3(v1, v2, v3, name) struct name \
		{   \
			int v1, v2, v3; \
			name(int v1 = 0, int v2 = 0, int v3 = 0) : v1(v1), v2(v2), v3(v3) {} \
			friend bool operator < (const name& athis, const name& other) \
			{   \
				if (athis.v1 != other.v1) return athis.v1 < other.v1;   \
				if (athis.v2 != other.v2) return athis.v2 < other.v2;   \
				return athis.v3 < other.v3;   \
			}\
		}
#define PB push_back
#define LS (((k) << 1) + 1)
#define RS (((k) << 1) + 2)
#define LM ((l) + (r) >> 1)
#define RM (LM + 1)
//#define LOG(x) tb[(UI(x) * (UI)263572066) >> 27]
#define FST first
#define SCD second
#define retunr return
#define modp 1000000007
#define EPS 1e-7
#define INF 0x3f3f3f3f
#define MAX2 113
#define MAX3 1013
#define MAX4 10013
#define MAX5 100013
#define MAX6 1000013
#define MAXN
#define MANX MAXN
using namespace std;
typedef long long LL;
typedef unsigned int UI;
//typedef pair<int, int> P;

int num[4];
int dp[113][113][113][4];

int main()
{
    int T;
    freopen("A-large.in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &T);
    FOR(Ce, 1, T + 1) {
        int N, p;
        scanf("%d%d", &N, &p);
        int res = 0;
        memset(num, 0, sizeof(num));
        memset(dp, 0, sizeof(dp));
        FOR(i, 0, N) {
            int x;
            scanf("%d", &x);
            x %= p;
            num[x]++;
        }
        if (p == 2) {
            res = num[0] + (num[1] + 1) / 2;
        }
        else if (p == 3) {
            FOR(i, 0, 101) FOR(j, 0, 101) FOR(k, 0, 1) FOR(s, 0, 4) {
                if (i) {
                    dp[i][j][k][s] = max(dp[i][j][k][s], dp[i - 1][j][k][(s + p - 1) % p] + (s == 0));
                }
                if (j) {
                    dp[i][j][k][s] = max(dp[i][j][k][s], dp[i][j - 1][k][(s + p - 2) % p] + (s == 0));
                }
            }
            res = num[0] + dp[num[1]][num[2]][0][0];
        }
        else if (p == 4) {
            FOR(i, 0, 101) FOR(j, 0, 101) FOR(k, 0, 101) FOR(s, 0, 4) {
                if (i) {
                    dp[i][j][k][s] = max(dp[i][j][k][s], dp[i - 1][j][k][(s + p - 1) % p] + (s == 0));
                }
                if (j) {
                    dp[i][j][k][s] = max(dp[i][j][k][s], dp[i][j - 1][k][(s + p - 2) % p] + (s == 0));
                }
                if (k) {
                    dp[i][j][k][s] = max(dp[i][j][k][s], dp[i][j][k - 1][(s + p - 3) % p] + (s == 0));
                }
            }
            res = num[0] + dp[num[1]][num[2]][num[3]][0];
        }
        printf("Case #%d: %d\n", Ce, res);
    }
    return 0;
}

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

int N, C, M;
int num[1013];
int ps[1013];
int cnt(int x)
{
    int S = 0;
    int res = 0;
    FOR(i, 0, N) {
        S += num[i];
        if (S > (i + 1) * x) {
            return -1;
        }
        if (num[i] > x) {
            res += num[i] - x;
        }
    }
    return res;
}
int main()
{
    int T;
    freopen("B-large.in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &T);
    FOR(Ce, 1, T + 1) {
        scanf("%d%d%d", &N, &C, &M);
        memset(num, 0, sizeof(num));
        memset(ps, 0, sizeof(ps));
        int l = 0;
        FOR(i, 0, M) {
            int p, b;
            scanf("%d%d", &p, &b);
            num[p - 1]++;
            ps[b - 1]++;
            l = max(l, ps[b - 1]);
        }
        int r = M;
        while (l < r) {
            int m = (l + r) / 2;
            int c = cnt(m);
            if (c == -1) {
                l = m + 1;
            }
            else {
                r = m;
            }
        }
        printf("Case #%d: %d %d\n", Ce, l, cnt(l));
    }
    return 0;
}

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
#define MAXN MAX3
#define MANX MAXN
using namespace std;
typedef long long LL;
typedef unsigned int UI;
typedef pair<int, int> P;

int T;
char S[MAXN];

int main()
{
//    freopen("data.in", "r", stdin);
//    freopen("data.out", "w", stdout);
    scanf("%d", &T);
    FOR(Ce, 1, T + 1) {
        scanf(" %s", S);
        int n = strlen(S);
        FOR(i, 1, n) {
            if (S[i - 1] > S[i]) {
                int j = i - 1;
                while (j > 0 && S[j - 1] == S[i - 1]) {
                    j--;
                }
                S[j]--;
                FOR(t, j + 1, n) {
                    S[t] = '9';
                }
                break;
            }
        }
        char *str = S;
        while (*str == '0') {
            str++;
        }
        printf("Case #%d: %s\n", Ce, str);
    }
    return 0;
}

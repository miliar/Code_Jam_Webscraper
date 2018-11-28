#include <bits/stdc++.h>

#define rep(i, j, k) for(int i = (int) j; i < (int) k; ++i)
#define sz(x) ((int) (x).size())
#define ll long long
#define mp make_pair
#define pii pair<int, int >
#define fi first
#define se second
#define pb push_back
#define inf 0x3f3f3f3f
#define INF 0x3f3f3f3f3f3f3f
#define zero(x) memset((x), (0), sizeof (x))
#define zerox(x, y) memset((x), (y), sizeof (x))

using namespace std;

int main()
{
#ifdef PIT
freopen("B-large.in", "r", stdin);
freopen("B-large.out", "w", stdout);
#endif // PIT

    int T, ic = 1;
    for(scanf("%d", &T); T--; ic++){
        ll n;
        scanf("%I64d", &n);
        int g[20], t = -1;
        while(n) {
            g[++t] = (int)(n%10);
            n /= 10;
        }
        printf("Case #%d: ", ic);
        if(t == 0) {
            printf("%d\n", g[0]);
            continue;
        }
        int bg = t;
        for(int i = t-1; i >= 0; --i) {
            if(g[i] > g[bg]) {
                bg = i ;
            }
            else if(g[i] == g[bg]) continue;
            else {
                g[bg]--;
                for(int j = bg-1; j >= 0; --j) g[j] = 9;
                break;
            }
        }
        ll s = 0;
        for(int i = t; i >= 0; --i) s = s*10 + g[i];

        printf("%I64d\n", s);
    }
    return 0;
}

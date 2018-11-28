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

int n, r, y, b, o, g, v;

pii p[10];

int main()
{
#ifdef PIT
freopen("B-small-attempt2.in", "r", stdin);
freopen("B-small-attempt2.out", "w", stdout);
#endif // PIT

    int T, ic = 1;
    for(scanf("%d", &T); T--; ic++){
        printf("Case #%d: ", ic);
        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);


        p[0] = {r, 0}; p[1] = {y, 1}; p[2] = {b, 2};
        sort(p, p+3);
        vector<int > v; v.clear();
        p[2].fi -= p[1].fi;
        while(p[1].fi--) v.pb(p[2].se), v.pb(p[1].se);
        p[0].fi -= p[2].fi;
        while(p[2].fi--) v.pb(p[2].se), v.pb(p[0].se);
        if(p[0].fi < 0) {
            puts("IMPOSSIBLE");
            continue;
        }
        int flag = 1;
        int t = 2;
        for(int i = 0; i < p[0].fi; ++i) {
            v.insert(v.begin()+t, p[0].se);
            t += 3;
        }

        for(auto & x: v) {
            if(x==0) printf("R");
            else if(x==1) printf("Y");
            else printf("B");
        }
        puts("");
    }
    return 0;
}

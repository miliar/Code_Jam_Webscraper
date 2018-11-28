/**
 *    author:  [itmo] enot.1.10
 *    created: 21.01.2017 23:42:28       
**/
#define __USE_MINGW_ANSI_STDIO 0
#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),a.end()
#define pw(x) (1LL<<(x))

using namespace std;

typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef pair<int, int> pi;

const int inf = 1.01e9;
const dbl eps = 1e-9;

/* --- main part --- */

namespace flow
{
    const int maxn = 3e6 + 10;
    const int maxe = 2 * maxn;

    int head[maxn], next[maxe], to[maxe], flow[maxe], cost[maxe], ec = 1;
    int ST, EN, N = maxn;

    inline void setN(int n)
    {
        ST = n;
        EN = n + 1;
        N = n + 2;
    }

    inline void _add(int x, int y, int f, int c)
    {
        ++ec;
        to[ec] = y;
        next[ec] = head[x];
        head[x] = ec;
        flow[ec] = f;
        cost[ec] = c;
    }

    inline int add(int x, int y, int f, int c)
    {
        _add(x, y, f, c);
        _add(y, x, 0, -c);
        return ec - 1;
    }

    void clear()
    {
        forn(i, N) head[i] = 0;
        ec = 1;
    }

    ll d[maxn], p[maxn];
    int last[maxn];
    int used[maxn];

    pair<ll, ll> _calc(int flag)
    {
        const ll INF = 1e12;
        forn(i, N) p[i] = INF;
        p[ST] = 0;
        forn(_, N) forn(x, N) for (int e = head[x]; e; e = next[e]) if (flow[e] > 0)
        {
            int y = to[e];
            if (p[y] > p[x] + cost[e])
            {
                p[y] = p[x] + cost[e];
            }
        }

        ll resFlow = 0, resCost = 0;
        while (1)
        {
            forn(i, N) d[i] = INF, used[i] = 0;
            d[ST] = 0;
            forn(_, N)
            {
                int x = -1;
                forn(i, N) if (!used[i] && (x == -1 || d[x] > d[i])) x = i;
                used[x] = 1;
                if (d[x] == INF) break;
                for (int e = head[x]; e; e = next[e]) if (flow[e] > 0)
                {
                    int y = to[e];
                    ll len = cost[e] + p[x] - p[y];
                    if (d[y] > d[x] + len)
                    {
                        d[y] = d[x] + len;
                        last[y] = e;
                    }
                }
            }
            
            if (d[EN] == INF) break;
            
            ll realCost = d[EN] + p[EN] - p[ST];
            if (flag && realCost > 0) break;

            int pushed = inf;
            int x = EN;
            while (x != ST)
            {
                int e = last[x];
                pushed = min(pushed, flow[e]);
                x = to[e ^ 1];
            }

            resCost += realCost * pushed;
            resFlow += pushed;

            x = EN;
            while (x != ST)
            {
                int e = last[x];
                flow[e] -= pushed;
                flow[e ^ 1] += pushed;
                x = to[e ^ 1];
            }

            forn(i, N) p[i] += d[i];
        }
        return {resFlow, resCost};
    }

    pair<ll, ll> maxFlow()
    {
        return _calc(0);
    }          

    pair<ll, ll> minCost()
    {
        return _calc(1);
    }          

    // HOW TO USE::
    // -- add adges using add(x, y, f, c), call setN(n)
    // -- run maxFlow/minCost, returns pair(flow, cost)
}



int main(int argc, char* argv[])
{
    assert(freopen("1.in", "r", stdin));
    int tn;
    scanf("%d", &tn);
    int testL = 0, testR = tn;
    if (argc == 4)
    {
        sscanf(argv[1], "%d", &testL);
        sscanf(argv[2], "%d", &testR);
        assert(freopen(argv[3], "w", stdout));
    }
    else
    {
        assert(freopen("1.out", "w", stdout));
    }


    forn(tt, tn)
    {
        //READ
        int n, c, m;
        scanf("%d%d%d", &n, &c, &m);
        vector<pi> v(m);
        forn(i, m) scanf("%d%d", &v[i].F, &v[i].S);
        
        if (!(testL <= tt && tt < testR)) continue;
        printf("Case #%d: ", tt + 1);
        
        //SOLVE

        eprintf("test %d\n", tt);
        vi cnt(n);
        vector<vi> t(c);
        forn(i, m)
        {
            v[i].F--;
            v[i].S--;
            t[v[i].S].pb(i);
            cnt[v[i].F]++;
        }

        vi sum(n + 1);
        forn(i, n) sum[i + 1] = sum[i] + cnt[i];

        int mx = 0;
        forn(i, c) mx = max(mx, sz(t[i]));
        for (int i = 1; i <= n; ++i) mx = max(mx, (sum[i] + i - 1) / i);
        //eprintf("here\n");

        int res;
        while (1)
        {

            flow::clear();
            flow::ST = 0;
            flow::EN = 1;
        
            int cs = 2;
            forn(i, c)
            {
                flow::add(flow::ST, cs + i, sz(t[i]), 0);
            }
            int ts = cs + c;
            int ps = ts + m;
            flow::N = ps + n;
            forn(i, m)
            {
                flow::add(cs + v[i].S, ts + i, 1, 0);
                flow::add(ts + i, ps + v[i].F, 1, 0);
                for (int j = 0; j < v[i].F; ++j) flow::add(ts + i, ps + j, 1, 1);
            }
            forn(j, n) flow::add(ps + j, flow::EN, mx, 0);
        
        //eprintf("before flow\n");
            auto z = (flow::maxFlow());
        //eprintf("after flow\n");
            if (z.F != m)
            {
                eprintf("fail on %d\n", mx);
                mx++;
                continue;
            }
            res = z.S;
            break;
        }

        printf("%d %d\n", mx, res);

    }
            
    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}

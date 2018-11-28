#include <bits/stdc++.h>
using namespace std;

#define LL long long
#define NL '\n'
#define xx first
#define yy second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define si(x) scanf("%d",&x)
#define sl(x) scanf("%I64d",&x)
#define sd(x) scanf("%lf",&x)
#define ss(x) scanf("%s",x)
#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(i=j;i<=k;i++)
#define REV(i,j,k) for(i=j;i>=k;i--)
#define READ(f) freopen(f,"r",stdin)
#define WRITE(f) freopen(f,"w",stdout)
#define cnd tree[idx]
#define lnd tree[idx*2]
#define rnd tree[(idx*2)+1]
#define lndp (idx*2),(b),((b+e)/2)
#define rndp (idx*2+1),((b+e)/2+1),(e)
#define pi 2.0*acos(0.0)
#define MOD 1000000007
#define MAX 100005

string s, alp = "RYBOGV";
pii p[10];
vector <int> g[10];
int start;

void dfs(int u)
{
    p[u].xx--;
    s += alp[u];

    int v, k = 0, x = -1;

    for(int i = 0; i < g[u].size(); i++)
    {
        v = g[u][i];
        if(p[v].xx > k)
        {
            k = p[v].xx;
            x = v;
        }
        if(v == start && p[v].xx == k) x = v;
    }

    if(k > 0 && x >= 0) dfs(x);
}

int main()
{
    //READ("B-small-attempt0.in");
    //WRITE("B-small-attempt0.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0, n, i, j, k, cnt, sum;
    int r, o, y, gg, b, v;

    cin >> cases;

    g[0].pb(1);
    g[0].pb(2);
    g[0].pb(4);
    g[1].pb(0);
    g[1].pb(2);
    g[1].pb(5);
    g[2].pb(0);
    g[2].pb(1);
    g[2].pb(3);
    g[3].pb(2);
    g[4].pb(0);
    g[5].pb(1);

    while(cases--)
    {
        cin >> n;

        cin >> r >> o >> y >> gg >> b >> v;
        p[0] = mp(r, 0);
        p[1] = mp(y, 1);
        p[2] = mp(b, 2);
        p[3] = mp(o, 3);
        p[4] = mp(gg, 4);
        p[5] = mp(v, 5);

        k = 0;

        FOR(i,0,5)
        {
            if(p[k].xx < p[i].xx)
                k = i;
        }

        s = "";
        start = k;

        dfs(k);
        if(s.size() != n) s = "IMPOSSIBLE";
        else if(s.size() > 1 && s[0] == s[(int)(s.size())-1]) s = "IMPOSSIBLE";

        cout << "Case #" << ++caseno << ": " << s << NL;
    }

    return 0;
}



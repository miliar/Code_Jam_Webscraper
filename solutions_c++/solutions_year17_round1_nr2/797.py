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
#define MAX 2505

pii p[55][55];
LL a[55];

int cap[2505][2505], idx[55][55];
vector <int> g[2505];

int max_flow(int src, int sink)
{
    int i, j, u, v, mn, flow = 0, vis[MAX]={0}, p[MAX];
    queue <int> q;
    bool flag;

    while(1)
    {
        // BFS - discovering augmenting path
        while(!q.empty()) q.pop();
        mem(vis,0);
        q.push(src);
        vis[src] = 1;
        flag = false;

        while(!q.empty())
        {
            u = q.front();
            q.pop();

            for(int i = 0; i < (int)g[u].size(); i++)
            {
                v = g[u][i];
                if(vis[v] == 0 && cap[u][v] > 0)
                {
                    // save the parent
                    p[v] = u;
                    if(v == sink)
                    {
                        // found the sink
                        flag = true;
                        break;
                    }
                    vis[v] = 1;
                    q.push(v);
                }
            }
            if(flag) break;
        }

        if(!flag) break;
        // find the minimum of the path
        i = sink;
        mn = INT_MAX;
        while(i != src)
        {
            mn = min(mn, cap[ p[i] ][i]);
            i = p[i];
        }
        // adjust the flow
        i = sink;
        while(i != src)
        {
            cap[ p[i] ][i] -= mn;
            cap[i][ p[i] ] += mn;
            i = p[i];
        }
        // add the flow to the max flow
        flow += mn;
    }
    return flow;
}

int main()
{
    //READ("B-large.in");
    //WRITE("B-large.out");
    std::ios_base::sync_with_stdio(0);
    int cases, caseno=0, n, i, j, k, u, v;
    LL cnt, sum, x, y, ans, t;

    cin >> cases;

    while(cases--)
    {
        cin >> n >> k;

        FOR(i,1,n) cin >> a[i];

        int sink = 1;
        int src = 0;
        g[0].clear();
        g[1].clear();

        FOR(i,1,n)
        {
            FOR(j,1,k)
            {
                cin >> t;
                sum = ((t*10) / (9*a[i]));
                if(t*10 >= 9*a[i]*sum && t*10 <= 11*a[i]*sum) {}
                else
                {
                    sum++;
                    if(t*10 >= 9*a[i]*sum && t*10 <= 11*a[i]*sum) {}
                    else sum = 0;
                }
                cnt = (((t*10)+(11*a[i]-1)) / (11*a[i]));
                if(t*10 >= 9*a[i]*cnt && t*10 <= 11*a[i]*cnt) {}
                else if(cnt > 0)
                {
                    cnt--;
                    if(t*10 >= 9*a[i]*cnt && t*10 <= 11*a[i]*cnt) {}
                    else cnt = 0;
                }
                p[i][j] = mp(cnt, sum);
                if(cnt == 0 && sum > 0) cnt = 1;
                idx[i][j] = sink++;
                g[sink].clear();
            }
        }

        FOR(j,1,k)
        {
            if(p[1][j].xx == 0) continue;
            u = src; v = idx[1][j];
            g[u].pb(v);
            g[v].pb(u);
            cap[u][v] = 1;
            cap[v][u] = 0;
        }

        FOR(i,1,n-1)
        {
            FOR(j,1,k)
            {
                FOR(t,1,k)
                {
                    u = idx[i][j]; v = idx[i+1][t];
                    if(p[i][j].xx > p[i+1][t].yy || p[i][j].yy < p[i+1][t].xx) continue;
                    if(p[i][j].xx == 0 || p[i+1][t].xx == 0) continue;
                    g[u].pb(v);
                    g[v].pb(u);
                    cap[u][v] = 1;
                    cap[v][u] = 0;
                    //cout << u << " " << v << NL;
                }
            }
        }

        FOR(j,1,k)
        {
            if(p[n][j].xx == 0) continue;
            v = sink; u = idx[n][j];
            g[u].pb(v);
            g[v].pb(u);
            cap[u][v] = 1;
            cap[v][u] = 0;
        }

        cout << "Case #" << ++caseno << ": " << max_flow(src, sink) << NL;
    }

    return 0;
}




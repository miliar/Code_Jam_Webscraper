
#include<bits/stdc++.h>
using namespace std;
#define D(x)        cout<<#x " = "<<(x)<<endl
#define un(x)       x.erase(unique(x.begin(),x.end()), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define pb          push_back
#define mp          make_pair
#define xx          first
#define yy          second
#define hp          (LL) 999983
#define MAX         100
#define eps         1e-9
#define pi          acos(-1.00)
typedef long long int LL;
typedef pair<int,int> pii;

int n, q;
LL d[MAX+5][MAX+5], edge[MAX+5][MAX+5];
LL enr[MAX+5], spd[MAX+5];
int src, goal;

const LL INF = 1000000000000000LL;
const double dbMax = 1e60;
double answer[MAX+5][MAX+5];

vector< pii > edgeList[MAX+5];

struct state{
    int p, h;
    double t;

    state(int _p, int _h, double _t){
        p = _p;
        h = _h;
        t = _t;
    }
};

bool operator < (const state &u, const state &v){ return u.t > v.t + eps; }
priority_queue<state> PQ;

void dijkstra(int pos, int h)
{
    PQ.push(state(pos, h, 0));
    answer[pos][h] = 0.00;

    while(!PQ.empty()){
        state u = PQ.top(); PQ.pop();

        for(auto x : edgeList[u.p]){
            int v = x.xx;
            int w = x.yy;

            if(d[u.h][v] > enr[u.h]) continue;
            double current = u.t + w / (double) spd[u.h];

            if(current + eps < answer[v][u.h]){
                answer[v][u.h] = current;
                PQ.push(state(v, u.h, current));
            }

            if(current + eps < answer[v][v]){
                answer[v][v] = current;
                PQ.push(state(v, v, current));
            }
        }
    }
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int i, j, k;
    int t, cs;

    sf(t);
    for(cs = 1; cs <= t; cs++)
    {

        sff(n, q);
        for(i = 1; i <= n; i++) scanf("%lld %lld", &enr[i], &spd[i]);

        for(i = 1; i <= n; i++)
            for(j = 1; j <= n; j++)
            {
                scanf("%lld", &edge[i][j]);
                if(edge[i][j] == -1) edge[i][j] = INF;

                if(edge[i][j] != INF)
                    edgeList[i].push_back(pii( j, edge[i][j] ));

            }

        for(i = 1; i <= n; i++)
            for(j = 1; j <= n; j++)
                if(i == j) d[i][j] = 0;
                else d[i][j] = edge[i][j];

        for(k = 1; k <= n; k++)
            for(i = 1; i <= n; i++)
                for(j = 1; j <= n; j++)
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j]);

        /*D("st");
        for(i = 1; i <= n; i++)
        {
            for(j = 1; j <= n; j++)
                printf("%lld ", d[i][j]);
            puts("");
        }
        D("ed");
        return 0;*/

        printf("Case #%d:", cs);
        while(q--)
        {
            sff(src, goal);
            for(i = 1; i <= n; i++)
                for(j = 1; j <= n; j++)
                    answer[i][j] = dbMax;

            dijkstra(src, src);
            double mn = numeric_limits<double>::max();
            for(i = 1; i <= n; i++)
                mn = min(mn, answer[goal][i]);

            printf(" %0.10f", mn);
        }
        puts("");

        for(i = 1; i <= n; i++) edgeList[i].clear();
    }
    return 0;
}






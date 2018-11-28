//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<cstdlib>
#include<cctype>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<fstream>
#include<numeric>
#include<iomanip>
#include<bitset>
#include<list>
#include<stdexcept>
#include<functional>
#include<utility>
#include<ctime>
#include<cassert>
using namespace std;
#define RI(X) scanf("%d", &(X))
#define DRI(X) int (X); scanf("%d", &X)
#define rep(i,a,n) for(int i=(a);i<(int)(n);i++)
#define repd(i,a,b) for(int i=(a);i>=(b);i--)
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define MP make_pair
#define PB push_back
#define AA first
#define BB second
#define OP begin()
#define ED end()
#define SZ size()
typedef long long LL;
typedef pair<int,int> PII;
typedef pair<LL,LL> PLL;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef vector<PII> VPII;
typedef vector<PLL> VPLL;
#define cmin(x,y) x=min(x,y)
#define cmax(x,y) x=max(x,y)
const LL MOD = 1000000007;
const double PI = acos(-1.);
const double eps = 1e-9;
LL modPow(LL a,LL b,LL MOD){
    LL ret=1;for(;b;b>>=1){
        if(b&1)ret=ret*a%MOD;a=a*a%MOD;
    }return ret;
}


#define COST_INF 1e9
template <typename T> class MinCostFlow{
    private:
    struct edge{int to;LL cap;T cost;int rev;};
    
    int V;
    vector<vector<edge> >adj;
    vector<T>pot;
    
    pair<LL,T>dijkstra(int s,int t,LL FLOW_BOUND){
        vector<int>used(V,0);
        vector<T>dist(V,COST_INF);
        vector<PII>path(V,MP(-1,-1));
        priority_queue<pair<T,int> >Q;
        dist[s]=0;
        Q.push(MP(0,s));
        while(!Q.empty()){
            int x=Q.top().BB;
            Q.pop();
            if(used[x])continue;
            used[x]=1;
            for(int i=0;i<adj[x].SZ;i++)if(adj[x][i].cap>0){
                edge e=adj[x][i];
                int y=e.to;
                T d=dist[x]+e.cost+pot[x]-pot[y];
                if(d<dist[y]&&!used[y]){
                    dist[y]=d;
                    path[y]=MP(x,i);
                    Q.push(MP(-d,y));
                }
            }
        }
        for(int i=0;i<V;i++)
            pot[i]+=dist[i];
        if(dist[t]==COST_INF)
            return MP(0,0);
        LL f=FLOW_BOUND;
        T sum=0;
        int x=t;
        while(x!=s){
            int y=path[x].AA;
            int id=path[x].BB;
            sum+=adj[y][id].cost;
            cmin(f,adj[y][id].cap);
            x=y;
        }
        x=t;
        while(x!=s){
            int y=path[x].AA;
            int id=path[x].BB;
            adj[y][id].cap-=f;
            int id2=adj[y][id].rev;
            adj[x][id2].cap+=f;
            x=y;
        }
        return MP(f,f*sum);
    }
    public:
    MinCostFlow(int n){//[0,n)
        V=n;
        adj.resize(V,vector<edge>(0));
        pot.resize(V,0);
    }
    void add_edge(int s,int t,LL f,T c){
        edge e1={t,f,c,(int)adj[t].SZ};
        edge e2={s,0LL,-c,(int)adj[s].SZ};
        adj[s].PB(e1);
        adj[t].PB(e2);
    }
    pair<LL,T>mincostflow(int s,int t,LL FLOW_BOUND=(1LL<<48)){
        pair<LL,T>ans=MP(0LL,0);
        while(FLOW_BOUND>0){
            pair<LL,T>tmp=dijkstra(s,t,FLOW_BOUND);
            if(tmp.AA==0)break;
            ans.AA+=tmp.AA;
            ans.BB+=tmp.BB;
            FLOW_BOUND-=tmp.AA;
        }
        return ans;
    }
};

VI G[1005];
int N,M,C;
int P[1005];
int B[1005];
PII PB[1005];
int s[1005];
int la[1005];
int can(int x){
    rep(i,1,N+1)s[i]=0;
    int free=0;
    int todo = 1;
    int rtn = 0;
    rep(i,0,M){
        int p=PB[i].AA,b=PB[i].BB;
        while(todo<p){
            free+=x-s[todo];
            todo++;
        }
        if(s[p]>=x){
            if(free)free--,rtn++;
            else return -1;
        }else s[p]++;
    }
    return rtn;
}

void solve(){
    RI(N);
    RI(C);
    RI(M);
    rep(i,1,C+1)G[i].clear();
    rep(i,0,M){
        RI(P[i]);
        RI(B[i]);
        PB[i]=MP(P[i],B[i]);
        G[B[i]].PB(P[i]);
    }
    sort(PB,PB+M);
    int max_g = 0;
    rep(i,1,C+1)cmax(max_g,sz(G[i]));
    rep(i,1,C+1){
        sort(all(G[i]));
        reverse(all(G[i]));
    }
    int le=max_g,re=M,ge=-1;
    while(re>=le){
        if(re-le<=1){
            if(~can(le))ge=le;
            else ge=re;
            break;
        }
        int me=(le+re)>>1;
        if(~can(me))re=me;
        else le=me;
    }
    int ans = can(ge);
    printf("%d %d\n",ge,ans);
}

int main(){
    int _T=1;
    scanf("%d",&_T);
    rep(CA,0,_T){
        printf("Case #%d: ",CA+1);
        solve();
    }
    return 0;
}
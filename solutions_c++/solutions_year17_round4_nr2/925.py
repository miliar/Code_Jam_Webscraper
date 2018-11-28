#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

#define CIN_ONLY if(1)
struct cww{cww(){
    CIN_ONLY{
        ios::sync_with_stdio(false);cin.tie(0);
    }
}}star;
#define fin "\n"
#define FOR(i,bg,ed) for(int i=(bg);i<(ed);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define fi first
#define se second
#define pb push_back
#define DEBUG if(0)
#define REC(ret, ...) std::function<ret (__VA_ARGS__)>
template <typename T>inline bool chmin(T &l,T r)
{bool a=l>r;if(a)l=r;return a;}
template <typename T>inline bool chmax(T &l,T r)
{bool a=l<r;if(a)l=r;return a;}
template <typename T>
istream& operator>>(istream &is,vector<T> &v){
    for(auto &it:v)is>>it;
    return is;
    
}
typedef vector<int> V;
struct edge{
    int flow,to,rev;
};
typedef vector<edge> E;
typedef vector<E> Graph;
#define pb push_back
void addedge(Graph&g,int from,int to,int f){
    int x=g[from].size();
    int y=g[to].size();
    g[from].pb(edge{f,to,y});
    g[to].pb(edge{0,from,x});
}

vector<int> bfs(Graph& G,int s){
    int N = G.size();
    queue<int> que;
    vector<int> dist(N,-1);
    dist[s] = 0;
    que.push(s);
    for(;!que.empty();que.pop()){
        auto v=que.front();
        for(auto& e : G[v])
            if(e.flow>0&&dist[e.to]==-1){
                dist[e.to] = dist[v] + 1;
                que.push(e.to);
        }
    }
    return dist;
}

int maxflow(Graph& G,int s,int t){
    int res=0;
    int N = G.size();
    while(true){
        auto dist = bfs(G,s);
        if(dist[t] < 0)break;
        vector<unsigned> iter(N,0);
        std::function<int(int,int)> dfs=[&](int v,int f){
            if(v==s)return f;
            for(auto &i = iter[v]; i < G[v].size(); i++){
                edge &e = G[v][i];
                edge &re = G[e.to][e.rev];
                if(re.flow>0 && dist[v] >dist[e.to]){
                    int d=dfs(e.to,min(f,re.flow));
                    if(d>0){e.flow+=d;re.flow-=d;return d;}
                }
            }
            return 0;
        };
        int f;
        while((f=dfs(t,114514))> 0)res+=f;
    }
    return res;
}

void solve(){
    int N,C,M;
    cin>>N>>C>>M;
    vector<V> c(N);
    REP(i,M){
        int a,b;
        cin>>a>>b;
        a--;b--;
        c[b].pb(a);
    }
    if(C>2)return;
    Graph g(c[0].size()+c[1].size()+2);
    int n=c[0].size();
    int m=c[1].size();
    int S=n+m;
    int T=S+1;
    REP(i,n)addedge(g,S,i,1);
    REP(i,m)addedge(g,n+i,T,1);
    REP(i,n)REP(j,m)if(c[0][i]!=c[1][j])addedge(g,i,n+j,1);
    int res=maxflow(g,S,T);
    int cost=0;
    vector<V> d(2);
    REP(i,g[S].size())if(g[S][i].flow==1)d[0].pb(i);
    REP(i,g[T].size())if(g[T][i].flow==0)d[1].pb(i);
    if(d[0].size()>0&&d[1].size()>0){
        if(c[0][d[0][0]]>0){
            res+=max(d[0].size(),d[1].size());
            cost+=min(d[0].size(),d[1].size());
        }
        else{
            res+=d[0].size()+d[1].size();
        }
    }
    else 
        res+=d[0].size()+d[1].size();
    cout<<res<<" "<<cost<<endl;
}
int main(){
    int T;
    cin>>T;
    FOR(i,1,T+1){
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}

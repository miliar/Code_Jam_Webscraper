#include <bits/stdc++.h>
using namespace std;

#define PB push_back
#define CL(A,I) (memset(A,I,sizeof(A)))

#define FOR(i, m, n) for (int i=(int)m; i < (int)n; i++)
#define F(n) FOR(i,0,n)
#define FF(n) FOR(j,0,n)

#define D(X) cout<<"  "<<#X": "<<X<<endl;

using ll=long long;
using ii=pair<ll,ll>;
using vi=vector<ll>;
using vii=vector<ii>;

#define aa first
#define bb second

#define EPS (1e-9)
#define EQ(A,B) (A+EPS>B&&A-EPS<B)


template <int MAXN>
struct BipartiteGraph {
    vector<int> g[MAXN],U,V;
    int matching[MAXN];
    int d[MAXN];

    BipartiteGraph(){
        memset(d,0,sizeof d);
    }

   void au(int u){
        if(!d[u])d[u]=1,U.PB(u);
    }
   void av(int v){
        if(!d[v])d[v]=1,V.PB(v);
    }


    void addEdge(int u, int v){
        if(!d[u])d[u]=1,U.PB(u);
        if(!d[v])d[v]=1,V.PB(v);
        g[u].PB(v);
        g[v].PB(u);
    }

    int hopcroftkarp() {
        memset(matching,-1, sizeof matching);
        int cnt=0;
        while(bfs())
        for(int u : U)
            if(matching[u]==-1 && d[u] != -1)
                cnt+=dfs(u);
        return cnt;
    }

    bool bfs() {
        memset(d,-1,sizeof d);
        queue<int> q;
        for(int u : U)
            if(matching[u]==-1){
                d[u]=0;
                q.push(u);
            }
        while(q.size()) {
            int node = q.front();
            q.pop();
            if(node == -1)
                return true;
            for(int neigh : g[node]) {
                if(d[neigh] != -1) continue;
                d[neigh] = d[node] + 1;

                if(matching[neigh] != -1)
                    d[matching[neigh]] = d[neigh] + 1;
                q.push(matching[neigh]);
            }
        }
        return false;
    }

    bool dfs(int node) {
        if(node==-1)return true;
        for(int neigh : g[node]) {
            if(d[neigh]!=d[node]+1) continue;
            if(dfs(matching[neigh])) {
                d[neigh] = d[node] = -1;
                matching[neigh] = node;
                matching[node] = neigh;
                return true;
            }
        }
        return false;
    }
};


const int MX=3007;

int n,c,m;
vector<int> cus[2];
int ccone[2];

void process(){
    cin>>n>>c>>m;

    BipartiteGraph<MX> bg;

    F(2){
        cus[i].clear();
        ccone[i]=0;
    }

    int rest0=0,rest1=0;

    F(m){
        int p,ci;
        cin>>p>>ci;ci--;
        cus[ci].PB(p);
        if(ci==0)rest0++;
        else rest1++;
    }


    // F(cus[0].size())bg.au(cus[0][i]);
    // F(cus[1].size())bg.av(cus[1][i]+2000);

    F(cus[0].size())
    FF(cus[1].size()){
        if(cus[0][i]!=cus[1][j])
            bg.addEdge(i,2000+j);
    }


    int ans=0,anns=0;
    int mm=bg.hopcroftkarp();
    ans+=mm;
    rest0-=mm;
    rest1-=mm;

    F(cus[0].size())if(bg.matching[i]==-1&&cus[0][i]==1)ans++,rest0--;
    F(cus[1].size())if(bg.matching[2000+i]==-1&&cus[1][i]==1)ans++,rest1--;

    int dd=min(rest0,rest1);
    ans+=rest0+rest1-dd;
    anns+=dd;

    cout<<ans<<' '<<anns<<endl;
}

int main() {
    int t;cin>>t;
    F(t){
        cout<<"Case #"<<i+1<<": ";
        process();
    }
    return 0;
}
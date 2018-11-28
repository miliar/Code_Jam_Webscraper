#include <bits/stdc++.h>
using namespace std;
//make_tuple emplace_back next_permutation push_back make_pair second first setprecision

#if MYDEBUG
#include "lib/cp_debug.h"
#else
#define DBG(...) ;
#endif

using LL = long long;
constexpr LL LINF=334ll<<53;
constexpr int INF=15<<26;
constexpr LL  MOD=1E9+7;

struct Edge{
    int from,to;
    Edge(int from,int to)
        : from(from),to(to){};
    Edge(){Edge(0,0);}
};
typedef vector<vector<Edge>> Graph;
struct StronglyConnectedComponents{
    vector<int> scrank,vis,po;
    Graph graph,rgraph;
    vector<set<int>>st;
    StronglyConnectedComponents(int n):scrank(n),vis(n),graph(n),rgraph(n){}
    private:
    void dfs(int a,Graph &g){
        vis[a]=1;
        for(int i=0; i<g[a].size(); ++i){
            if(!vis[g[a][i].to]) dfs(g[a][i].to,g);
        }
        po.push_back(a);
    }
    void rdfs(int a, int k, Graph &rg){
        scrank[a]=k;
        vis[a]=1;
        for(int i=0; i<rg[a].size(); ++i){
            if(!vis[rg[a][i].to]) rdfs(rg[a][i].to,k,rg);
        }
    }
    public:
    void calc(){
        for(int i=0; i<graph.size(); ++i){
            if(!vis[i]) dfs(i,graph);
        }
        fill(vis.begin(),vis.end(),0);
        int c=0;
        for(int i=rgraph.size()-1; i>=0; --i){
            if(!vis[po[i]]) rdfs(po[i],c++,rgraph);
        }
    }
    void add_edge(int a, int b){
        if(st[a].count(b))return;
        st[a].insert(b);
        graph[a].emplace_back(a,b);
        rgraph[b].emplace_back(b,a);
    }
};

struct Problem{
    int r,c;
    vector<vector<char>> b;
    vector<vector<int>> g;
    map<pair<int,int>,int>m;
    vector<pair<int,int>> gen;
    StronglyConnectedComponents scc;
    vector<vector<vector<int>>> reach;
    Problem(int r,int c):r(r),c(c),b (r,vector<char>(c)),g(r,vector<int>(c)),scc(0),reach (r,vector<vector<int>>(c,vector<int>(4,-1))){};

    void beam(int generator,int sa,int sb){
        int m1[4]={1,0,3,2}; /* / */
        int m2[4]={3,2,1,0}; /* \ */
        int dx[4]={0,-1,0,1}, dy[4]={1,0,-1,0};
        for(int i=0; i<4; ++i){
            int x=sa,y=sb,dir=i;
            while(1){
                x+=dx[dir];
                y+=dy[dir];
                DBG(i,x,y)
                if(x<0 or r<=x or y<0 or c<=y)break;
                if(b[x][y]=='|' or b[x][y]=='-'){
                    scc.add_edge(generator*2+(i%2),generator*2+((i+1)%2));
                    break;
                }else if(b[x][y]=='/'){
                    dir=m1[dir];
                }else if(b[x][y]=='\\'){
                    dir=m2[dir];
                }else if(b[x][y]=='.'){
                    reach[x][y][dir]=generator*2+(i%2);
                }else{
                    break;
                }
            }
        }
    }
    void fail(){cout <<"IMPOSSIBLE" <<"\n";}
    void solve(){
        for(int i=0; i<r; ++i){
            for(int j=0; j<c; ++j){
                cin >> b[i][j];
                if(b[i][j]=='|' or b[i][j]=='-'){
                    g[i][j]=1;
                    gen.emplace_back(i,j);
                    m[{i,j}]=gen.size()-1;
                }
            }
        }
        scc=StronglyConnectedComponents((int)gen.size()*2);
        scc.st.resize((int)gen.size()*2,set<int>());
        for(int i=0; i<(int)gen.size(); ++i){
            beam(i,gen[i].first,gen[i].second);
        }
        for(int i=0; i<r; ++i){
            for(int j=0; j<c; ++j){
                if(b[i][j]=='.'){
                    vector<int> tmp;
                    for(int k=0; k<4; ++k){
                        if(reach[i][j][k]!=-1 and reach[i][j][(k+2)%4]==-1){
                            tmp.push_back(reach[i][j][k]);
                        }
                    }
                    if((int)tmp.size()==0){
                        fail();return;
                    }else if((int)tmp.size()==1){
                        scc.add_edge(tmp[0]^1,tmp[0]);
                    }else if((int)tmp.size()==2){
                        scc.add_edge(tmp[0]^1,tmp[1]);
                        scc.add_edge(tmp[1]^1,tmp[0]);
                    }
                }
            }
        }
        scc.calc();
        for(int i=0; i<(int)gen.size(); ++i){
            DBG(i,scc.scrank[2*i],scc.scrank[2*i+1])
            if(scc.scrank[2*i]==scc.scrank[2*i+1]){
            fail();return;
            }
        }
        for(int i=0; i<(int)gen.size(); ++i){
            if(scc.scrank[2*i]>scc.scrank[2*i+1]){
                b[gen[i].first][gen[i].second]='-';
            }else{
                b[gen[i].first][gen[i].second]='|';
            }
        }
        cout << "POSSIBLE" <<"\n";
        for(int i=0; i<r; ++i){
            for(int j=0; j<c; ++j){
                cout << b[i][j];
            }
            cout <<"\n";
        }

    }
};

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int testcases;
    cin >> testcases;
    for(int i=1; i<=testcases; ++i){
        cout << "Case #" << i << ": ";
        int r,c;
        cin >> r >> c;
        Problem p(r,c);
        p.solve();
    }

    return 0;
}


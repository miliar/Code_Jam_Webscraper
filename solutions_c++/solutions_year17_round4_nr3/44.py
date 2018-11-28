#include<bits/stdc++.h>
using namespace std;

#define int long long

#define rep(i,n) for(int i=0;i<(n);i++)
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define fi first
#define se second
typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;

template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

namespace SCC{
    void visit(const vector<vector<int>>&G,vector<int>&vs,vector<int>&used,int v){
        used[v]=true;
        for(auto u:G[v]){
            if(!used[u])visit(G,vs,used,u);
        }
        vs.push_back(v);
    }

    void visit2(const vector<vector<int>>&T,vector<int>&used,vector<int>&comp,vector<int>&vec,int k,int v){
        comp[v]=k;
        used[v]=true;
        vec.push_back(v);

        for(auto u:T[v]){
            if(!used[u])visit2(T,used,comp,vec,k,u);
        }
    }

    void decompose(const vector<vector<int>>&G,vector<vector<int>>&H,vector<int>&comp){
        vector<vector<int>>T(G.size());
        for(int i=0;i<G.size();i++){
            for(auto v:G[i]){
                T[v].push_back(i);
            }
        }
        comp.resize(G.size());

        vector<int>vs(G.size());
        vector<int>used(G.size());
        for(int i=0;i<G.size();i++){
            if(!used[i])visit(G,vs,used,i);
        }
        reverse(vs.begin(),vs.end());
        fill(used.begin(),used.end(),0);

        int K=0;
        vector<vector<int>>S;
        for(auto v:vs){
            if(!used[v]){
                S.push_back(vector<int>());
                visit2(T,used,comp,S.back(),K++,v);
            }
        }

        H.resize(K);
        fill(used.begin(),used.end(),0);
        for(int i=0;i<K;i++){
            for(auto v:S[i]){
                for(auto u:G[v]){
                    if(used[comp[u]]||comp[v]==comp[u])continue;
                    used[comp[u]]=true;
                    H[comp[v]].push_back(comp[u]);
                }
            }
            for(auto v:H[i])used[v]=false;
        }

    }
}

int dy[]={0,-1,0,1};
int dx[]={1,0,-1,0};

int H,W;
char fld[55][55];
vpint to[55][55][2];
bool ng[55][55][2];

vint from[55][55];

void solve(){
    cin>>H>>W;
    rep(i,H)cin>>fld[i];

    rep(i,H)rep(j,W)rep(k,2)to[i][j][k].clear();
    rep(i,H)rep(j,W)from[i][j].clear();
    memset(ng,0,sizeof(ng));

    rep(i,H){
        rep(j,W){
            if(fld[i][j]!='-'&&fld[i][j]!='|')continue;
            rep(s,4){
                int y=i,x=j,d=s;
                while(true){
                    y+=dy[d];
                    x+=dx[d];
                    if(y<0||y>=H||x<0||x>=W)break;
                    if(fld[y][x]=='#')break;
                    if(fld[y][x]=='-'||fld[y][x]=='|'){
                        ng[i][j][s&1]=1;
                        break;
                    }
                    if(fld[y][x]=='/'){
                        d^=1;
                    }
                    if(fld[y][x]=='\\'){
                        d^=3;
                    }
                    if(fld[y][x]=='.'){
                        to[i][j][s&1].pb({y,x});
                    }
                }
            }
        }
    }

    rep(i,H)rep(j,W)if(ng[i][j][0]&&ng[i][j][1]){
        cout<<"IMPOSSIBLE"<<endl;
        return;
    }

    vpint latte;
    rep(i,H)rep(j,W){
        if(fld[i][j]!='-'&&fld[i][j]!='|')continue;
        latte.pb({i,j});
    }

    sort(all(latte));

    vector<vint>G(latte.size()*2);
    rep(i,H)rep(j,W){
        if(fld[i][j]!='-'&&fld[i][j]!='|')continue;
        int id=lower_bound(all(latte),pint(i,j))-latte.begin();
        if(ng[i][j][0])G[id*2].pb(id*2+1);
        if(ng[i][j][1])G[id*2+1].pb(id*2);

        if(!ng[i][j][0])for(auto &p:to[i][j][0]){
            from[p.fi][p.se].pb(id*2);
        }
        if(!ng[i][j][1])for(auto &p:to[i][j][1]){
            from[p.fi][p.se].pb(id*2+1);
        }
    }

    rep(i,H)rep(j,W){
        if(fld[i][j]!='.')continue;
        if(from[i][j].size()==0){
            cout<<"IMPOSSIBLE"<<endl;
            return;
        }
        if(from[i][j].size()==1){
            G[from[i][j][0]^1].pb(from[i][j][0]);
        }
        if(from[i][j].size()==2){
            G[from[i][j][0]^1].pb(from[i][j][1]);
            G[from[i][j][1]^1].pb(from[i][j][0]);
        }
        assert(from[i][j].size()<=2);
    }

    vector<vint>malta;
    vint comp;
    SCC::decompose(G,malta,comp);
    rep(i,latte.size()){
        if(comp[i*2]==comp[i*2+1]){
            cout<<"IMPOSSIBLE"<<endl;
            return;
        }
        if(comp[i*2]>comp[i*2+1]){
            fld[latte[i].fi][latte[i].se]='-';
        }
        else{
            fld[latte[i].fi][latte[i].se]='|';
        }
    }
    cout<<"POSSIBLE"<<endl;
    rep(i,H)cout<<fld[i]<<endl;

}

signed main(){
    int T;cin>>T;
    for(int i=1;i<=T;i++){
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

#define int long long

typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;
#define rep(i,n) for(int i=0;i<(n);i++)
#define reps(i,f,n) for(int i=(f);i<(n);i++)
#define all(v) (v).begin(),(v).end()
#define each(it,v) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)
#define pb push_back
#define fi first
#define se second
template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

struct bipartite_matching{
    static const int MAX_V=444;
    vector<int>G[MAX_V];
    int match[MAX_V];
    bool used[MAX_V];

    void add_edge(int u,int v){
        G[u].push_back(v);
        G[v].push_back(u);
    }

    bool dfs(int v){
        used[v]=true;
        for(int i=0;i<G[v].size();i++){
            int u=G[v][i],w=match[u];
            if(w<0||!used[w]&&dfs(w)){
                match[v]=u;
                match[u]=v;
                return true;
            }
        }
        return false;
    }

    int matching(){
        int res=0;
        memset(match,-1,sizeof(match));
        for(int v=0;v<MAX_V;v++){
            if(match[v]<0){
                memset(used,0,sizeof(used));
                if(dfs(v))res++;
            }
        }
        return res;
    }
};

int N,M;

void solve(){
    cin>>N>>M;

    bool luz[111][111]={};
    bool izr[111][111]={};
    bool ex1[222]={},ex2[222]={};
    char fld[111][111];

    rep(i,N)rep(j,N)fld[i][j]='.';

    rep(i,M){
        char c;
        int y,x;
        cin>>c>>y>>x;
        y--;x--;
        fld[y][x]=c;
        assert(c=='o'||c=='x'||c=='+');
        assert(fld[y][x]=='o'||fld[y][x]=='x'||fld[y][x]=='+'||fld[y][x]=='.');
        if(c=='x'||c=='o')luz[y][x]=true;
        if(c=='+'||c=='o'){
            izr[y][x]=true;
            ex1[y+x]=true;
            ex2[y-x+N-1]=true;
        }
    }

    int cur=0;
    rep(j,N){
        bool ok=true;
        rep(i,N)if(luz[i][j])ok=false;
        if(!ok)continue;
        while(accumulate(luz[cur],luz[cur]+N,0ll))cur++;
        luz[cur][j]=true;
        cur++;
    }

    bipartite_matching bm;


    rep(i,N){
        rep(j,N){
            int v=i+j;
            int u=i-j+N-1;
            if(ex1[v])continue;
            if(ex2[u])continue;
            bm.add_edge(v,u+2*N-1);
        }
    }

    bm.matching();

    rep(i,2*N-1){
        int tmp=bm.match[i];
        if(tmp==-1)continue;

        tmp-=2*N-1;
        if(tmp<0||tmp>=2*N-1)assert(0);

        int y=(i+tmp-N+1)/2;
        int x=i-y;
        izr[y][x]=true;
    }


    int sum=0;
    vector<char>C;
    vint Y,X;


    rep(i,N)rep(j,N){
        sum+=luz[i][j]+izr[i][j];

        char c;
        if(luz[i][j]&&izr[i][j])c='o';
        else if(luz[i][j])c='x';
        else if(izr[i][j])c='+';
        else c='.';

        if(fld[i][j]==c)continue;
        C.pb(c);
        Y.pb(i);
        X.pb(j);
        fld[i][j]=c;
    }

    cout<<sum<<" "<<C.size()<<"\n";
    rep(i,C.size()){
        cout<<C[i]<<" "<<Y[i]+1<<" "<<X[i]+1<<"\n";
    }

}

signed main(){
    cin.tie(0);ios_base::sync_with_stdio(0);
    int T;
    cin>>T;
    rep(i,T){
        cout<<"Case #"<<i+1<<": ";
        solve();
    }
    return 0;
}

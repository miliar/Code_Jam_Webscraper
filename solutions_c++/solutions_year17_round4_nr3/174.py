#include <bits/stdc++.h>
#define SZ(X) ((int)(X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < (N); ++I)
#define REPP(I, A, B) for (int I = (A); I < (B); ++I)
#define RI(X) scanf("%d", &(X))
#define RII(X, Y) scanf("%d%d", &(X), &(Y))
#define RIII(X, Y, Z) scanf("%d%d%d", &(X), &(Y), &(Z))
#define DRI(X) int (X); scanf("%d", &X)
#define DRII(X, Y) int X, Y; scanf("%d%d", &X, &Y)
#define DRIII(X, Y, Z) int X, Y, Z; scanf("%d%d%d", &X, &Y, &Z)
#define RS(X) scanf("%s", (X))
#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)
#define MP make_pair
#define PB push_back
#define MS0(X) memset((X), 0, sizeof((X)))
#define MS1(X) memset((X), -1, sizeof((X)))
#define LEN(X) strlen(X)
#define PII pair<int,int>
#define VI vector<int>
#define VPII vector<pair<int,int> >
#define PLL pair<long long,long long>
#define VPLL vector<pair<long long,long long> >
#define F first
#define S second
typedef long long LL;
using namespace std;
const int SIZE = 2555;
char s[55][55];
VI e[SIZE];
int _id[55][55][4];
int grid[55][55][2];
const int LEFT = 0;
const int UP = 1;
const int RIGHT = 2;
const int DOWN = 3;
int dx[4]={0,-1,0,1};
int dy[4]={-1,0,1,0};
int R,C;
bool Out(int x,int y){
    return x<0||y<0||x>=R||y>=C;
}
struct Union_Find{
    int d[SIZE],num[SIZE],v[SIZE],from[SIZE];
    void init(int n){
        REP(i,n)d[i]=i,num[i]=1,v[i]=0,from[i]=0;
    }
    int find(int x){
        return (x!=d[x])?(d[x]=find(d[x])):x;
    }
    bool uu(int x,int y){
        x=find(x);
        y=find(y);
        if(x==y)return 0;
        if(num[x]>num[y])swap(x,y);
        v[y]+=v[x];
        from[y]+=from[x];
        num[y]+=num[x];
        d[x]=y;
        return 1;
    }
    int get(int x){
        x=find(x);
        if(v[x]!=1)return -1;
        return from[x];
    }
}U;
struct SCC{
    int n,used[SIZE],order[SIZE],gg[SIZE];
    vector<int>e[SIZE],ae[SIZE],ge[SIZE],emp;
    int id,gn;
    void init(int _n){
        n=_n;
        memset(used,0,sizeof(int)*n);
        REP(i,n){
            e[i]=ae[i]=ge[i]=emp;
        }
    }
    void add_edge(int x,int y){
        e[x].PB(y);
        ae[y].PB(x);
    }
    void dfs1(int x){
        if(used[x]==1)return;
        used[x]=1;
        REP(i,SZ(e[x])){
            int y=e[x][i];
            dfs1(y);
        }
        order[--id]=x;
    }
    void dfs2(int x){
        if(used[x]==2)return;
        gg[x]=gn;
        used[x]=2;
        REP(i,SZ(ae[x])){
            int y=ae[x][i];
            if(used[y]==2){
                //if(gg[y]!=gg[x])ge[gg[y]].PB(gg[x]);
            }
            else dfs2(y);
        }
    }
    bool valid(){
        gn=0;
        id=n;
        REP(i,n)
            dfs1(i);
        REP(i,n){
            if(used[order[i]]!=2){
                dfs2(order[i]);
                gn++;
            }
        }
        REP(i,n){
            if(gg[i]==gg[i^1])return 0;
        }
        return 1;
    }
}scc;
int node_N;
bool solve(){
    scc.init(node_N);
    REP(i,R)REP(j,C){
        if(s[i][j]=='#')continue;
        if(s[i][j]!='.'){
            int vv[2];
            REP(k,2)vv[k]=U.get(grid[i][j][k]);
            if(vv[0]==-1&&vv[1]==-1)return 0;
            if(vv[0]==-1)scc.add_edge(vv[1]^1,vv[1]);
            else if(vv[1]==-1)scc.add_edge(vv[0]^1,vv[0]);
        }
        if(s[i][j]=='-'){
            scc.add_edge(_id[i][j][UP],_id[i][j][LEFT]);
        }
        else if(s[i][j]=='|'){
            scc.add_edge(_id[i][j][LEFT],_id[i][j][UP]);
        }
        else if(s[i][j]=='.'){
            int vv[2];
            REP(k,2)vv[k]=U.get(grid[i][j][k]);
            if(vv[0]==-1&&vv[1]==-1)return 0;
            if(vv[0]==-1){
                scc.add_edge(vv[1]^1,vv[1]);
            }
            else if(vv[1]==-1){
                scc.add_edge(vv[0]^1,vv[0]);
            }
            else{
                scc.add_edge(vv[0]^1,vv[1]);
                scc.add_edge(vv[1]^1,vv[0]);
            }
        }
    }
    return scc.valid();
}
int main(){
    CASET{
        RII(R,C);
        MS1(_id);
        {
            int tmp=0;
            REP(i,R){
                RS(s[i]);
                REP(j,C){
                    if(s[i][j]=='/'){
                        _id[i][j][LEFT]=_id[i][j][UP]=tmp;
                        grid[i][j][0]=tmp++;
                        _id[i][j][RIGHT]=_id[i][j][DOWN]=tmp;
                        grid[i][j][1]=tmp++;
                    }
                    else if(s[i][j]=='\\'){
                        _id[i][j][LEFT]=_id[i][j][DOWN]=tmp;
                        grid[i][j][0]=tmp++;
                        _id[i][j][RIGHT]=_id[i][j][UP]=tmp;
                        grid[i][j][1]=tmp++;
                    }
                    else if(s[i][j]!='#'){
                        _id[i][j][LEFT]=_id[i][j][RIGHT]=tmp;
                        grid[i][j][0]=tmp++;
                        _id[i][j][UP]=_id[i][j][DOWN]=tmp;
                        grid[i][j][1]=tmp++;
                        if(s[i][j]!='.')s[i][j]='*';
                    }
                }
            }
            node_N=tmp;
        }
        U.init(node_N);
        REP(i,R)REP(j,C){
            if(s[i][j]=='*'){
                REP(k,2){
                    U.v[grid[i][j][k]]=1;
                    U.from[grid[i][j][k]]=grid[i][j][k];
                }
            }
        }
        REP(i,R)REP(j,C){
            if(s[i][j]=='#')continue;
            REP(k,4){
                int nx=i+dx[k];
                int ny=j+dy[k];
                if(Out(nx,ny))continue;
                if(s[nx][ny]=='#')continue;
                U.uu(_id[i][j][k],_id[nx][ny][k^2]);
            }
        }
        printf("Case #%d: ",case_n++);
        if(!solve())puts("IMPOSSIBLE");
        else{
            REP(i,R)REP(j,C){
                if(s[i][j]=='*'){
                    s[i][j]='|';
                    if(!solve())s[i][j]='-';
                }
            }
            puts("POSSIBLE");
            REP(i,R)puts(s[i]);
        }
    }
    return 0;
}

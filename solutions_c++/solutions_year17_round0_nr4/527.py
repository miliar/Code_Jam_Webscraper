#include <bits/stdc++.h>
using namespace std;
#define PB push_back
#define ZERO (1e-10)
#define INF (1<<29)
#define CL(A,I) (memset(A,I,sizeof(A)))
#define DEB printf("DEB!\n");
#define D(X) cout<<"  "<<#X": "<<X<<endl;
#define EQ(A,B) (A+ZERO>B&&A-ZERO<B)
typedef long long ll;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define IN(n) int n;scanf("%d",&n);
#define FOR(i, m, n) for (int i(m); i < n; i++)
#define F(n) FOR(i,0,n)
#define FF(n) FOR(j,0,n)
#define FT(m, n) FOR(k, m, n)
#define aa first
#define bb second
void ga(int N,int *A){F(N)scanf("%d",A+i);}
#define SZ 5005
#define ME (1<<21)
struct Dinic{
    int n,m,h[SZ],l[SZ],s,t,w[SZ];
    struct eg{
        int v,c,f,x;
    }e[ME];
    bool bfs(){
        static int q[SZ];
        F(n)l[i]=-1;/*CL(l,-1)*/
        int B(l[s]=0),E(1);
        q[0]=s;
        while(B<E)for(int k(q[B++]),i(h[k]);~i;i=e[i].x)
            if(e[i].f<e[i].c&&!~l[e[i].v])
                l[e[i].v]=l[k]+1,q[E++]=e[i].v;
        return ~l[t];
    }
    int dfs(int u,int f){
        if(u==t)return f;
        int mf;
        for(int i(w[u]);~i;i=e[i].x)
            if(e[i].f<e[i].c&&l[u]+1==l[e[i].v])
                if((mf=dfs(e[i].v,min(f,e[i].c-e[i].f)))>0)
                    return e[i].f+=mf,e[i^1].f-=mf,mf;
        return 0;
    }
    void ini(int N,int f,int d){n=N;s=f;t=d;m=0;F(n)h[i]=-1;}
    void ade(int u,int v,int c=1,int rc=0){
        e[m]=eg{v,c,0,h[u]};
        h[u]=m++;
        e[m]=eg{u,rc,0,h[v]};
        h[v]=m++;
    }
    int mf(){
        int a(0),d;
        while(bfs()){
            memcpy(w,h,sizeof(int)*n);
            do a+=d=dfs(s,INF); while(d);
        }
        return a;
    }
    void go(vii&H,int T){FF(T)for(int i(w[j]);~i;i=e[i].x)if(e[i].f)H.PB({j,e[i].v});}
}X,P;
#define MX (666)
#define TS (666)
#define DA(X,Y) (X-Y+100)
#define DB(X,Y) (X+Y+200)
#define TR(C) ((C)==3?111:(C)&1?43:(C)?120:46)
char c;
int N,M,r[MX],R[MX],d[MX],D[MX],t,a,b,g[MX][MX],G[MX][MX],S;
void sig(){
    vii H,U;
    X.go(H,N),P.go(U,200);
    for(auto&h:H)G[h.aa][h.bb-N]|=2;
    for(auto&h:U)F(N)FF(N)if(DA(i,j)==h.aa&&DB(i,j)==h.bb)G[i][j]|=1;//O(n^3) - fail :P   
    F(N)FF(N)S+=!!G[i][j];
}
int main(void){
    IN(_)F(_){
        scanf("%d%d",&N,&M),X.ini(TS,TS-1,TS-2),P.ini(TS,TS-1,TS-2);
        CL(r,0),CL(R,0),CL(d,0),CL(D,t=0),CL(g,0),CL(G,S=0);
        F(M){
            scanf(" %c%d%d",&c,&a,&b),--a,--b;
            if(c==43||c==111)++d[DA(a,b)],++D[DB(a,b)],g[a][b]|=1,++t;
            if(c==120||c==111)++r[a],++R[b],g[a][b]|=2,++t;
        }
        F(MX)assert(r[i]<2&&R[i]<2&&d[i]<2&&D[i]<2);
//        F(MX)if(!(r[i]<2&&R[i]<2&&d[i]<2&&D[i]<2)){
//            D(N)D(M)
//            printf("Case #%d: %d %d\n",i+1,0,0);
//            D("REAL:");
//            F(N){
//                FF(N)putchar(TR(g[i][j]|G[i][j]));
//                puts("");
//            }
//            assert(0);
//            goto GOW;
//        }
        F(N)FF(N)X.ade(i,N+j);
        F(N)FF(N)P.ade(DA(i,j),DB(i,j));
        F(N){
            if(!r[i])X.ade(TS-1,i);
            if(!R[i])X.ade(N+i,TS-2);
        }
        F(200)if(!d[i])P.ade(TS-1,i);
        FT(200,400)if(!D[k])P.ade(k,TS-2);
        t+=X.mf(),t+=P.mf();
        sig();
        printf("Case #%d: %d %d\n",i+1,t,S);
        F(N)FF(N)if(G[i][j])printf("%c %d %d\n",TR(g[i][j]|G[i][j]),i+1,j+1);
//        GOW:c=1;
    //        D("REAL:");
    //        F(N){
    //            FF(N)putchar(TR(g[i][j]|G[i][j]));
    //            puts("");
    //        }
    }
    return 0;
}

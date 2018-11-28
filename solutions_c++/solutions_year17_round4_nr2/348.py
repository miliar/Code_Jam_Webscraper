#include <bits/stdc++.h>
using namespace std;
#define PB push_back
#define ZERO (1e-10)
#define INF int(1e9+1)
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
#define SZ (4000)
#define MX SZ
#define ME (1<<20)
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
}G;
int N,M,C,P[MX],B[MX],S,I[MX];
void st(int t){
    G.ini(C+N+2,C+N,C+N+1);
    F(M)G.ade(B[i]-1,P[i]-1+C,1);
    F(N-1)G.ade(C+i+1,C+i,INF);
    F(C)G.ade(C+N,i,t);
    F(N)G.ade(C+i,C+N+1,t);
}
bool ok(ll t){
    st(t);
    return G.mf()==M;
}
ll bs(ll B=0,ll E=INF){
    ll M;
    while(B<E)
        if(ok(M=(B+E)>>1))E=M;
        else B=M+1;
    return B;
}
int main(void){
    IN(_)F(_){
        scanf("%d%d%d",&N,&C,&M),CL(I,S=0);
        F(M)scanf("%d%d",P+i,B+i);
        int a=bs(0,1001);
        F(M)++I[P[i]-1];
        F(N)S+=max(0,I[i]-a);
        printf("Case #%d: %d %d\n",i+1,a,S);
    }
    return 0;
}

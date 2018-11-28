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
#define MX (55)
int N,P,Q[MX][MX],R[MX],I[MX],S;
bool ok(int r,int H,int t){
    return t*r*.9-ZERO<H&&t*r*1.1+ZERO>H;
}
void go(){
    FT(1,1e6+666){
        bool x=1;
        F(N){
            while(I[i]<P&&k*.9*R[i]-ZERO>Q[i][I[i]])++I[i];
            if(I[i]==P)return;
            x&=ok(R[i],Q[i][I[i]],k);
        }
        if(x){
            ++S,--k;
            F(N)++I[i];
        }
    }
}
int main(void){
    IN(_)F(_){
        scanf("%d%d",&N,&P),ga(N,R),CL(I,S=0);
        F(N)FF(P)scanf("%d",Q[i]+j);
        F(N)sort(Q[i],Q[i]+P);
        go();
        printf("Case #%d: %d\n",i+1,S);
    }
    return 0;
}

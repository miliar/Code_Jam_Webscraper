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
#define MX (1000009)
#define GG(A,B) {printf("Case #%d: %lld %lld\n",i+1,A,B);continue;}
ll N,K,a,S;
map<ll,ll> T; 
int main(void){
    IN(_)F(_){
        scanf("%lld%lld",&N,&K),T.clear(),T[-N]=1;
        while(K){
            a=-T.begin()->aa,S=T.begin()->bb;
            if(S>=K)break;
            T.erase(-a),K-=S;
            if(a>2)T[(1-a)/2]+=S;
            if(a>1)T[-a/2]+=S;
        }
        GG(a/2,(a-1)/2)
    }
    return 0;
}

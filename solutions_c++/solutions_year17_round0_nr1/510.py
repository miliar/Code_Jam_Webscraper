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
#define MX (10000)
#define IV(C) (C^45?45:43)
char s[MX];
int L,K,S;
bool ok(){F(L)if(s[i]^43)return 0;return 1;}
int main(void){
    IN(_)F(_){
        scanf("%s%d",s,&K),L=strlen(s),S=0;
        F(L-K+1)if(s[i]^43){++S;FF(K)s[i+j]=IV(s[i+j]);}
        if(ok())printf("Case #%d: %d\n",i+1,S);
        else printf("Case #%d: IMPOSSIBLE\n",i+1);
    }
    return 0;
}

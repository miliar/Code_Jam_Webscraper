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
int N,S,P,a,c,A[128],C[5],J[5];
int main(void){
    IN(_)F(_){
        scanf("%d%d",&N,&P),CL(C,S=c=0),ga(N,A);
        F(N)++C[A[i]%=P];
        if(P==2)S=*C+(C[1]/2)+C[1]%2;
        else if(P==3){
            S=*C;
            a=min(C[1],C[2]),S+=a,C[1]-=a,C[2]-=a;
            S+=C[1]/3,C[1]%=3;
            S+=C[2]/3,C[2]%=3;
            if(C[1]||C[2])++S;
        }else {
            S=*C;
            a=min(C[1],C[3]),S+=a,C[1]-=a,C[3]-=a;
            S+=C[2]/2,C[2]&=1;
            if(C[2]&&C[1]>1)C[1]-=2,C[2]=0,++S;
            if(C[2]&&C[3]>1)C[3]-=2,C[2]=0,++S;
            S+=C[1]/4,C[1]&=3;
            S+=C[3]/4,C[3]&=3;
            if(C[2]||C[1]||C[3])++S;
        }   
        printf("Case #%d: %d\n",i+1,S);
    }
    return 0;
}

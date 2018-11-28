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
#define MX (26)
char s[MX][MX];
int N,M,C;
bool ok(int x,int y,char C){
    F(N)FF(M)if(s[i][j]==C){
        int a=min(i,x),b=max(i,x),c=min(j,y),d=max(j,y);
        FOR(m,a,b+1)FOR(n,c,d+1)if(s[m][n]^63&&s[m][n]^C)return 0;
    }
    return 1;
}
void go(int x,int y,char C){
    F(N)FF(M)if(s[i][j]==C){
        int a=min(i,x),b=max(i,x),c=min(j,y),d=max(j,y);
        FOR(m,a,b+1)FOR(n,c,d+1)s[m][n]=C;
    }
}
int main(void){
    IN(_)F(_){
        scanf("%d%d",&N,&M),C=0;
        F(N)scanf("%s",s[i]);
        F(N)FF(M)if(s[i][j]^63)C|=1<<(s[i][j]-65);
        F(N)FF(M)if(s[i][j]^63)FT(0,N)FOR(l,0,M)if(s[i][j]==s[k][l]){
            int a=min(i,k),b=max(i,k),c=min(j,l),d=max(j,l);
            FOR(x,a,b+1)FOR(y,c,d+1)s[x][y]=s[i][j];
        }
        F(N)FF(M)if(s[i][j]==63)FT(0,26)if(C&1<<k&&ok(i,j,k+65))go(i,j,k+65),k=666;
        printf("Case #%d:\n",i+1);
        F(N)FF(M)assert(s[i][j]^63);
        F(N)puts(s[i]);
    }
    return 0;
}

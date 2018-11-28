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
const int MOD = 1e9+7;
const int SIZE = 111;
int dp3[SIZE][SIZE],dp4[SIZE][SIZE][SIZE];
int dp33[SIZE][SIZE],dp44[SIZE][SIZE][SIZE];
template <class T>
void maa(T& x,T y){
    if(x<y)x=y;
}
template <class T>
void mii(T& x,T y){
    if(x>y)x=y;
}
void build(){
    MS1(dp3);
    MS1(dp4);
    dp3[0][0]=dp4[0][0][0]=0;
    REP(i,SIZE)REP(j,SIZE){
        if(dp3[i][j]==-1)continue;
        if(i+3<SIZE)maa(dp3[i+3][j],dp3[i][j]+1);
        if(j+3<SIZE)maa(dp3[i][j+3],dp3[i][j]+1);
        if(i+1<SIZE&&j+1<SIZE)maa(dp3[i+1][j+1],dp3[i][j]+1);
    }
    REP(i,SIZE)REP(j,SIZE){
        dp33[i][j]=dp3[i][j];
        if(i>0)maa(dp33[i][j],dp33[i-1][j]);
        if(j>0)maa(dp33[i][j],dp33[i][j-1]);
    }
    REP(i,SIZE)REP(j,SIZE){
        if(i+j==0)continue;
        if(dp3[i][j]==-1)maa(dp3[i][j],dp33[i][j]+1);
    }
    REP(i,SIZE)REP(j,SIZE)REP(k,SIZE){
        if(dp4[i][j][k]==-1)continue;
        if(i+4<SIZE)maa(dp4[i+4][j][k],dp4[i][j][k]+1);
        if(j+2<SIZE)maa(dp4[i][j+2][k],dp4[i][j][k]+1);
        if(k+4<SIZE)maa(dp4[i][j][k+4],dp4[i][j][k]+1);
        if(i+1<SIZE&&k+1<SIZE)maa(dp4[i+1][j][k+1],dp4[i][j][k]+1);
        if(i+2<SIZE&&j+1<SIZE)maa(dp4[i+2][j+1][k],dp4[i][j][k]+1);
        if(j+1<SIZE&&k+2<SIZE)maa(dp4[i][j+1][k+2],dp4[i][j][k]+1);
    }
    REP(i,SIZE)REP(j,SIZE)REP(k,SIZE){
        dp44[i][j][k]=dp4[i][j][k];
        if(i>0)maa(dp44[i][j][k],dp44[i-1][j][k]);
        if(j>0)maa(dp44[i][j][k],dp44[i][j-1][k]);
        if(k>0)maa(dp44[i][j][k],dp44[i][j][k-1]);
    }
    REP(i,SIZE)REP(j,SIZE)REP(k,SIZE){
        if(i+j+k==0)continue;
        if(dp4[i][j][k]==-1)maa(dp4[i][j][k],dp44[i][j][k]+1);
    }
}
int main(){
    build();
    CASET{
        DRII(n,p);
        int an=0;
        int d[4]={};
        REP(i,n){
            DRI(x);
            if(x%p==0)an++;
            else d[x%p]++;
        }
        if(p==2){
            an+=(d[1]+1)/2;
        }
        else if(p==3){
            an+=dp3[d[1]][d[2]];
        }
        else{
            an+=dp4[d[1]][d[2]][d[3]];
        }
        printf("Case #%d: %d\n",case_n++,an);
    }
    return 0;
}

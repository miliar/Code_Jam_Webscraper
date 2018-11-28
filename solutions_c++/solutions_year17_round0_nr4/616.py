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
const int SIZE = 1e6+10;
int a[100][100],b[100][100];
int main(){
    CASET{
        DRII(N,M);
        MS0(a);
        REP(i,M){
            char c[4];
            RS(c);
            DRII(x,y);x--;y--;
            if(c[0]=='+')a[x][y]|=1;
            else if(c[0]=='x')a[x][y]|=2;
            else a[x][y]|=3;
        }
        memcpy(b,a,sizeof(a));
        int st=0;
        REP(i,N){
            b[0][i]|=1;
            if(i&&i!=N-1)b[N-1][i]|=1;
            if(b[0][i]&2)st=i;
        }
        REP(i,N)b[i][(i+st)%N]|=2;
        VPII ch;
        REP(i,N)REP(j,N)
            if(a[i][j]!=b[i][j])ch.PB(MP(i,j));
        printf("Case #%d: %d %d\n",case_n++,max(2,N*3-2),SZ(ch));
        REP(i,SZ(ch)){
            char c=b[ch[i].F][ch[i].S];
            printf("%c %d %d\n",c==1?'+':(c==2?'x':'o'),ch[i].F+1,ch[i].S+1);
        }
    }
    return 0;
}

#include <iostream>
#include <algorithm>

#define SZ(X) ((X).size())
#define ALL(X) (X).begin(), (X).end()
#define REP(I, N) for (int I = 0; I < N; ++I)
#define REPP(I, A, B) for (int I = (A); I < B; ++I)
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
#define PLL pair<LL,LL>
#define VPLL vector<PLL >
#define IOS ios_base::sync_with_stdio(false);cin.tie(0)
#define Fi first
#define Se second
typedef long long int LL;
using namespace std;

int digit[20],ans[20];
int len(LL a){
    int i=0;
    for(;a;a/=10,++i)digit[i]=a%10;
    return i;
}
/*bool BF(LL a){
    int m=9;
    for(;a;a/=10){if(a%10>m)return false; m=min(a%10,(LL)m);}
    return true;
}*/
int main(){
    freopen("B-large.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    DRI(T);
    REP(t, T){
        fill(digit, digit+20,0);
        fill(ans, ans+20, 0);
        LL a;
        scanf("%lld",&a);
        
        
        
        printf("Case #%d: ",t+1);
        int l=len(a);
        for(int i=l-1;i>=0;--i){
            if(digit[i]<digit[i+1]){
                while(digit[i]<=digit[i+1])++i;
                ans[i]=digit[i];
                --ans[i--];
                for(;i>=0;--i)ans[i]=9;
            }else{
                ans[i]=digit[i];
            }
        }
        bool ok=0;
        
        
        /*while (!BF(a)) --a;
        for(int i=0;a;a/=10,++i)if(a%10!=ans[i])puts("WA");*/
        
        for(int i=19;i>=0;--i){
            if(ans[i])ok=1;
            if(ok)printf("%d",ans[i]);
        }puts("");
        
    }
}

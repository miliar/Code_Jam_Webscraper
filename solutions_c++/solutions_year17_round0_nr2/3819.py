#include <bits/stdc++.h>
#define REP(i,x,y) for(int i=x;i<(y);++i)
#define RREP(i,x,y) for(int i=x;i>(y);--i)
#define maxn 20
using namespace std;
typedef long long ll;
int a[maxn];
ll n;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("data.out","w",stdout);
    int T;scanf("%d",&T);int cas=1;
    while(T--){
        scanf("%I64d",&n);
        memset(a,0,sizeof(a));
        int cnt=1;
        while(n){
            a[cnt]=n%10;
            n/=10LL;
            ++cnt;
        }
        int pos=0;
        REP(i,2,cnt){
            if(a[i]>a[i-1]){
                a[i]-=1;
                pos=i;
            }
        }
        RREP(i,pos-1,0) a[i]=9;
        printf("Case #%d: ",cas++);
        RREP(i,cnt-1,0){
            if(!a[i]) continue;
            printf("%d",a[i]);
        }
        puts("");
    }
}

#include<bits/stdc++.h>
using namespace std;
#define lala long long int
#define mx 1009
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,cs=1,n,i,k,d,spd,pos;
    double tm;
    scanf("%d",&t);
    while(t--){
        scanf("%d %d",&d,&n);
        tm=0.0;
        while(n--){
            scanf("%d %d",&pos,&spd);
            tm=max(tm,(d-pos+0.0)/spd);
        }
        tm=d/tm;
        printf("Case #%d: %.8lf\n",cs++,tm+10e-12);
    }
    return 0;
}

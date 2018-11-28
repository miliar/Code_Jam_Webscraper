#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

#define INF 0x3f3f3f3f
ll n,K;
ll num[100],val[100];
int head,tail;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,tt=0;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld %lld",&n,&K);
        printf("Case #%d: ",++tt);
        head=0,tail=1;
        num[head]=1,val[head]=n;
        ll cnt=0;
        while(head<tail)
        {
            if(val[head]%2==1)
            {
                int r=val[head]/2;
                if(tail-1>=head&&val[tail-1]==r) num[tail-1]+=num[head]*2;
                else if(tail-2>=head&&val[tail-2]==r) num[tail-2]+=num[head]*2;
                else num[tail]=num[head]*2,val[tail++]=r;
                cnt+=num[head];
            }
            else
            {
                int r=val[head]/2;
                if(tail-1>=head&&val[tail-1]==r) num[tail-1]+=num[head];
                else if(tail-2>=head&&val[tail-2]==r) num[tail-2]+=num[head];
                else num[tail]=num[head],val[tail++]=r;

                if(tail-1>=head&&val[tail-1]==r-1) num[tail-1]+=num[head];
                else if(tail-2>=head&&val[tail-2]==r-1) num[tail-2]+=num[head];
                else num[tail]=num[head],val[tail++]=r-1;

                cnt+=num[head];
            }
            if(cnt>=K) break;
            head++;
        }
        printf("%lld %lld\n",val[head]/2,(val[head]-1)/2);
    }
    return 0;
}

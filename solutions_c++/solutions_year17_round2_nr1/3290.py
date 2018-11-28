#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
lli power(int x,int y)
{
    if(y==0)
        return 1;

    if(y&1)
        return x*power(x,y-1);
    lli ans= power(x,y/2);
    return ans*ans;
}

int t,cas,n;
double tim,ans,d,k[1005],s[1005];

int main()
{
    int i;
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d",&t);
    while(t--)
    {
        cas++;
        scanf("%lf%d",&d,&n);

        for(i=0;i<n;i++)
            scanf("%lf%lf",&k[i],&s[i]);
        tim=0.0;
        for(i=0;i<n;i++){
            tim= max(tim, (d-k[i])/s[i]);
            //cout<<tim<<"\n";
        }

        ans= d/tim;
        //cout<<ans;
        cout << "Case #" << cas << ": ";
        printf("%.7f\n",ans);
        //printf("Case #%d: ",cas);
        //printf("%.7lf\n",ans);
    }
    return 0;
}

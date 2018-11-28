#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("i.in","r",stdin);
    freopen("o.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int x=1;x<=t;x++)
    {
        long long int n,k;
        scanf("%lld %lld",&n,&k);
        map<long long int ,long long int> mp;
        mp[n]=1;
        long long int sum=0,ans,m;
        while(1)
        {
            sum+=mp[n];
            if(sum>=k)
            {
                ans=n;
                break;
            }
            m=n-1;
            mp[m/2]+=mp[n];
            mp[m-m/2]+=mp[n];
            sum+=mp[n-1];
            if(sum>=k)
            {
                ans=n-1;
                break;
            }
            m=n-2;
            mp[m/2]+=mp[n-1];
            mp[m-m/2]+=mp[n-1];
            n=n/2;
        }
        ans--;
        long long int mn=ans/2;
        long long int mx=ans-ans/2;
        printf("Case #%d: %lld %lld\n",x,mx,mn);
    }
    return 0;
}

#include <bits/stdc++.h>
using namespace std;
void solve()
{
    int n,p;
    scanf("%d%d",&n,&p);
    int t[4]={0,0,0,0};
    int ans=0;
    for(int i=0;i<n;i++)
    {
        int a;
        scanf("%d",&a);
        if(a%p==0)
            ++ans;
        else
            ++t[a%p];
    }
    if(p==2)
    {
        ans+=(t[1]+1)/2;
    }
    if(p==3)
    {
        int x=min(t[1],t[2]);
        ans+=x;
        t[1]-=x,t[2]-=x;
        ans+=(t[1]+t[2]+2)/3;
    }
    if(p==4)
    {
        int x=min(t[1],t[3]);
        ans+=x;
        t[1]-=x,t[3]-=x;
        ans+=t[2]/2;
        if(t[2]&1)
        {
            ++ans;
            if(t[1]>=2)
            {
                t[1]-=2;
                ans+=(t[1]+3)/4;
            }
        }
    }
    printf("%d\n",ans);
}

int main()
{
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d: ",cas++);
        solve();
    }
    return 0;
}

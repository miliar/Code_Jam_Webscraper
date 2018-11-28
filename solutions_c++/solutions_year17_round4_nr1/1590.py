#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t,n,p,g[111];
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d%d",&n,&p);
        for (int i=1;i<=n;++i) scanf("%d",g+i);
        int ans=0;
        if (p==2)
        {
            for (int i=1;i<=n;++i)
                if (g[i]%2==0)
                    ++ans;
            ans+=(n-ans+1)/2;
        }
        else if (p==3)
        {
            int cnt1=0,cnt2=0;
            for (int i=1;i<=n;++i)
                if (g[i]%3==0)
                    ++ans;
                else if (g[i]%3==1)
                    ++cnt1;
                else ++cnt2;
            if (cnt1>cnt2) swap(cnt1,cnt2);
            ans+=cnt1;
            ans+=(cnt2-cnt1+2)/3;
        }
        else if (p==4)
        {
            ;
        }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}

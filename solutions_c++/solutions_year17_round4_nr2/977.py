#include<bits/stdc++.h>
using namespace std;

int cs[1001], cp[1001];
int main()
{
    int T;
    scanf("%d",&T);
    for(int tc=1;tc<=T;tc++)
    {
        memset(cs,0,sizeof(cs));
        memset(cp,0,sizeof(cp));
        printf("Case #%d: ",tc);
        int n,c,m;
        scanf("%d%d%d", &n, &c, &m);
        int ans1=0,ans2=0;
        for(int i=0;i<m;i++)
        {
            int a,b;
            scanf("%d%d",&a,&b);
            cs[a]++;
            cp[b]++;
            if(cp[b]>ans1)
                ans1 = cp[b];
        }
        int fr = 0;
        for(int i=1;i<=n;i++)
        {
            fr += ans1;
            while(cs[i]>fr)
            {
                ans1++;
                fr += i;
            }
        }
        for(int i=1;i<=n;i++)
            if(cs[i]>ans1) ans2 += cs[i]-ans1;
        printf("%d %d\n",ans1,ans2);
    }
}


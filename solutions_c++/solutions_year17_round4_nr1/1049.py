#include<bits/stdc++.h>
using namespace std;

int s[100];
int cnt[4];
int main()
{
    int T;
    scanf("%d",&T);
    for(int tc=1;tc<=T;tc++)
    {
        memset(cnt,0,sizeof(cnt));
        printf("Case #%d: ",tc);
        int n, p;
        scanf("%d%d",&n,&p);
        for(int i=0;i<n;i++)
        {
            scanf("%d",s+i);
            cnt[s[i]%p]++;
        }
        int ans = cnt[0];
        if(p == 2)
        {
            ans += (cnt[1]+1)/2;
        }
        else if(p == 3)
        {
            int x = min(cnt[1],cnt[2]);
            ans += x;
            cnt[1] -= x;
            cnt[2] -= x;
            x = cnt[1]/3;
            ans += x;
            cnt[1] -= x*3;
            x = cnt[2]/3;
            ans += x;
            cnt[2] -= x*3;
            if(cnt[1] || cnt[2])
                ans++;

        }
        else if(p == 4)
        {
            int x = min(cnt[1],cnt[3]);
            ans += x;
            cnt[1] -= x;
            cnt[3] -= x;
            x = cnt[2]/2;
            ans += x;
            cnt[2] -= x*2;
            x = min(cnt[1]/2,cnt[2]);
            ans += x;
            cnt[1] -= 2*x;
            cnt[2] -= x;
            x = min(cnt[3]/2,cnt[2]);
            ans += x;
            cnt[3] -= 2*x;
            cnt[2] -= x;
            x = cnt[1]/4;
            ans += x;
            cnt[1] -= x*4;
            x = cnt[3]/4;
            ans += x;
            cnt[3] -= x*4;
            if(cnt[1] || cnt[2] || cnt[3])
                ans++;
        }
        printf("%d\n",ans);
    }
}


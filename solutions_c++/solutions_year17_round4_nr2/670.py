#include<bits/stdc++.h>

using namespace std;
int g[1010];
int s[1010],n,c,m;
int main()
{
    freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int tt=1; tt<=cas; tt++)
    {
        scanf("%d%d%d",&n,&c,&m);
        memset(g,0,sizeof(g));
        memset(s,0,sizeof(s));
        for (int i=1; i<=m; i++)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            g[x]++;
            s[y]++;
        }
        int a1=0,a2=0;
        for (int i=1; i<=n; i++)
        {
            g[i]=g[i-1]+g[i];
            a1=max(a1,(g[i]+i-1)/i);
        }
        for (int i=1; i<=c; i++)
            a1=max(a1,s[i]);
        for (int i=1; i<=n; i++)
            a2+=max(0,g[i]-g[i-1]-a1);
        printf("Case #%d: %d %d\n",tt,a1,a2);
      /*  if (c==2)
        {
            if (n==1)
            {
                printf("%d 0\n",m);
                continue;
            }
            int s11=g[1][1],s21=g[2][1],s22=0,s12=0;
            for (int i=2; i<=n; i++)
            {
                s12+=g[1][i];
                s22+=g[2][i];
            }
            int l1=min(s11,s22),l2=min(s12,s21);
            int ans=l1+l2;
            s11-=l1; s22-=l1; s12-=l2; s21-=l2;
            if (s11&&s12) printf("%d 0\n",ans+s11+s12);
            else if (s22&&s21) printf("%d 0\n",ans+s22+s21);
            else if (s11&&s21) printf("%d 0\n",ans+s11+s21);
            else printf("%d %d\n",ans+max(s12,s22),min(s12,s22));
        }*/

    }
}

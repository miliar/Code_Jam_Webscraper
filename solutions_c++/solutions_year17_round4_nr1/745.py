#include<bits/stdc++.h>

using namespace std;
int n,p,c[10];
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("a.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int tt=1; tt<=cas; tt++)
    {
        scanf("%d%d",&n,&p);
        memset(c,0,sizeof(c));
        for (int i=1; i<=n; i++)
        {
            int x;
            scanf("%d",&x);
            c[x%p]++;
        }
        printf("Case #%d: ",tt);
        if (p==2)
        {
            printf("%d\n",c[0]+(c[1]+1)/2);
            continue;
        }
        if (p==3)
        {
            int ans=c[0];
            if(c[1] >= c[2]) {
				ans += c[2]; c[1] -= c[2];
				ans += (c[1]+2)/3;
			} else {
				ans += c[1]; c[2] -= c[1];
				ans += (c[2]+2)/3;
			}
            printf("%d\n",ans);
        }
        if (p==4)
        {
            int ans=c[0];
			ans+=c[2]/ 2; c[2] %= 2;
			if(c[1] >= c[3]) {
				ans += c[3]; c[1] -= c[3];
				ans += c[1]/4; c[1] %= 4;
				ans += (c[1]+2*c[2]+3)%4;
			} else {
				ans += c[1]; c[3] -= c[1];
				ans += c[3]/4; c[3] %= 4;
				if(c[2] == 0) ans ++;
				else {
					ans+=(c[3]+2*c[2]+3)%4;
				}
			}
			 printf("%d\n",ans);
        }
    }
}

#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
using namespace std;
int a[505];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        int n,p;
        scanf("%d%d",&n,&p);
        int ans = 1;
        int c[6];
        c[0] = c[1] = c[2] = c[3] = 0;
        int sum = 0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            a[i] %= p;
            c[a[i]] ++;
            sum += a[i];

        }
        sort(a, a+n);
        ans += c[0];
        if(p == 2)
        {
            ans += c[1]/2;
        }
        else if(p == 3)
        {
            ans += min(c[1], c[2]);
            int gg = min(c[1], c[2]);
            c[1] -= gg;
            c[2] -= gg;
            ans += c[1] /3;
            ans += c[2] /3;
        }
        else if(p ==4)
        {
            ans += c[2] / 2;
            c[2] %= 2;
            ans += min(c[1], c[3]);
            int gg=min(c[1], c[3]);
            c[1] -= gg;
            c[3] -= gg;
            if(c[2]>=1&&c[1]>=2)
            {
                ans ++;
                c[2] --;
                c[1] -=2;
            }
            ans +=c[1]/4;
            ans +=c[3]/4;
        }
        if(sum%p==0)
        ans--;
        printf("Case #%d: %d\n", ++cas, ans);



    }
}

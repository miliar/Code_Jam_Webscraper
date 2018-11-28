#include<bits/stdc++.h>
using namespace std;

char in[1005];
bool s[1000];

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int k, n, ans=0;
        scanf("%s%d",in,&k);
        for(n=0;in[n] == '+' || in[n] == '-';n++)
            s[n] = in[n] == '+';
        for(int i=0;i+k<=n;i++)
        {
            if(s[i]) continue;
            ans++;
            for(int j=0;j<k;j++)
                s[i+j] = !s[i+j];
        }
        bool ok = true;
        for(int i=0;i<n;i++)
            ok &= s[i];
        if(!ok) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }
}

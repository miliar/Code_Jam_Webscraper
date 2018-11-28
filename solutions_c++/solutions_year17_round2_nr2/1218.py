#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
int T,a,b,c,n;
void solve()
{
    if((a&&!b&&!c)||(!a&&b&&!c)||(!a&&!b&&c))
    {
        printf("IMPOSSIBLE");
        return;
    }
    if((a&&b&&!c)||(a&&!b&&c)||(!a&&b&&c))
    {
        if(a==b)
        {
            while(a--)
                printf("RY");
        }
        else if(a==c)
        {
            while(a--)
                printf("RB");
        }
        else if(b==c)
        {
            while(b--)
                printf("YB");
        }
        else printf("IMPOSSIBLE");
        return;
    }
    if(a==b&&a==c)
    {
        while(a--)
            printf("RYB");
        return;
    }
    string s;
    if(a>=b&&a>=c)
        s="R",--a;
    else if(b>=a&&b>=c)
        s="Y",--b;
    else s="B",--c;
    for(int i=2;i<=n;++i)
    {
        if(s.back()=='R')
        {
            if(b>c)
                s+="Y",--b;
            else if(b<c)
                s+="B",--c;
            else if(s.front()=='Y')
                s+='Y',--b;
            else s+='B',--c;
        }
        else if(s.back()=='Y')
        {
            if(a>c)
                s+="R",--a;
            else if(a<c)
                s+="B",--c;
            else if(s.front()=='R')
                s+="R",--a;
            else s+="B",--c;
        }
        else
        {
            if(a>b)
                s+="R",--a;
            else if(a<b)
                s+="Y",--b;
            else if(s.front()=='R')
                s+="R",--a;
            else s+="Y",--b;
        }
    }
    if(!a&&!b&&!c&&s.front()!=s.back())
    {
        cout<<s;
        return;
    }
    printf("IMPOSSIBLE");
}
int main()
{
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        scanf("%d",&n);
        scanf("%d%*d%d%*d%d%*d",&a,&b,&c);
        printf("Case #%d: ",t);
        solve();
        putchar('\n');
    }
    return 0;
}

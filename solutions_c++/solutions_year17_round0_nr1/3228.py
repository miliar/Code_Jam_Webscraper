#include <bits/stdc++.h>
#define fread(ch) freopen(ch,"r",stdin)
#define fwrite(ch) freopen(ch,"w",stdout)

using namespace std;

const int  INF = 0x3f3f3f3f;

char str[10];
int ans,k;

bool cal(int len)
{
    for(int i = 0; i < len; ++i)
        if(str[i] == '-') return false;
    return true;
}

bool rush(int pos,int len)
{
    if(len-pos < k) return false;
    for(int i = pos; i < pos+k; ++i)
    {
        if(str[i] == '+') str[i] = '-';
        else str[i] = '+';
    }
    return true;
}

void solve(int pos,int len,int tmp)
{
    if(pos == len)
    {
        if(cal(len)) ans = min(ans,tmp);
        return;
    }
    if(rush(pos,len))
    {
        solve(pos+1,len,tmp+1);
        rush(pos,len);
    }
    solve(pos+1,len,tmp);
}

int main()
{
    fread("A-small-attempt1.in");
    fwrite("out.out");
    int t;

    scanf("%d",&t);

    for(int z = 1; z <= t; ++z)
    {
        scanf("%s%d",str,&k);
        ans = INF;

        solve(0,strlen(str),0);

        printf("Case #%d: ",z);
        if(ans == INF) puts("IMPOSSIBLE");
        else printf("%d\n",ans);
    }

    return 0;
}

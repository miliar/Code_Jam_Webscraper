#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int maxn = 1005;
const int INF = (1<<30) - 1;
char s[maxn];
int n,k;

void flip(int x)
{
    for(int i = x;i <= x + k-1;i++)
    {
        if(s[i] == '+') s[i] = '-';
        else s[i] = '+';
    }

}

int ok()
{
    for(int i = 0;i < n;i++) if(s[i] == '-') return 0;
    return 1;
}

int main()
{
    int T;

    freopen("A-large.txt","r",stdin);
    freopen("Ajjyjy.txt","w",stdout);

    scanf("%d",&T);
    for(int kase = 1;kase <= T;kase++)
    {
        scanf("%s %d",s,&k);
        printf("Case #%d: ",kase);
        int ans = 0;
        n = strlen(s);
        for(int i = 0;i <= n-k;i++)
        {
            if(s[i] == '-') flip(i),ans++;
        }
        if(ok()) printf("%d\n",ans);
        else puts("IMPOSSIBLE");

    }
    return 0;
}



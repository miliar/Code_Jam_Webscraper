#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
const int N = 2000;
char f[N];
int n , m;

void init()
{
    scanf("%s",f + 1);
    n = strlen(f + 1);
    scanf("%d",&m);
}

void work()
{
    int ans = 0;
    for(int i = 1;i + m - 1 <= n;i++)
    if(f[i] == '-')
    {
        for(int j = i;j <= i + m - 1;j++)
        {
            f[j] = '+' + '-' - f[j];
        }
        ans++;
    }

    for(int i = 1;i <= n;i++)
    if(f[i] == '-')
    {
        printf("IMPOSSIBLE\n");
        return;
    }
    printf("%d\n",ans);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int i = 1;i <= T;i++)
    {
        printf("Case #%d: ",i);
        init();
        work();
    }

    return 0;
}

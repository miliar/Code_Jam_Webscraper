#include<bits/stdc++.h>

using namespace std;
char b[1010],a[1010];
int n;
int f[20][15][2];
bool dp(int i,int c,int les)
{
    if (i==n+1) return 1;
    if (f[i][c][les]>-1) return f[i][c][les];
    int d=(les)?a[i]-'0':9;
    for (int x=d; x>=c; x--)
    {
        if (dp(i+1,x,les&&(x==d)))
        {
            b[i]=x+'0';
            f[i][c][les]=1;
            return 1;
        }
    }
    f[i][c][les]=0;
    return 0;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("b.out","w",stdout);
    int cas,k;
    scanf("%d",&cas);
    for (int tt=1; tt<=cas; tt++)
    {
        scanf("%s",a+1);
        a[0]='0';
        n=strlen(a+1); a[n+1]='9';
        for (int i=1; i<=n; i++) b[i]='9';
        printf("Case #%d: ",tt);
        memset(f,255,sizeof(f));
        dp(1,0,1);
        int i=1;
        while (b[i]=='0') i++;
        for (;i<=n; i++) printf("%c",b[i]);
        cout <<endl;
    }
}

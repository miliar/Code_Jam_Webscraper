#include<bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pi pair<int,int>
using namespace std;
pi q[50];
int a[50][50],n,m;
bool v[50];
char s[50];

bool check(int l,int r,int j)
{
    for (int i=l; i<=r; i++)
        if (a[i][j]>-1) return 0;
    return 1;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int tt=1; tt<=cas; tt++)
    {
        scanf("%d%d",&n,&m);
        printf("Case #%d:\n",tt);
        memset(a,0,sizeof(a));
        memset(v,0,sizeof(v));
        for (int i=1; i<=n; i++)
        {
            scanf("%s",s+1);
            for (int j=1; j<=m; j++)
                if (s[j]=='?') a[i][j]=-1;
                else {
                    int x=s[j]-'A';
                    q[x]=mp(i,j);
                    a[i][j]=x;
                }
        }
        for (int y=1; y<=m; y++)
            for (int x=1; x<=n; x++)
            if (a[x][y]>-1&&!v[a[x][y]])
            {
                int i=a[x][y],l=x,r=x;
                v[i]=1;
                for (int j=x-1; j>=0; j--)
                    if (a[j][y]==-1) a[j][y]=i;
                    else {
                        l=j+1;
                        break;
                    }
                for (int j=x+1; j<=n+1; j++)
                    if (a[j][y]==-1) a[j][y]=i;
                    else {
                        r=j-1;
                        break;
                    }
                for (int j=y-1; j; j--)
                    if (check(l,r,j))
                    {
                        for (int k=l; k<=r; k++)
                            a[k][j]=i;
                    }
                    else break;

                for (int j=y+1; j<=m; j++)
                    if (check(l,r,j))
                    {
                        for (int k=l; k<=r; k++)
                            a[k][j]=i;
                    }
                    else break;
            }
        for (int i=1; i<=n; i++)
        {
            for (int j=1; j<=m; j++)
                printf("%c",a[i][j]+'A');
            puts("");
        }
    }
}


#include<bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pi pair<int,int>

using namespace std;
int a[100010];
pi q[60][60];
vector<int> g;
int n,m,t,ans,r[60],b[60];

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("b.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int tt=1; tt<=cas; tt++)
    {
        scanf("%d%d",&n,&m);
        for (int i=1; i<=n; i++)
            scanf("%d",&r[i]);
        t=0;
        for (int i=1; i<=n; i++)
        {
            for (int j=1; j<=m; j++)
            {
                int w;
                scanf("%d",&w);
                int y=w/(r[i]*0.9);
                int x=w/(r[i]*1.1);
                g.clear();
                for (int k=max(1,x); k<=y; k++)
                    if (0.9*r[i]*k<=w&&w<=1.1*r[i]*k)
                        g.push_back(k);
                if (g.size())
                {
                  //  cout <<i<<" "<<j<<" "<<g[0]<<" "<<g[g.size()-1]<<endl;
                    q[i][j]=mp(g[0],g[g.size()-1]);
                    a[++t]=g[0];
                    a[++t]=g[g.size()-1];
                }
                else q[i][j]=mp(0,0);
            }
            sort(q[i]+1,q[i]+1+m);
            b[i]=1;
        }
        sort(a+1,a+1+t);
        ans=0;
        for (int i=1; i<=t; i++)
        {
            int ff=0;
            for (int j=1; j<=n; j++)
            {
                while (b[j]<=m&&q[j][b[j]].se<a[i]) b[j]++;
                if (b[j]<=m&&q[j][b[j]].fi<=a[i]&&a[i]<=q[j][b[j]].se)
                    ff++;
            }
            //cout <<a[i]<<" "<<ff<<endl;
            if (ff==n)
            {
                for (int j=1; j<=n; j++) b[j]++;
                ans++;
            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }
}

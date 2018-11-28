#include <cstdio>
#include <algorithm>

using namespace std;

const int inf=1e9;
pair<int,int> v[55][55];
int val[55],poz[55];

int main()
{
    freopen("file.in", "r", stdin);
    freopen("file.out", "w", stdout);
    int test;
    scanf("%d",&test);
    for(int t=1;t<=test;t++)
    {
        int n,m,sol=0,a;
        scanf("%d%d",&n,&m);
        for(int i=1;i<=n;i++) scanf("%d",&val[i]);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=m;j++)
            {
                scanf("%d",&a);
                double s=(a*10.0)/(11.0*val[i]);
                int x=s;
                if(s>x) x++;
                int y=(a*10.0)/(9.0*val[i]);
                v[i][j]={x,y};
            }
            sort(v[i]+1,v[i]+1+m);
        }
        for(int i=1;i<=n;i++) poz[i]=1;
        while(1)
        {
            int ok=1,x=1,y=inf;
            for(int i=1;i<=n;i++)
            {
                if(poz[i]==m+1) {ok=0;break;}
                x=max(x,v[i][poz[i]].first);
                y=min(y,v[i][poz[i]].second);
            }
            if(!ok) break;
            if(x<=y)
            {
                sol++;
                for(int i=1;i<=n;i++) poz[i]++;
            }
            else
            {
                int minn=inf,ind=0;
                for(int i=1;i<=n;i++)
                    if(v[i][poz[i]].first<minn) {minn=v[i][poz[i]].first,ind=i;}
                poz[ind]++;
            }
        }
        printf("Case #%d: %d\n",t,sol);
    }
    return 0;
}

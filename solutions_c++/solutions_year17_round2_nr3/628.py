#include <cstring>
#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <iostream>
#include <iomanip>
using namespace std;

typedef long long ll;

const int maxn = 305;
const double eps = 1e-8;
const double inf = 1e15;
int n,q;
double e[maxn],s[maxn];
double dis[maxn][maxn];

double g[maxn][maxn];

void floyd()
{
  for(int k=1;k<=n;k++)
    for(int i=1;i<=n;i++)
      for(int j=1;j<=n;j++)
      {
        g[i][j] = min(g[i][j],g[i][k] + g[k][j]);
      }
}
int main()
{

  int t,cs = 0;
  scanf("%d",&t);
  while(t--)
  {
    scanf("%d%d",&n,&q);
    for(int i=1;i<=n;i++)
      scanf("%lf%lf",e+i,s+i);
    for(int i=1;i<=n;i++)
      for(int j=1;j<=n;j++)
      {
        scanf("%lf",&dis[i][j]);
        if(dis[i][j] < 0)
          dis[i][j] = inf;
      }
    for(int k=1;k<=n;k++)
      for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
        {
          dis[i][j] = min(dis[i][j],dis[i][k] + dis[k][j]);
        }
    for(int i=1;i<=n;i++)
    {
      for(int j=1;j<=n;j++)
      {
        if(i==j)
          g[i][j] = 0;
        else if(dis[i][j] > e[i])
          g[i][j] = inf;
        else
          g[i][j] = dis[i][j]/s[i];
        //printf("i=%d,j=%d,g=%lf\n",i,j,g[i][j] );
      }
    }
    floyd();
    printf("Case #%d:",++cs);
    int a,b;
    while(q--)
    {
      scanf("%d%d",&a,&b);
      printf(" %.7lf",g[a][b]);
    }
    puts("");
  }
}
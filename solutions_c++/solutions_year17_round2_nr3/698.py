#include<bits/stdc++.h>

using namespace std;

int T;
int m,n,q;
typedef long long ll;
ll dis[111][111];
ll sum[111][111];

struct node
{
  ll dis;
  ll speed;
}f[111];

double ans[111];
int st,ed;

double calc(int l,int r)
{
  double dis = sum[l][r];
  double speed = f[l].speed;
  if(dis!=-1)
    return dis/speed;
  else
    return 1e30;
}



int main()
{
  freopen("C-large.in","r",stdin);
  freopen("C-large.out","w",stdout);
  cin>>T;
  for(int it=1;it<=T;it++)
  {
    printf("Case #%d: ",it);
    cin>>m>>n;
    for(int i=1;i<=m;i++)
      cin>>f[i].dis>>f[i].speed;
    for(int i=1;i<=m;i++)
      for(int j=1;j<=m;j++)
      {
        cin>>dis[i][j];
        sum[i][j]=dis[i][j];
      }

    for(int k=1;k<=m;k++)
      for(int i=1;i<=m;i++)
        for(int j=1;j<=m;j++)
          if( sum[i][k]!=-1 && sum[k][j]!=-1
              &&(sum[i][j]==-1 || sum[i][j]>sum[i][k]+sum[k][j]))
            sum[i][j]=sum[i][k]+sum[k][j];

    for(int q=1;q<=n;q++)
    {
      cin>>st>>ed;
      for(int i=0;i<=m;i++)
        ans[i]=1e30;

      ans[st]=0;

      for(int k=1;k<=m;k++)
        for(int now=1;now<=m;now++)
          for(int old=1;old<=m;old++)
            if(sum[old][now]!=-1 && f[old].dis>=sum[old][now])
                ans[now]=min(ans[now],ans[old]+calc(old,now));
      printf("%.8f ",ans[ed]);
    }
    printf("\n");
  }

  return 0;
}



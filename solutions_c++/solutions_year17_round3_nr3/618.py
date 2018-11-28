#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double db;
const int N=1e6+5;
int n,k;
db p[N],u;
void solve()
{
  scanf("%d%d%Lf",&n,&k,&u);
  for(int i=1; i<=n; ++i) scanf("%Lf",&p[i]);
  sort(p+1,p+n+1);
  p[n+1]=1;
  for(int i=1; u>0&&i<=n; ++i)
  {
    db sum=(p[i+1]-p[i]);
    if(sum*i<=u)
    {
      u-=sum*i;
      for(int j=1; j<=i; ++j) p[j]=p[i+1];
    }
    else
    {
      for(int j=1; j<=i; ++j) p[j]+=u/i;
      break;
    }
  }
  db res=1.0;
  for(int i=1; i<=n; ++i) res*=p[i];
  printf("%.9Lf\n",res);
}
int main()
{
	int tt; scanf("%d",&tt); 
	for(int i=1; i<=tt; ++i)
	{
		printf("Case #%d: ",i);
		solve();
	}
}

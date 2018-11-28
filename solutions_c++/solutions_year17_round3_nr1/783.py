#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double db;
const int N=1e6+5;
int n,k;
pair<db,db> r[N];
void solve()
{
  scanf("%d%d",&n,&k);
  for(int i=1; i<=n; ++i) scanf("%Lf%Lf",&r[i].first,&r[i].second);
  sort(r+1,r+n+1,[](pair<db,db> a, pair<db,db> b){ return a.first*a.second > b.first*b.second; });
  db res=0.0;
  for(int i=1; i<=n; ++i)
  {
    db tem=M_PI*r[i].first*r[i].first+2.0*M_PI*r[i].first*r[i].second;
    int ile=0;
    for(int j=1; j<=n; ++j) if(j!=i)
    {
      ++ile; if(ile==k) break;
      tem+=2.0*M_PI*r[j].first*r[j].second;
    }
    res=max(res,tem);
  }
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

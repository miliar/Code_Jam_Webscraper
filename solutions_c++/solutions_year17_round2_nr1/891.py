#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double db;
const int N=1e6+5;
int n;
db d,k[N],s[N];
void solve()
{
  scanf("%Lf%d",&d,&n);
  for(int i=1; i<=n; ++i) scanf("%Lf%Lf",&k[i],&s[i]);
  db c=d*s[1]/(d-k[1]);
  for(int i=1; i<=n; ++i) c=min(c,d*s[i]/(d-k[i]));
  printf("%.10Lf\n",c);
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

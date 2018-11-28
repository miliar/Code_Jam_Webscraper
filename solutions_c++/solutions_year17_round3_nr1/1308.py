#include<bits/stdc++.h>
#define rep(i,j,k) for(int i=(j);i<(k);i++)
#define mp make_pair
#define sz(a) (int)(a).size()
#define pb push_back
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef long double ld;
//----head----
const double pi=acos(-1);
pii data[1005];
vector<pii> V;
int cmp1(pii a,pii b)
{
	return a>b;
}
double cal(pii a)
{
	return 2.0*pi*a.first*a.second;
}
int cmp2(pii a,pii b)
{
	return cal(a)>cal(b);
}
int main()
{
	freopen("0.in","r",stdin);
	freopen("0.out","w",stdout);
	int T;
	scanf("%d",&T);
	rep(cas,1,T+1)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		rep(i,0,n)scanf("%d%d",&data[i].first,&data[i].second);
		sort(data,data+n,cmp1);
		double ans=0.0;
		rep(i,0,n-k+1)
		{
			double anss=cal(data[i])+pi*data[i].first*data[i].first;
			V.clear();
			rep(j,i+1,n)V.pb(data[j]);
			sort(V.begin(),V.end(),cmp2);
			rep(j,0,k-1)anss+=cal(V[j]);
			ans=max(ans,anss);
		}
		printf("Case #%d: %.9lf\n",cas,ans);
	}
	return 0;
}

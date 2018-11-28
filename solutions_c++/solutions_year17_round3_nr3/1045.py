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
double data[55];
int cmp(double a,double b)
{
	return a>b;
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
		double m;
		scanf("%lf",&m);
		data[0]=1.0;
		rep(i,1,n+1)scanf("%lf",&data[i]);
		sort(data,data+n+1,cmp);
		for(int i=k;i>=1;i--)
		{
			if(m>=(data[i-1]-data[i])*(k-i+1))
			{
				m-=(data[i-1]-data[i])*(k-i+1);
				rep(j,i,k+1)data[j]=data[i-1];
			}
			else
			{
				data[i]+=m/(k-i+1);
				rep(j,i+1,k+1)data[j]=data[i];
				break;
			}
		}
		double ans=1.0;
		rep(i,1,k+1)ans*=data[i];
		printf("Case #%d: %.6lf\n",cas,ans);
	}
	return 0;
}

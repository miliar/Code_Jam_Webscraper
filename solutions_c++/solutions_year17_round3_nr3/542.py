#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
void ioinit()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.out","w",stdout);
}
ld p[57];
int n,k;
ld u;
bool check(ld k)
{
	ld res=0;
	for(int i=1;i<=n;i++)
	{
		res+=(k>p[i]?k-p[i]:0);
	}
	return res<=u;
}
int main()
{
	ioinit();
	int T;
	cin>>T;
	for(int kase=1;kase<=T;kase++)
	{
		cin>>n>>k;
		cin>>u;
		for(int i=1;i<=n;i++) cin>>p[i];
		ld l=0,r=1;
		for(int i=0;i<200;i++)
		{
			ld mid=(l+r)/2;
			if(check(mid)) l=mid;
			else r=mid;
		}
		ld ans=1;
		for(int i=1;i<=n;i++)
		{
			ans*=(l>p[i]?l:p[i]);
		}
		printf("Case #%d: %.15f\n",kase,(double)ans);
	}
	return 0;
}

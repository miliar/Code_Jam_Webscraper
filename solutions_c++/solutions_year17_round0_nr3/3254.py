#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long int lli;

pair<lli,lli> func(lli n,lli k)
{
	if(k==1)
	{
		return make_pair(n/2,(n-1)/2);
	}
	if(n&1)
	{
		return func((n-1)/2,k/2);
	}
	if(k&1)
	{
		return func((n/2)-1,k/2);
	}
	return func((n/2),k/2);
}

int main()
{
	int t,count;
	freopen("C-large.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	lli n,k;
	pair<lli,lli> ans;
	for(int testcase=1; testcase<=t; testcase++)
	{
		scanf("%lld%lld",&n,&k);
		ans=func(n,k);
		printf("Case #%d: %lld %lld\n",testcase,ans.first,ans.second);
	}
	return 0;
}

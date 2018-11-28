#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
using namespace std;
typedef long long LL;
bool check(LL t)
{
	while(t)
	{
		if(t%10<t/10%10)return 0;
		t/=10;
	}
	return 1;
}
int main()
{
	int T;
	LL n,ans;
	cin>>T;
	for(int qi=1;qi<=T;qi++)
	{
		printf("Case #%d: ",qi);
		cin>>n;
		ans=-1;
		if(check(n))ans=n;
		LL t=1;
		for(int i=0;i<=18;i++,t*=10)
		{
			LL m=n;
			m/=t;
			if(m%10==0)continue;
			m*=t;
			m--;
			if(check(m))ans=max(ans,m);
		}
		cout<<ans<<endl;
	}
	return 0;
}

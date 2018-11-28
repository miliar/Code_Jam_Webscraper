#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define INF 200000000
int a[1005],s[1005]; 
int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T;
	cin>>T;
	for(int qq=1;qq<=T;qq++)
	{
		ll ans = 0,K;
		memset(a,0,sizeof a);
		memset(s,0,sizeof s);
		string str;
		cin>>str>>K;
		int len = str.length();
		for(int i=0;i<len;i++)
		{
			if(str[i]=='+') a[i]=0;
			else a[i]=1;
		}
		int sum = 0;
		for(int i=0;i<len;i++)
		{
			s[i] = (a[i]+sum)%2!=0;
			sum += s[i] - (i>=K-1?s[i-K+1]:0);
			ans += s[i];
			if(i>len-K and s[i]!=0) 
			{
				ans = INF;	
			}
		}
		if(ans != INF)
			printf("Case #%d: %d\n",qq,ans);
		else printf("Case #%d: IMPOSSIBLE\n",qq);
	}
	return 0;
}
#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define bitcount __builtin_popcountll
#define ll long long
#define pb push_back
#define pi pair<int,int>
#define pii pair<pi,int>
#define mp make_pair
int main()
{
	int i,j,k;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	sd(t);
	for(int x=1;x<=t;x++)
	{
		int n;
		string s;
		cin>>s;
		sd(n);
		int ans=0;
		for(i=0;i<=s.size()-n;i++)
		{
			if(s[i]=='-')
			{
				for(j=0;j<n;j++)
				{
					s[i+j]=(s[i+j]=='-')?'+':'-';
				}
				ans++;
			}
		}
		while(i<s.size())
		{
			if(s[i]=='-')
				ans=-1;
			i++;
		}
		if(ans!=-1)
			printf("Case #%d: %d\n",x,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",x );
	}
	return 0;
}
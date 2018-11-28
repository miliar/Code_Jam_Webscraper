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
	int t;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	sd(t);
	for(int x=1;x<=t;x++)
	{
		string s;
		cin>>s;
		for(i=1;i<s.size();i++)
		{
			if(s[i]>=s[i-1])
				continue;
			for(j=i;j<s.size();j++)
				s[j]='9';
			break;
		}
		if(i==s.size())
		{
			printf("Case #%d: %s\n",x,s.c_str());
			continue;
		}
		i--;
		while(i!=0&&s[i]==s[i-1])
		{
			s[i]='9';
			i--;
		}
		s[i]--;
		i=0;
		while(s[i]=='0')
			i++;
		s=s.substr(i);
		printf("Case #%d: %s\n",x,s.c_str());
	}
	return 0;
}
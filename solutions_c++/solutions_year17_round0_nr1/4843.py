#include<bits/stdc++.h>
using namespace std;
#define lli long long int
int main()
{
	freopen("A-large.in","r",stdin);
    freopen("Cout5.out","w",stdout);
	lli t,k;
	string s;
	scanf("%lld",&t);
	for(lli z=1;z<=t;++z)
	{
		printf("Case #%lld: ",z);
		cin>>s;
		scanf("%lld",&k);
		if(k==s.length())
		{
			bool flag=true;
			for(lli i=1;i<s.length();++i)
			{
				if(s[i]!=s[i-1])
				{
					flag=false;
					printf("IMPOSSIBLE\n");
					break;
				}
			}
			if(flag)
			{
				if(s[0]=='-')
					printf("1\n");
				else
					printf("0\n");	
			}
		}
		else
		{
			lli c=0;
			for(lli i=0;i<=s.length()-k;++i)
			{
				if(s[i]=='-')
				{
					for(lli j=i;j<i+k;++j)
					{
						if(s[j]=='-')
							s[j]='+';
						else
							s[j]='-';	
					}
					c++;
				}
			}
			bool flag=true;
			for(lli i=0;i<s.length();++i)
			{
				if(s[i]=='-')
				{
					printf("IMPOSSIBLE\n");
					flag=false;
					break;
				}
			}
			if(flag)
			{
				printf("%lld\n",c);
			}
		}
	}
}

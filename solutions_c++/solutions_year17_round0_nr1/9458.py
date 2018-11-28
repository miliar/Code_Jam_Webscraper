
#include<bits/stdc++.h>
using namespace std;
#define INF 4294967296

int main()
{
	int t;
	long long int n;
	scanf("%d",&t);
	for(int test=1;test<=t;++test)
	{
		string s;
		int k,ans=0;
		cin>>s>>k;
		for(int i=0;i<s.length();++i)
		{
			if(s[i]=='+') continue;
			else
			{
				ans++;
				if((s.length()-i)>=k)
				{
					s[i]='+';
					for(int j=1;j<k;++j)
					{
						s[i+j]=(s[i+j]=='+')?'-':'+';
					}
				}
				//cout<<s<<"\n";
			}
		}
		bool possible=true;
		for(int i=0;i<s.length();++i)
		{
			if(s[i]=='-')
			{
				possible = false;
				break;
			}
		}
		if(possible)
		printf("Case #%d: %d\n",test,ans);
		else
		printf("Case #%d: IMPOSSIBLE\n",test);
			
	}	
	return 0;
}

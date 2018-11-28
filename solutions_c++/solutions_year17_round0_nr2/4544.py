#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int cnt=1;
	while(t--)
	{
		long long int n=0,num=0;
		string s;
		cin>>s;
		//scanf("%lld",&n);
		long long digless=0;
		int flag=0;

		//printf("%d\n",s.length() );
		for(int i=0;i<s.length()-1;i++)
		{
			digless=digless*10+9;
			if(s[i]-'0' > s[i+1]-'0')
				flag=1;
			n=n*10+(s[i]-'0');
		}
		n=n*10+(s[s.length()-1]-'0');
		int only9=0;
		s[s.length()]='9';
		int pt=0;
		for(int i=0;i<s.length()-1;i++)
		{
			if(s[i]>s[i+1])
			{
				pt=i;
				break;
			}
		}
		int i=pt;
		while(i!=0)
		{
			if(s[i]-'0'-1>=s[i-1]-'0')
				break;
			i--;
		}
		for(int j=0;j<i;j++)
		{
			num=num*10+s[j]-'0';
		}
		num=num*10+(s[i]-'0'-1);
		for(int j=i+1;j<s.length();j++)
		{
			num=num*10+9;
		}
		if(flag==1)
			n=0;
		printf("Case #%d: %lld\n",cnt++,max(n,max(num,digless)) );
	}
	return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		string s;
		int k;
		cin>>s;
		cin>>k;
		int count=0;
		int len=s.length();
		for(int i=0;i<=len-k;i++)
		{
			if(s[i]=='+')
				continue;
			for(int j=i;j<i+k;j++)
			{
				if(s[j]=='-')
					s[j]='+';
				else
					s[j]='-';
				
			}
			count++;
		}
		bool flag=false;
		for(int i=0;i<len;i++)
		{
			if(s[i]=='-')
				flag=true;
		}
		if(flag)
			cout<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<endl;
			
		else
			cout<<"Case #"<<z<<": "<<count<<endl;
	}
	return 0;
}

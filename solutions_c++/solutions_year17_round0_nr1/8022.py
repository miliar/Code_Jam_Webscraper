#include<iostream>
#include<string>
using namespace std;
int main()
{
	int i,t,k,j,l;
	string s;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>s>>k;
		int count = 0;
		int flag = 0;
		for(j=0;j<s.size();j++)
		{
			if((j+k)<=s.size())
			{
				if(s[j]=='+')
					continue;
				else if(s[j]=='-')
				{
					count++;
					for(l=j;l<(j+k);l++)
					{
						if(s[l]=='-')
							s[l] = '+';
						else if(s[l]=='+')
							s[l] = '-';
					}
				}
			}
			else
			{
				for(l=j;l<s.size();l++)
				{
					if(s[l]=='-')
					{
						flag = 1;
						break;
					}	
				}
				break;
			}
		}
		if(flag==1)
			cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<i<<": "<<count<<endl;
	}
	return 0;
}
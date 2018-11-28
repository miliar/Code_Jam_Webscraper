#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s1;
	int t,ans=0,flag=0,k,l1,i,j,z;
	cin>>t;
	for( i=1;i<=t;i++)
	{
		ans=0;
		flag=0;
		cin>>s1>>k;
		l1=s1.length();
		for( j=0;j<l1;j++)
		{
			if(j+k<=l1)
			{
				if(s1[j]=='-')
				{
					ans++;
					for(z=j;z<j+k;z++)
					{
						if(s1[z]=='+')
						s1[z]='-';
						else
						s1[z]='+';
					}
				}
			}
			else
			break;
		}
		for(j=0;j<l1;j++)
		{
			if(s1[j]=='-')
			{
				flag=1;
				break;
			}
		}
		if(flag)
		{
			cout<<"Case #"<<i<<": IMPOSSIBLE\n";
		}
		else
		cout<<"Case #"<<i<<": "<<ans<<"\n";
	}
	return 0;
}

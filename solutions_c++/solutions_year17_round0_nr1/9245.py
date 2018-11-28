#include <bits/stdc++.h>
using namespace std;
int main() 
{ 
	long long t,k,i,j,c,flag,z,l;string s;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		cin>>s;
		cin>>k;
		c=0;
		l=s.size();
		flag=0;
		for(i=0;i<=l-k;i++)
		{
			if(s[i]=='-')
			{
				c++;
				for(j=i;j<i+k;j++)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
				}
			}
		}
		for(i=0;i<l;i++)
		{
			if(s[i]=='-')
			{
				flag=1;
				break;
			}
		}
		printf("Case #%lld: ",z);
		if(flag)
			cout<<"IMPOSSIBLE";
		else
			cout<<c;
		cout<<endl;
	}
	return 0;
}

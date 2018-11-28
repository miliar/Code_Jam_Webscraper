#include <bits/stdc++.h>
using namespace std;
int main() 
{ 
	long long t,k,i,j,c,flag,x,l;string s;
	cin>>t;
	for(x=1;x<=t;x++)
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
		cout<<"Case #"<<x<<": ";
		if(flag)
			cout<<"IMPOSSIBLE";
		else
			cout<<c;
		cout<<endl;
	}
	return 0;
}

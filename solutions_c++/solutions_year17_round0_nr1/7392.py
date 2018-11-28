#include<bits/stdc++.h>
#define li long long int
#define S string
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A_large_out.txt","w",stdout);
	li t;
	cin>>t;
	for(li z=1;z<=t;z++)
	{
		S s;
		li count=0,k,i;
		cin>>s>>k;
		li len=s.length();
		len=len-k+1;
		for(i=0;i<len;i++)
		{
			if(s[i]=='-')
			{
				li j=0;
				while(j<k)
				{
					if(s[i+j]=='+')
						s[i+j]='-';
					else
						s[i+j]='+';
					j++;		
				}
				count++;
			}
		}
		//cout<<s<<endl;
		for(i=0;i<s.length();i++)
			if(s[i]=='-')
			{
				cout<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<endl;
				break;
			}
		if(i==s.length())	
			cout<<"Case #"<<z<<": "<<count<<endl;	
	}
	return 0;
}

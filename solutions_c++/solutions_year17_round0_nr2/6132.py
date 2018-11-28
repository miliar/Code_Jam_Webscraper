#include<bits/stdc++.h>
using  namespace std;
int main()
{
	int t;
	cin>>t;
	int i1=1;
	while(t--)
	{
		string s;
		cin>>s;
		cout<<"Case #"<<i1<<": ";
		
		
		int i;
		for( i=0;i<s.length()-1;i++)
		{
			if(s[i]-'0'>s[i+1]-'0')
			break;
		}
		if(i==s.length()-1)
		{
			cout<<s<<"\n";
		}
		else
		{
			for(;i>0;i--)
			{
				if(s[i]!=s[i-1])
				break;
			}
			if(s[i]=='1'&&i==0)
			{
				for(int j=0;j<s.length()-1;j++)
				{
					cout<<"9";
				}
				cout<<"\n";
				
			}
			else
			{
			
			s[i]=s[i]-1;
			for(int k=i+1;k<s.length();k++)
			{
				s[k]='9';
				
			}
			cout<<s<<"\n";
		}
			
	}
	i1++;
	}
}

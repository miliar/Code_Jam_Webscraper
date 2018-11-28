#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t,c=1;
	cin>>t;
	while(t--)
	{
		string s;
		cin>>s;
		for(int i=s.length()-1;i>=0;i--)
		{
			if(s[i]<s[i-1])
			{
				s[i-1]=s[i-1]-1;
				for(int j=s.length()-1;j>i-1;j--)
				s[j]='9';
			}
		}
		cout<<"Case #"<<c<<":"<<" ";
		for(int i=0;i<s.length();i++)
		{
			if(i==0)
			{
				if(s[i]=='0')
				continue;
			}
			cout<<s[i];
		}
		cout<<endl;
		c++;
	}
}

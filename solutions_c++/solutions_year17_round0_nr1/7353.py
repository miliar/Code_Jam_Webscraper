#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t,a=1;
	cin>>t;
	while(t--)
	{
		string s;
		int k,c=0;
		cin>>s;
		cin>>k;
		for(int i=0;i<=s.length()-k;i++)
		{
			if(s[i]=='-')
			{
				c++;
				for(int j=0;j<k;j++)
				{
					if(s[i+j]=='-')
					s[i+j]='+';
					else
					s[i+j]='-';
				}
			}
			else
			continue;
		}
		for(int i=s.length()-1;i>=s.length()-k+1;i--)
		{
			if(s[i]=='+')
			continue;
			else
			c=-1;
		}
		cout<<"Case #"<<a<<":"<<" ";
		if(c==-1)
		cout<<"IMPOSSIBLE";
		else
		cout<<c;
		cout<<endl;
		a++;
	}
}

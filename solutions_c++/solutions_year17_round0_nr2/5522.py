#include <iostream>
#include <string>
#include <cmath>
using namespace std;
int main()
{
	int t;
	cin>>t;
	string s;
	for(int i=0;i<t;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		getline(cin>>ws,s);
		int l=s.size();
		for(int p=l-2;p>=0;p--)
		{
			if(s[p]>s[p+1])
			{
				for(int k=p+1;k<=l-1;k++)
				{
					s[k]='9';
				}
			
				
			s[p]=min(s[p]-1-48,s[p+1]-48)+48;}
			
		}
		if(s[0]=='0')
		{
			for(int p=0;p<l-1;p++)
				cout<<9;
			cout<<endl;
		}
		else
		cout<<s<<endl;
	}
}
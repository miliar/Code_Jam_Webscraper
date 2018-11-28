#include<iostream>
using namespace std;
main()
{
	int t;cin>>t;
	for(int j=1;j<=t;j++)
	{
		string s;cin>>s;
		bool flag=false,e=false;
		for(int i=1;i<s.size();i++)
		{
			if(!flag&&s[i-1]>s[i])
			{
				flag=true;
				while(i>0&&s[i]<=s[i-1])i--;
				s[i]--;
			}
			else if(flag)s[i]='9';
		}
		cout<<"Case #"<<j<<": ";
		if(s[0]=='0')
		{
			for(int i=1;i<s.size();i++)cout<<s[i];
			cout<<endl;
		}
		else cout<<s<<endl;
	}
}

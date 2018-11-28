#include <iostream>
using namespace std;
int main()
{
	int t,n;
	ios::sync_with_stdio(false);
	cin>>t;
	for(int iii=1;iii<=t;iii++)
	{
		string s;
		cin>>s;
		int len=s.length();
		int i;
		for(i=1;i<len;i++)
		{
			if(s[i-1]>s[i])
				break;
		}
		if(i==len)
		{
			cout<<"Case #"<<iii<<": "<<s<<'\n';
			continue;
		}

		if(i>=2&&s[i-2]==s[i-1])
		{
			char c=s[i-1];
			int ii=i-1;
			while(ii>=0)
			{
				if(ii==0)
					s[ii]=c-1;	
				else if(s[ii]==c&&ii>0&&s[ii-1]==c)
					s[ii]='9';
				else
				{
					s[ii]=c-1;	
					break;
				}
				ii--;
			}
		}
		else
			s[i-1]-=1;
		for(;i<len;i++)
			s[i]='9';
		bool flag=false;
		cout<<"Case #"<<iii<<": ";
		for(int i=0;i<len;i++)
		{
			if(s[i]!='0')
				flag=true;
			if(s[i]=='0'&&!flag)
				continue;
			cout<<s[i];
				
		}
		cout<<'\n';


	}
	return 0;
}

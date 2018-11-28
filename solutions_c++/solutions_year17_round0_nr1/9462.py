#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string s;
		int k;
		cin>>s>>k;
		int count=0;
		for(int j=0;j<s.length()-k+1;j++)
		{
			if(s[j]!='+')
			{
				for(int l=0;l<k;l++)
				{
					if(s[j+l]=='+')
						s[j+l]='-';
					else
						s[j+l]='+';
				}
				count++;
			}
		}
		bool flag = true;
		for(int j=s.length()-k+1;j<s.length();j++)
			if(s[j]=='-')
			{
				flag=false;
				break;
			}
		if(flag==false)
			cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}
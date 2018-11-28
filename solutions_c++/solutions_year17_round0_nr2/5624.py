#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int cas=1;
	while(t--)
	{
		string s;
		cin>>s;
		int p;
		cout<<"Case #"<<cas<<": ";
		bool check=false;
		for(int i=0;i<s.size()-1;i++)
		{
			if(s[i+1]<s[i])
			{
				p=i;
				check=true;
				break;
			}
		}
		if(check)
		{
			if(s[p]-1=='0')
			{
				for(int i=0;i<s.size()-1;i++)
				{
					cout<<'9';
				}
				cout<<endl;
			}
			else
			{
				int x=int(s[p]);
				int j;
				for(j=p;j>=0;)
				{
					if(s[j]==x)
					{
						p=j;
						j--;
					}
					else
						break;
				}
				s[p]=s[p]-1;
				for(j=p+1;j<s.size();j++)
					s[j]='9';
				cout<<s<<endl;
			}
		}
		else
			cout<<s<<endl;
		cas++;
	}
}

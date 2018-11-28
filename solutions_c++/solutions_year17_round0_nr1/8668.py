#include<iostream>
using namespace std;
int main()
{
int t,loop=1;
cin>>t;
while(t--)
	{
	string str;
	cin>>str;
	int k;
	cin>>k;
	int i=0,l=str.length();
	int count=0;
	cout<<"Case #"<<loop<<": ";
	while(i+k<=l)
		{
		if(str[i]=='-')
			{
			for(int j=i;j<i+k;j++)
				if(str[j]=='+')
					str[j]='-';
				else
					str[j]='+';
			count++;
			}
			++i;
		}
	i=0;
	bool c=false;
	while(i<l)
		{
		if(str[i]=='-')
			{
			c=true;
			break;
			}
		++i;
		}
	if(c)
		cout<<"IMPOSSIBLE\n";
	else
		cout<<count<<'\n';
	++loop;
	}
return 0;
}
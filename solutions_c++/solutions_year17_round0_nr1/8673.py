#include<iostream>
using namespace std;
int main()
{
int t;
cin>>t;
for(int x=1;x<=t;++x)
	{
	string str;
		bool check=false;
	cin>>str;
	int k;
	cin>>k;
	int i=0,l=str.length();
	int count=0;
	cout<<"Case #"<<x<<": ";
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

	while(i<l)
		{
		if(str[i]=='-')
			{
			check=true;
			break;
			}
		++i;
		}
	if(check)
		cout<<"IMPOSSIBLE\n";
	else
		cout<<count<<'\n';
	}
return 0;
}
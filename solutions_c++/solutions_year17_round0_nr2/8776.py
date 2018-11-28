#include<iostream>
using namespace std;
int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
	{
	string str;
	cin>>str;
	int l=str.length();
	cout<<"Case #"<<i<<": ";
	if(l==1)
		cout<<str;
	else
		{
		l-=2;
		bool check=false;
		while(l>=0)
			{
			if(str[l]>str[l+1])
				{
				str[l+1]='9';
				str[l]-=1;
				check=true;
				}
			else if(str[l+1]=='0')
				{
				str[l+1]='9';
				check=true;
				}
			--l;
			}
		if(check)
			{
			str[str.length()-1]='9';
			}
		
		if(str[0]=='0')
			str.erase(str.begin(),str.begin()+1);
		cout<<str;
		}
	cout<<'\n';
	}
	return 0;
}
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
	int len=str.length();
	cout<<"Case #"<<i<<": ";
	if(len==1)
		cout<<str;
	else
		{
		bool c=false;
		len=len-2;
		while(len>=0)
			{
			if(str[len]>str[len+1])
				{
				str[len+1]='9';
				str[len]-=1;
				c=true;
				}
			else if(str[len+1]=='0')
				{
				str[len+1]='9';
				c=true;
				}
			--l;
			}
		if(c)
			str[str.length()-1]='9';
		if(str[0]=='0')
			str.erase(str.begin(),str.begin()+1);
		cout<<str;
		}
	cout<<endl;
	}
	return 0;
}
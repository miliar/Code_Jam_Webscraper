#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int x=0;
	while(t--)
	{
		string s;
		cin>>s;
		int k,f=0,flag=0;
		cin>>k;
		for(int i=0;i<=(s.length()-k);i++)
		{
			if(s[i]=='-')
			{
				for(int j=i;j<(i+k);j++)
				{
					if(s[j]=='-')
					s[j]='+';
					else
					s[j]='-';
				}
				f++;
			}
		}
		for(int i=(s.length()-k+1);i<s.length();i++)
		{
			if(s[i]=='-')
			{
				flag=1;
				break;
			}
		}
		x++;
		if(flag==0)
		cout<<"Case #"<<x<<": "<<f<<"\n";
		else
		cout<<"Case #"<<x<<": IMPOSSIBLE\n";
	}
	return 0;
}

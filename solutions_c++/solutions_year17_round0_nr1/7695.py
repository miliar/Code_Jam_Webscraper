#include<iostream>
#include<string>
using namespace std;
string a;
int main()
{
	int t;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		int k,c=0,ch=0;
		cin>>a>>k;
		for(int i=0;i<a.size();i++)
		{
			if(a[i]=='-'&&i+k-1<a.size())
			{
				for(int j=0;j<k;j++)
				{
					if(a[i+j]=='+')
						a[i+j]='-';
					else a[i+j]='+';
				}
				c++;
			}
			if(a[i]=='-')
				ch=1;
		}
		if(ch)
			cout<<"Case #"<<p<<": "<<"IMPOSSIBLE\n";
		else cout<<"Case #"<<p<<": "<<c<<"\n";
	}
}
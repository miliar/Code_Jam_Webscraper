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
		cin>>a;
		for(int i=(int)a.size()-1;i>=0;i--)
		{
			if(i-1>=0)
			{
				if(a[i-1]>a[i])
				{
					a[i-1]--;
					for(int j=i;j<a.size();j++)
					a[j]='9';
				}
			}
		}
		while(a[0]=='0')
		{
			a.erase(a.begin());
		}
		cout<<"Case #"<<p<<": "<<a<<"\n";
	}
}
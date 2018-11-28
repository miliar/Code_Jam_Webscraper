#include <bits/stdc++.h>
using namespace std;
bool izi(string a)
{
	for(long long i=0;i<a.size()-1;i++)
	{
		if(a[i]>a[i+1])return false;
	}
	return true;
}
string sc(string a)
{
	for(long long i=0;i<a.size();i++)
	{
		if(a[i]!='0')return a.substr(i);
	}
	return "0";
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B_out.txt","w",stdout);
	long long t;
	cin>>t;
	for(long long tt=1;tt<=t;tt++)
	{

		string a;
		cin>>a;
		cout<<"Case #"<<tt<<": ";
		if(izi(a))cout<<a<<endl;
		else
		{
			while(izi(a)!=true)
			{
				for(long long i=0;i<a.size()-1;i++)
				{
					if(a[i]>a[i+1])
					{
						a[i]--;
						for(long long j=i+1;j<a.size();j++)
						{
							a[j]='9';
						}
						break;
					}
				}
			}
			cout<<sc(a)<<endl;
			//cout<<a<<endl;
		}


	}
}
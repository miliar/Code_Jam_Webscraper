#include <iostream>
#include <string>
using namespace std;
string reverse (string a,int k)
{
	for (int z =0;z<k;z++)
	{
		if(a[z]=='+')
		{
			a[z] = '-';
		}
		else 
		{
			a[z] = '+';
		}
	}
	return a;
}
string flip(string a,int k,string l)
{
	int s = a.size();
	int x = a.find("-");
	if (x == string::npos)
	{
		return l;
	}
	else if ((s-x)>=k)
	{
		return flip((reverse(a.substr(x),k)),k,(l + "+"));
	}
	else 
	{
		l = "IMPOSSIBLE";
		return l;
	}
}
int main()
{
	int t;
	cin>>t;
	for (int z=0;z<t;z++)
	{
		string a;
		int k;
		cin>>a>>k;
		string l = "";
		string as = flip(a,k,l);
		if (as=="IMPOSSIBLE")
		{
			cout<<"Case #"<<(z+1)<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<(z+1)<<": "<<as.size()<<endl;
		}
	}
}
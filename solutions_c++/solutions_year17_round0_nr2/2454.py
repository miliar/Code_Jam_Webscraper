#include <iostream>
#include <string>
#include <cmath>
using namespace std;
unsigned long long int stoi (const string &s)
{
	unsigned long long int x = 0;
	unsigned long long int dummy = 48;
	int size = s.size();
	int i =0;
	while (size != 0)
	{
		x = x + ((s[i]-dummy)*pow(10,(size-1)));
		i++;
		size--;
	}
	return x;
}
string reverse (string a)
{
	string b;
	int i = (a.size()-1);
	while(i >= 0)
	{
		b.push_back(a[i]);
		i--;
	}
	return b;
}
string itos(unsigned long long int a)
{
	string x;
	while (a!=0)
	{
		int l = a%10;
		char c = l + 48;
		x.push_back(c);
		a = a/10;
	}
	return reverse(x);
}
string make (int a)
{
	string x = "";
	while(a!=0)
	{
		x = x + "9";
		a--;
	}
	return x;
}
string check (string a,int k)
{
	if ((a[0]-48)>=k)
	{
		if (a.size() == 1)
		{
			return a;
		}
		else
		{
			string champu = (check(a.substr(1),(a[0]-48)));
			if (champu == "false")
			{
				if ((a[0]-k) == 48)
				{
					string aaa = "false";
					return aaa;
				}
				else
				{
					return ((itos(a[0] - 49)+make(a.size()-1)));
				}
			}
			else
			{
				return ((itos(a[0]-48))+champu);
			}
		}
	}
	else 
	{
		string aaa = "false";
		return aaa;
	}
}
string ans (string n)
{
	string a = check(n,1);
	if (a=="false")
	{
		return (make(n.size()-1));
	}
	else 
	{
		return a;
	}
}
int main()
{
	int t;
	cin>>t;
	for (int z=0;z<t;z++)
	{
		string n;
		cin>>n;
		cout<<"Case #"<<(z+1)<<": "<<(ans(n))<<endl;
	}
}
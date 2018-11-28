#include <iostream>
#include <string>
using namespace std;
int count=0;
void mods(string &s)
{
	while(true)
		{
			if(s.find("+")==0)
				s.erase(0,1);
			else break;
		}
		return;
}
void result(string &s,int k)
{
	mods(s);
	if(s.size()==0) 
	{
		cout<<count<<endl;
		return;
	}
	else
	{
		if(s.size()<k) 
		{
			cout<<"IMPOSSIBLE"<<endl;
			return;
		}
		else
		{
			for(int i=0;i<k;i++)
			{
				if(s[i]=='+') s[i]='-';
					else s[i]='+';
			}
			count++;
			result(s,k);
		}
	}

}
int main()
{
	int t;
	cin>>t;
	string s;
	int k;
	for(int i=0;i<t;i++)
	{
		cin>>s>>k;
		count=0;
		cout<<"Case #"<<i+1<<": ";
		result(s,k);

	}
}
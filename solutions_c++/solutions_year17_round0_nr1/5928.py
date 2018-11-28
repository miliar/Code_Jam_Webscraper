#include <iostream>
using namespace std;
string change(string s, int l, int k, bool* check)
{
	//cout<<l<<" "<<k<<"\n";
	while(k--&&(*check))
	{
	//	cout<<l<<" "<<k<<"\n";
		if(l<0)
		{
			*check = false;
			return s;
		}
		if(s[l]=='+')
			s[l] = '-';
		else
			s[l] = '+';
		l--;
	}
	return s;
}
int main() {
	int n;
	cin>>n;
	int co = 1;
	while(n--)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		char set = '+';
		int len = s.length();
		int i = 0, count = 0;
		len--;
		bool res = true;
		while(len>=0&&res)
		{
			if(s[len]==set)
				len--;
			else
			{
				count++;
				s = change(s,len,k,&res);
				//cout<<"1<<"<<s<<"\n";
				len--;
			}
		}
		//cout<<s<<"\n";
		if(res)
			cout<<"Case #"<<co<<": "<<count<<"\n";
		else
			cout<<"Case #"<<co<<": IMPOSSIBLE\n";
		co++;
	}
	return 0;
}
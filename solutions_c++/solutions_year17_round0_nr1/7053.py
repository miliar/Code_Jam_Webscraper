#include <iostream>
using namespace std;
string fun(string s, int l, int k, bool* check)
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
	int n1;
	cin>>n1;
	int coo = 1;
	while(n1--)
	{
		string str;
		cin>>str;
		int k;
		cin>>k;
		char set = '+';
		int len = str.length();
		int i = 0, count = 0;
		len--;
		bool res = true;
		while(len>=0&&res)
		{
			if(str[len]==set)
				len--;
			else
			{
				count++;
				str = fun(str,len,k,&res);
				len--;
			}
		}
		if(res)
			cout<<"Case #"<<coo<<": "<<count<<"\n";
		else
			cout<<"Case #"<<coo<<": IMPOSSIBLE\n";
		coo++;
	}
	return 0;
}
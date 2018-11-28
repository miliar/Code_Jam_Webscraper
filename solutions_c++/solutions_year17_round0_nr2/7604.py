#include <bits/stdc++.h>
using namespace std;

string zamien(string s)
{
	string ret;
	bool czy = false;
	ret.push_back(s[0]);
	for(int i = 1 ; i < s.size() ; i++)
	{
		if(s[i] < s[i - 1] && czy == false)
		{
			ret.back()--;
			czy = true;
		}
		if(czy)
			ret.push_back('9');	
		else
			ret.push_back(s[i]);
	}
	
	if(ret[0] == '0')
	{
		string ret2;
		for(int i = 1 ; i < ret.size() ; i++)
			ret2.push_back(ret[i]);
		return ret2;
	}	
	else
		return ret;
}

string solve()
{
	string s;
	cin >> s;
	int xd = 0;
	string poprz = "##!@#$!@#$";
	while(poprz != s)
	{
		poprz = s;
		s = zamien(s);
	}
	return s;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1 ; i <= t ; i++)
		cout << "Case #" << i << ": " << solve() << "\n";
}

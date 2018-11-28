#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>

using namespace std;

#define INF 1000000000
#define double long double
#define ll long long

bool IsAscending(const string &s)
{
	for(int i=1; i<s.size(); i++)
		if(s[i-1] > s[i])
			return false;
	return true;
}

ll GetLastAscending(string &s)
{
	if(IsAscending(s))
		return stoll(s);
	for(int i=s.size()-1; i>0; i--)
	{
		s[i] = '9';
		if(s[i-1]==0)
			continue;
		s[i-1]--;
		
		
		if(IsAscending(s))
			return stoll(s);
	}
}

int main()
{
	int T;
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		string s;
		cin >> s;
		
		ll ans = GetLastAscending(s);
		cout << "Case #"<< t << ": " << ans << endl;
	}
	
	return 0;
}


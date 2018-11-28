#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>

using namespace std;

#define INF 1000000000
#define double long double
#define ll long long
#define endl '\n'

void Flip(string &s, int from, int k)
{
	for(int i=from; k>0; i++, k--)
		s[i] = (s[i]=='+')?'-':'+';
}

bool CheckDone(string &s, int k)
{
	for(int i=s.size()-k; i<s.size(); i++)
		if(s[i]=='-')
			return false;
	return true;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		int k;
		string s;
		cin >> s >> k;
		
		
		int ans = 0;
		for(int i=0; i<=s.size()-k; i++)
			if(s[i]=='-')
			{
				Flip(s,i,k);
				ans++;
			}
		
		//
//		cout << "final : " << s << endl;
		
		cout << "Case #"<< t << ": ";
		if(CheckDone(s,k))
			cout << ans << endl;
		else
			cout << "IMPOSSIBLE\n";
	}
	return 0;
}


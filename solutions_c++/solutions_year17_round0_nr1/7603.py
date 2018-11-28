#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;

int solve(string s, int k)
{
	int res = 0;
	for(int i = 0; i < s.size(); i++)
	{
		if(s[i] == '-')
		{
			res++;
			if(i + k > s.size())
				return -1;
			for(int j = 0; j < k; j++)
				s[i + j] = (s[i + j] == '+') ? '-' : '+';
			//cout << s << endl;
		}
	}
	return res;

}


int main() 
{
	freopen ("A-large.in","r", stdin);
	freopen ("A.out","w",stdout);
	string s, rs;
	int tt, k, res;
	cin >> tt;
	for(int t = 1; t <= tt; t++)
	{

		cin >> s >> k;
		
		
		int res1 = solve(s, k);
		reverse(s.begin(), s.end());
		int res2 = solve(s, k);

		res = min(max(res1, 0), max(res2, 0));
		cout << "Case #" << t << ": ";
		if(res1 == -1 and res2 == -1)
			cout << "IMPOSSIBLE";
		else
			cout << res;
		cout << endl;
	}
	return 0;
}
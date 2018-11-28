#include <iostream>
#include <string>
#include <vector>
#include <queue> 
#include <algorithm>
using namespace std;

#define FOR(i,n) for(int i=0; i<n; i++)

string s;
long long dp[20][10][2];

long long solve(int idx, int last, bool ok)
{	
	if (dp[idx][last][ok] != -1) return dp[idx][last][ok];
	if (idx == 0)
	{
		if (ok)
			return min(s[idx] - '0', last);
		else
			return min(s[idx] -1 - '0', last);
	}
	long long mx = 0;
	for (int i = last; i >= 0; i--)
	{
		if (i < s[idx]-'0')
			mx = max(mx, 10*solve(idx - 1, i, 1)+i);
		else if (i > s[idx] - '0')
			mx = max(mx, 10*solve(idx - 1, i, 0)+i);
		else 
			mx = max(mx, 10 * solve(idx - 1, i, ok) + i);
	}
	return dp[idx][last][ok] = mx;	
}



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc; cin >> tc;
	FOR(k, tc)
	{
		memset(dp, -1, sizeof dp);	cin >> s;
		long long sol = solve(s.length() - 1, 9, 1);
		cout << "Case #"<<k+1<<": "<< sol << endl;
	}
	return 0;
}

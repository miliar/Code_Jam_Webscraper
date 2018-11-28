#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve()
{
	int N, P;
	cin >> N >> P;
	vector<int> grps(N);
	for(auto &x : grps) cin >> x;

	vector<int> rem(4);
	for(auto &x : grps) rem[x % P]++;
	
	int res = rem[0];
	int dp[101][101][101] = {};

	for(int a = 0; a <= rem[1]; ++a)
	for(int b = 0; b <= rem[2]; ++b)
	for(int c = 0; c <= rem[3]; ++c)
	{
		if(a > 0)
			dp[a][b][c] = max(dp[a][b][c], dp[a-1][b][c] + ((a-1 + b * 2 + c * 3) % P == 0));
		if(b > 0)
			dp[a][b][c] = max(dp[a][b][c], dp[a][b-1][c] + ((a + (b-1) * 2 + c * 3) % P == 0));
		if(c > 0)
			dp[a][b][c] = max(dp[a][b][c], dp[a][b][c-1] + ((a + b * 2 + (c-1) * 3) % P == 0));
	}

	cout << rem[0] + dp[rem[1]][rem[2]][rem[3]] << "\n";
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
}

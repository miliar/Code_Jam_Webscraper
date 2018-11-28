#include <iostream>
#include <vector>
#include <cstring>

int cur_step = 0;

int memo[101][101][101][4][3];

int dp(int a1, int a2, int a3, int rest, int mod)
{
	if(a1 + a2 + a3 == 0)
		return 0;
	int &ans = memo[a1][a2][a3][rest][mod - 2];
	if(ans != -1)
		return ans;
	ans = 0;
	if(a1)
		ans = std::max(ans, dp(a1 - 1, a2, a3, (rest + 1) % mod, mod));
	if(a2)
		ans = std::max(ans, dp(a1, a2 - 1, a3, (rest + 2) % mod, mod));
	if(a3)
		ans = std::max(ans, dp(a1, a2, a3 - 1, (rest + 3) % mod, mod));
	if(rest == 0)
		ans++;
	return ans;
}

int main()
{
	int t;
	std::cin >> t;
	memset(memo, -1, sizeof memo);
	for(int te = 1; te <= t; te++)
	{
		int n, m;
		std::cout << "Case #" << te << ": ";
		cur_step++;
		std::cin >> n >> m;
		std::vector<int> a(3, 0);
		int ans = 0;
		while(n--)
		{
			int temp;
			std::cin >> temp;
			temp %= m;
			if(temp == 0)
				ans++;
			else
				a[temp - 1]++;
		}
		std::cout << ans + dp(a[0], a[1], a[2], 0, m) << '\n';
	}
}

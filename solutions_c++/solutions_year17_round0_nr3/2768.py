#include <iostream>
#include <cstdio>

using namespace std;

int t;
long long n, k;
pair < long long, long long > ans;

pair < long long, long long > solve(long long n, long long k)
{
	if (n % 2) {
		if (k == 1)
			return make_pair(n / 2, n / 2);
		return solve(n / 2, k / 2);
	} else {
		if (k == 1)
			return make_pair(n / 2, n / 2 - 1);
		if (k % 2)
			return solve(n / 2 - 1, k / 2);
		return solve(n / 2, k / 2);
	}
}


int main()
{
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	cin >> t;
	
	for (int l = 0; l < t; l++) {
		cin >> n >> k;
		ans = solve(n, k);
		
		cout << "Case #" << l + 1 << ": ";
		cout << ans.first << ' ' << ans.second;
		cout << endl;		
	}
	
	
	return 0;
}

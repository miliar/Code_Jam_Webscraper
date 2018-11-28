#include <bits/stdc++.h>
#define f(x, y, z) for(int x = (y); x <= (z); ++x)
#define g(x, y, z) for(int x = (y); x < (z); ++x)
#define h(x, y, z) for(int x = (y); x >= (z); --x)
using namespace std;

int p;
struct state
{
	int a[7]; 
	state(){memset(a, 0, sizeof(a));}
};
inline bool operator <(const state &x, const state &y)
{
	g(i, 0, p) if(x.a[i] != y.a[i]) return x.a[i] < y.a[i];
	return false;
}

map<state, int> _dp;
int dp(state s)
{
	if(_dp.find(s) != _dp.end()) return _dp[s];
	int &ans = _dp[s];
	ans = 0;
	bool empty = true;
	g(i, 1, p) if(s.a[i]) empty = false;
	if(empty) return ans = 0;
	g(i, 1, p) if(s.a[i])
	{
		state t = s;
		--t.a[i]; t.a[0] = (t.a[0] - i + p) % p;
		ans = max(ans, dp(t) + !s.a[0]);
	}
	return ans;
}

int main()
{
	int T; cin >> T;
	f(_, 1, T)
	{
		_dp.clear();
		int n; cin >> n >> p;
		state s;
		int ans = 0;
		while(n--)
		{
			int x; cin >> x;
			x %= p;
			if(!x) ++ans;
			else ++s.a[x];
		}
		printf("Case #%d: %d\n", _, ans + dp(s));
	}
	return 0;
}

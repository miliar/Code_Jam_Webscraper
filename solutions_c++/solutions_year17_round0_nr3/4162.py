// https://code.google.com/codejam/contest/3264486/dashboard#s=p2
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <iostream>
#include <functional>
#include <algorithm>
#include <iterator>
#include <cmath>
#include <queue>

using namespace std;

typedef long long ll;

pair<ll,ll> solve(ll N, ll K)
{
	pair<ll, ll> ans;
	priority_queue<ll> q;
	q.push(N);
	while (K > 0) {
		K--;
		ll n = q.top(); q.pop();
		if (n % 2 == 0) {
			n /= 2;
			ans = make_pair(n, n - 1);
		} else {
			n /= 2;
			ans = make_pair(n, n);
		}
		q.push(ans.first);
		q.push(ans.second);
	}
	return ans;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		ll N, K;
		cin >> N >> K;
		auto ans = solve(N, K);
		cout << "Case #" << (t + 1) << ": " << ans.first << " " << ans.second << endl;
	}
	return 0;
}

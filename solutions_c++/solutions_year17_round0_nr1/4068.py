// https://code.google.com/codejam/contest/3264486/dashboard#s=p0
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <iostream>
#include <functional>
#include <algorithm>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdint>

using namespace std;

typedef long long ll;

vector<bool> trim(const vector<bool>& bits)
{
	int i = 0;
	int j = (int)bits.size();
	for (; i < j; i++) {
		if (!bits[i])
			break;
	}
	for (; j > i; j--) {
		if (!bits[j-1])
			break;
	}
	vector<bool> ret;
	for (int k = i; k < j; k++)
		ret.push_back(bits[k]);
	return ret;
}

ll solve(const vector<bool>& s, int K)
{
	auto S = trim(s);
	static map<pair<vector<bool>, int>, ll> memo;
	auto mit = memo.find(make_pair(S, K));
	if (mit != memo.end())
		return mit->second;

	ll ans = 0;
	auto it = find(S.begin(), S.end(), false);
	if (it == S.end())
		return 0;
	vector<bool> B(it, S.end());
	if ((int)B.size() < K)
		return -1;
	for (auto it = B.begin(); it != B.begin() + K; ++it) {
		*it = !*it;
	}
	ans = solve(B, K);
	memo[make_pair(S, K)] = (ans < 0) ? ans : ans + 1;
	return memo[make_pair(S, K)];
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string S;
		int K;
		cin >> S >> K;
		vector<bool> bit;
		for (auto i : S) {
			bit.push_back(i == '+');
		}
		auto ans = solve(bit, K);
		cout << "Case #" << t << ": " << ((ans < 0) ? "IMPOSSIBLE" : to_string(ans)) << endl;
	}
	return 0;
}

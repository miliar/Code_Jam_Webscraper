#include<bits/stdc++.h>
/*
*/

using namespace std;

typedef pair < pair<long long int, long long int>, pair < long long int, long long int >>status;

long long int calc() {
	long long int Hd, Ad, Hk, Ak, B, D;
	cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
	map<status, long long int>dp;
	queue<status>que;
	dp[make_pair(make_pair(Hd, Ad), make_pair(Hk, Ak))] = 0;
	que.push(make_pair(make_pair(Hd, Ad), make_pair(Hk, Ak)));
	long long int ans = LLONG_MAX / 6;
	while (que.size()) {
		auto now = que.front(); que.pop();
		if (ans <= dp[now]+1)
		{
			continue;
		}
		{
			auto next = now;
			next.second.second -= D;
			if (next.second.second < 0)
			{
				next.second.second=0;
			}
			next.first.first -= next.second.second;
			if (next.first.first > 0 && (dp.count(next) == 0 || dp[next] > dp[now] + 1))
			{
				dp[next] = dp[now] + 1;
				que.push(next);
			}
		}
		{
			auto next = now;
			next.first.first = Hd;
			next.first.first -= next.second.second;
			if (next.first.first > 0 && (dp.count(next) == 0 || dp[next] > dp[now] + 1))
			{
				dp[next] = dp[now] + 1;
				que.push(next);
			}
		}
		{
			auto next = now;
			next.second.first -= next.first.second;
			if (next.second.first <= 0)
			{
				ans = min(ans, dp[now] + 1);
			}
			next.first.first -= next.second.second;
			if (next.first.first > 0 && (dp.count(next) == 0 || dp[next] > dp[now] + 1))
			{
				dp[next] = dp[now] + 1;
				que.push(next);
			}
		}
		{
			auto next = now;
			next.first.second += B;
			next.first.first -= next.second.second;
			if (next.first.first > 0 && (dp.count(next) == 0 || dp[next] > dp[now] + 1))
			{
				dp[next] = dp[now] + 1;
				que.push(next);
			}
		}
	}
	return ans;
}

int main() {
	long long int casenum;
	cin >> casenum;
	for (size_t index = 0; index < casenum; index++)
	{
		long long int ans = calc();
		cout << "Case #" << index + 1 << ": ";
		if (ans == LLONG_MAX/6)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			cout << ans << endl;
		}
	}
}

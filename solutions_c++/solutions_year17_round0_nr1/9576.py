#define scan(x) do{while((_n=getchar())<45);if(_n-45)x=_n;else x=getchar();for(x-=48;47<(_=getchar());x=(x<<3)+(x<<1)+_-48);if(_n<46)x=-x;}while(0)
char _, _n;

#include <iostream>
#include <set>
#include <string>
#include <queue>
#define inf 0x3f3f3f3f
using namespace std;

set<string> dp;

bool happy(string S) {
	for (int i = 0; i < S.size(); i++) {
		if (S[i] == '-')
			return 0;
	}
	return 1;
}

int bfs(string S, int K) {
	if (happy(S))
		return 0;
	int diff = (S.size() - K) + 1, ans = inf;
	queue<pair<string, int>> q;
	dp.insert(S);
	q.push(make_pair(S, 0));
	while (!q.empty()) {
		int x = q.front().second;
		S = q.front().first, q.pop();
		for (int i = 0; i < diff; i++) {
			string s = S;
			for (int j = i; j < i + K; j++) {
				if (S[j] == '+')
					s[j] = '-';
				else s[j] = '+';
			}
			if (dp.find(s) == dp.end()) {
				if (happy(s) && x + 1 < ans)
					ans = x + 1;
				dp.insert(s);
				q.push(make_pair(s, x + 1));
			}
		}
	}
	return ans;
}

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	for (int test = 1; test <= T; test++) {
		dp.clear();
		string S;
		int K;
		cin >> S >> K;
		cout << "Case #" << test << ": ";
		int ans = bfs(S, K);
		if (ans != inf)
			cout << ans << '\n';
		else cout << "IMPOSSIBLE\n";
	}
	return 0;
}

#include <bits/stdc++.h>

using ll = long long;
using ull = unsigned long long;
using std::cout;
using std::cin;

void solve(int __T) {
	std::string ans = "";
	int R, O, Y, G, B, V, N;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	std::vector<std::pair<int, char>> cols(6);
	cols[0] = {R, 'R'};
	cols[1] = {O, 'O'};
	cols[2] = {Y, 'Y'};
	cols[3] = {G, 'G'};
	cols[4] = {B, 'B'};
	cols[5] = {V, 'V'};
	ans = std::string(N, '.');
	std::sort(cols.begin(), cols.end());
	if (2 * cols[5].first > N) {
		cout << "Case #" << __T << ": "
			 << "IMPOSSIBLE"
			 << "\n";
		return;
	}
	int index = 0, i = 5, count = 0;
	while (count < N) {
		ans[index] = cols[i].second;
		cols[i].first--;
		if (cols[i].first == 0) {
			i--;
		}
		index = (index + 2) % N;
		if (ans[index] != '.')
			index++;
		count++;
	}
	cout << "Case #" << __T << ": " << ans << "\n";
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		solve(t + 1);
	}
	return 0;
}
/***

6
9 3 0 3 0 3 0
3 2 0 1 0 0 0
6 2 0 2 0 2 0
3 1 0 2 0 0 0
6 2 0 1 1 2 0
4 0 0 2 0 0 2

***/
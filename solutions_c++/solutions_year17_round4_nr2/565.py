#include <fstream>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

const int MAX = 1000;
const int INF = 1e9;

int n, c, m;
int p_cnt[MAX], b_cnt[MAX];

int check(int days) {
	int free = 0, ans = 0;
	for (int i = 0; i < n; ++i) {
		if (p_cnt[i] > days) {
			if (p_cnt[i] - days > free)
				return -1;
			ans += (p_cnt[i] - days);
			free -= (p_cnt[i] - days);
		} else
			free += days - p_cnt[i];
	}
	return ans;
}

pair <int, int> solve() {
	for (int i = 0; i < MAX; ++i)
		p_cnt[i] = b_cnt[i] = 0;
	cin >> n >> c >> m;
	int l = 0, r = INF;
	for (int i = 0; i < m; ++i) {
		int p, b;
		cin >> p >> b;
		++p_cnt[--p], ++b_cnt[--b];
		l = max(l, b_cnt[b] - 1);
	}
	while (l + 1 < r) {
		int f = (l + r) / 2;
		if (check(f) != -1)
			r = f;
		else
			l = f;
	}
	return make_pair(r, check(r));
}

int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		pair <int, int> s = solve();
		cout << "Case #" << i << ": " << s.first << ' ' << s.second << endl;
	}
	cin >> t;
	return 0;
}
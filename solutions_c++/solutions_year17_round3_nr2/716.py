#include <fstream>
#include <queue>

using namespace std;

ifstream cin("input.txt");
ofstream cout("output.txt");

const int MINS = 60 * 24;
const int C = 0;
const int J = 1;
const int F = 2;
const int INF = 1e9;

int ac, aj;
int m[MINS], d[MINS][MINS / 2 + 1][2];

int count() {
	for (int i = 0; i < MINS; ++i)
		for (int j = 0; j <= MINS / 2; ++j)
				d[i][j][C] = d[i][j][J] = INF;
	if (m[0] == C)
		d[0][1][C] = 0;
	else
		d[0][0][J] = 0;
	for (int i = 1; i < MINS; ++i) {
		if (m[i] == C || m[i] == F)
			for (int j = 1; j <= MINS / 2; ++j)
				d[i][j][C] = min(d[i - 1][j - 1][C], d[i - 1][j - 1][J] + 1);
		if (m[i] == J || m[i] == F)
			for (int j = 0; j <= MINS / 2; ++j)
				d[i][j][J] = min(d[i - 1][j][J], d[i - 1][j][C] + 1);
	}
	if (m[0] == C)
		return min(d[MINS - 1][MINS / 2][C], d[MINS - 1][MINS / 2][J] + 1);
	else
		return min(d[MINS - 1][MINS / 2][J], d[MINS - 1][MINS / 2][C] + 1);
}

int solve() {
	for (int i = 0; i < MINS; ++i)
		m[i] = F;
	cin >> ac >> aj;
	int tc = 0, tj = 0;
	for (int i = 0; i < ac; ++i) {
		int l, r;
		cin >> l >> r;
		for (int j = l; j < r; ++j)
			m[j] = C, ++tc;
	}
	for (int i = 0; i < aj; ++i) {
		int l, r;
		cin >> l >> r;
		for (int j = l; j < r; ++j)
			m[j] = J, ++tj;
	}
	if (m[0] == F) {
		int res1 = INF, res2 = INF;
		if (tc < MINS / 2) {
			m[0] = C;
			res1 = count();
		}
		if (tj < MINS / 2) {
			m[0] = J;
			res2 = count();
		}
		return min(res1, res2);
	} else
		return count();
}

int main() {
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
		cout << "Case #" << i << ": " << solve() << endl;
	cin >> t;
	return 0;
}
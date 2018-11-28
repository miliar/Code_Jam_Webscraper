#include <iostream>
#include <vector>
#include <map>

using namespace std;

#define rep(i, n) for (int i = 0; i < (int)n; i++)
#define vec vector
#define pb push_back

int main(void)
{
	int T;
	cin >> T;
	rep(t, T) {
		int r, c;
		cin >> r >> c;
		vec<vec<char>> cake(r, vec<char>(c));
		vec<vec<char>> tate(r);
		rep(i, r) rep(j, c) {
			cin >> cake[i][j];
			if (cake[i][j] != '?') tate[i].pb(cake[i][j]);
		}
		int prev = 0;
		rep(i, r) {
			if (tate[i].empty()) {
				prev++;
				continue;
			}
			int cur = 0;
			rep(j, c) {
				if ((int)tate[i].size() == cur + 1) cake[i][j] = tate[i][cur];
				else if (cake[i][j] == '?') cake[i][j] = tate[i][cur];
				else cur++;
			}
			rep(k, prev) rep(j, c) cake[i - k - 1][j] = cake[i][j];
			prev = 0;
		}
		if (prev) {
			rep(k, prev) rep(j, c) cake[r - k - 1][j] = cake[r - prev - 1][j];
		}

		cout << "Case #" << t + 1 << ":" << endl;
		rep(i, r) {
			rep(j, c) cout << cake[i][j];
			cout << endl;
		}
	}
	return 0;
}


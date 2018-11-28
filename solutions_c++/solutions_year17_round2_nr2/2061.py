#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// B-small

struct Color {
	int c, n;

	Color() {}
	Color(int c, int n) : c(c), n(n) {}
};

int t, n, r, o, y, g, b, v, cnt = 1, prevc = -1;
string ans = "";
vector<Color> color;
bool flag = true;

// r : 0, y : 1, b : 2
bool comp(const Color &c1, const Color &c2) {
	if (c1.n == c2.n) return c1.c < c2.c;
	return c1.n > c2.n;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> t;

	while (t--) {
		cin >> n;
		cin >> r >> o >> y >> g >> b >> v;

		color.push_back({0, r});
		color.push_back({1, y});
		color.push_back({2, b});

		while (n--) {
			sort(color.begin(), color.end(), comp);

			/*for(int i = 0; i < color.size(); ++i) {
				cout << color[i].c << " " << color[i].n << endl;
			}*/

			int cc;

			if (prevc != color[0].c) {
				color[0].n--;
				cc = color[0].c;
				prevc = color[0].c;
			}
			else {
				if (color[1].n == 0) {
					flag = false;
					break;
				}
				color[1].n--;
				cc = color[1].c;
				prevc = color[1].c;
			}
			
			if (cc == 0) ans += "R";
			else if (cc == 1) ans += "Y";
			else if (cc == 2) ans += "B";
		}

		int chance = 3, point = 0;

		L:;

		for (int i = 1; i < ans.size() - 1; ++i) {
			if (ans[i - 1] == ans[i]) {
				if (i + 1 < ans.size()) swap(ans[i], ans[i + 1]);
				flag = false;
			}
			else if (ans[i] == ans[i + 1]) {
				if (i + 2 < ans.size()) swap(ans[i + 1], ans[i + 2]);
				flag = false;
			}
		}

		if (ans[0] == ans[ans.size() - 1]) flag = false;

		if (!flag && chance > 0) {
			chance--;
			flag = true;
			char c = ans[ans.size() - 1];
			string sub = c + ans.erase(ans.size() - 1, 1);
			ans = sub;
			goto L;
		}

		if (!flag) {
			for (int i = 1; i < ans.size() - 1; ++i) {
				if (ans[i - 1] == ans[i] || ans[i] == ans[i + 1]) {
					flag = false;
					break;
				}
			}

			if (ans[0] == ans[ans.size() - 1]) flag = false;
		}

		if (flag) cout << "Case #" << cnt++ << ": " << ans << endl;
		else cout << "Case #" << cnt++ << ": IMPOSSIBLE" << endl;

		color.clear();
		ans = "";
		flag = true;
		prevc = -1;
	}

	return 0;
}

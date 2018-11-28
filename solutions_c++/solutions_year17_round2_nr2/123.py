#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<string>
using namespace std;
int T, n, m;
string fr, fy, fb, ans;

int main()  {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> T;
	for (int C = 1; C <= T; C++) {
		int n, r, ry, y, yb, b, br;
		cin >> n >> r >> ry >> y >> yb >> b >> br;
		fr = "R", fy = "Y", fb = "B";
		printf("Case #%d: ", C);

		if (ry) {
			int needb = ry;
			if (ry + b < n) needb++;
			if (b < needb) {
				puts("IMPOSSIBLE");
				continue;
			}
			if (b == ry) {
				while (b--) printf("BO");
				puts("");
				continue;
			}
			b -= ry;
			while (ry--) fb.push_back('O'), fb.push_back('B');
		}

		if (yb) {
			int needr = yb;
			if (yb + r < n) needr++;
			if (r < needr) {
				puts("IMPOSSIBLE");
				continue;
			}
			if (r == yb) {
				while (r--) printf("RG");
				puts("");
				continue;
			}
			r -= yb;
			while (yb--) fr.push_back('G'), fr.push_back('R');
		}

		if (br) {
			int needy = br;
			if (br + y < n) needy++;
			if (y < needy) {
				puts("IMPOSSIBLE");
				continue;
			}
			if (y == br) {
				while (y--) printf("YV");
				puts("");
				continue;
			}
			y -= br;
			while (br--) fy.push_back('V'), fy.push_back('Y');
		}

		if (r&&!y&&!b || y&&!r&&!b || b&&!r&&!y) {
			puts("IMPOSSIBLE");
			continue;
		}

		if (!r) {
			if (y != b) {
				puts("IMPOSSIBLE");
				continue;
			}
			ans = "";
			while (y--) ans.push_back('Y'), ans.push_back('B');
		}
		else if (!y) {
			if (r != b) {
				puts("IMPOSSIBLE");
				continue;
			}
			ans = "";
			while (r--) ans.push_back('R'), ans.push_back('B');
		}
		else if (!b) {
			if (r != y) {
				puts("IMPOSSIBLE");
				continue;
			}
			ans = "";
			while (r--) ans.push_back('R'), ans.push_back('Y');
		}
		else {
			if (r > y + b || y > b + r || b > y + r) {
				puts("IMPOSSIBLE");
				continue;
			}
			ans = "";
			if (r >= y && r >= b) {
				while (r--) {
					ans.push_back('R');
					if (y > b) ans.push_back('Y'), y--;
					else ans.push_back('B'), b--;
				}
				while (y + b) {
					if (ans[ans.size() - 1] == 'Y') ans.push_back('B'), b--;
					else ans.push_back('Y'), y--;
				}
			}
			else if (y >= r && y >= b) {
				while (y--) {
					ans.push_back('Y');
					if (r > b) ans.push_back('R'), r--;
					else ans.push_back('B'), b--;
				}
				while (r + b) {
					if (ans[ans.size() - 1] == 'R') ans.push_back('B'), b--;
					else ans.push_back('R'), r--;
				}
			}
			else if (b >= y && b >= r) {
				while (b--) {
					ans.push_back('B');
					if (y > r) ans.push_back('Y'), y--;
					else ans.push_back('R'), r--;
				}
				while (y + r) {
					if (ans[ans.size() - 1] == 'Y') ans.push_back('R'), r--;
					else ans.push_back('Y'), y--;
				}
			}
		}

		for (int i = 0; i < ans.size(); i++) {
			if (ans[i] == 'R' && fr.size()) cout << fr, fr = "";
			else if (ans[i] == 'Y' && fy.size()) cout << fy, fy = "";
			else if (ans[i] == 'B' && fb.size()) cout << fb, fb = "";
			else cout << ans[i];
		}
		cout << endl;
	}
}
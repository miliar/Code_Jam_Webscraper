#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;


int main()
{
	freopen("B-small-attempt2.in", "rt", stdin);
	freopen("B-small-attempt2.out", "wt", stdout);

	int tests, caseNumber = 0;
	cin >> tests;
	while (++caseNumber <= tests) {
		int n, y, r, b, v, g, o;
		cin >> n >> r >> o >> y >> g >> b >> v;
		bool x = true;
		string ans;
		string vs;
		string gs;
		string os;

		if (v <= y && x) {
			for (int i = 0; i < v; ++i) {
				vs.push_back('Y');
				vs.push_back('V');
			}
			y -= v;
			v = 0;
		}
		else { x = false; }

		if (g <= r && x) {
			for (int i = 0; i < g; ++i) {
				gs.push_back('R');
				gs.push_back('G');
			}
			r -= g;
			g = 0;
		}
		else { x = false; }

		if (o <= b && x) {
			for (int i = 0; i < o; ++i) {
				os.push_back('B');
				os.push_back('O');
			}
			b -= o;
			o = 0;
		}
		else { x = false; }

		if (x && !(b == 0 && r == 0 && y == 0)) {
			if (!vs.empty()) {
				if (y > 0) {
					vs.push_back('Y');
					--y;
				}
				else { x = false; }
			}

			if (!gs.empty()) {
				if (r > 0) {
					gs.push_back('R');
					--r;
				}
				else { x = false; }
			}

			if (!os.empty()) {
				if (b > 0) {
					os.push_back('B');
					--b;
				}
				else { x = false; }
			}
		}

		if (x) {
			if (b == 0 && r == 0 && y == 0) {
				if (!vs.empty()) {
					ans = vs;
				}

				if (!gs.empty()) {
					ans = gs;
				}

				if (!os.empty()) {
					ans = os;
				}

				if (ans[0] == ans.back() && ans.size() > 1) {
					x = false;
				}
			}
			else {
				if (!vs.empty()) {
					++y;
				}

				if (!gs.empty()) {
					++r;
				}

				if (!os.empty()) {
					++b;
				}
				if (y + r + b == 1) {
					if (y == 1) {
						ans = "Y";
					}


					if (r == 1) {
						ans = "R";
					}


					if (b == 1) {
						ans = "B";
					}
				}
				else {
					if (y + r < b || r + b < y || y + b < r) {
						x = false;
					}
					else {
						bool can_y = true;
						bool can_r = true;
						bool can_b = true;
						n = y + r + b;
						for (int i = 0; i < n; ++i) {
							if (y >= r && y >= b && can_y) {
								--y;
								ans.push_back('Y');
								can_y = false;
								can_r = true;
								can_b = true;
								continue;
							}
							if (r >= y && r >= b && can_r) {
								--r;
								ans.push_back('R');
								can_y = true;
								can_r = false;
								can_b = true;
								continue;
							}
							if (b >= r && b >= y && can_b) {
								--b;
								ans.push_back('B');
								can_y = true;
								can_r = true;
								can_b = false;
								continue;
							}


							if ((y >= r || y >= b) && can_y) {
								--y;
								ans.push_back('Y');
								can_y = false;
								can_r = true;
								can_b = true;
								continue;
							}
							if ((r >= y || r >= b) && can_r) {
								--r;
								ans.push_back('R');
								can_y = true;
								can_r = false;
								can_b = true;
								continue;
							}
							if ((b >= r || b >= y) && can_b) {
								--b;
								ans.push_back('B');
								can_y = true;
								can_r = true;
								can_b = false;
								continue;
							}
							cout << "wrong algorithm" << endl;
							x = false;
							break;
						}
						if (x && ans[0] == ans.back()) {
							swap(ans[ans.size() - 1], ans[ans.size() - 2]);
						}
					}
				}
				if (x) {
					string new_ans;
					for (size_t i = 0; i < ans.size(); ++i) {
						if (ans[i] == 'Y' && !vs.empty()) {
							new_ans.append(vs);
							vs.clear();
						}
						else if (ans[i] == 'R' && !gs.empty()) {
							new_ans.append(gs);
							gs.clear();
						}
						else if (ans[i] == 'B' && !os.empty()) {
							new_ans.append(os);
							os.clear();
						}
						else {
							new_ans.push_back(ans[i]);
						}
					}
					ans = new_ans;
				}
			}			
		}

		if (x) {
			printf("Case #%d: %s\n", caseNumber, ans.c_str());
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", caseNumber);
		}
	}
	return 0;
}

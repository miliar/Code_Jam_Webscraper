#include <bits/stdc++.h>
using namespace std;

bool check(char a, char b) {
	if (a == b) {
		return false;
	}
	if ((a == 'O' && b != 'B') || (b == 'O' && a != 'B')) {
		return false;
	}
	if ((a == 'G' && b != 'R') || (b == 'G' && a != 'R')) {
		return false;
	}
	if ((a == 'V' && b != 'Y') || (b == 'V' && a != 'Y')) {
		return false;
	}
	return true;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		int N, R, O, Y, G, B, V;
		scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
		bool tk = (R <= B + Y && B <= R + Y && Y <= R + B);
		bool ok = true;
		string ans;
		if (N < 3) {
			assert(false);
		} else {
			while (ok && ans.size() < N) {
				if (O > 0) {
					if (B == 0) {
						ok = false;
					} else {
						ans += "OB";
						--O, --B;
					}
				} else if (G > 0) {
					if (R == 0) {
						ok = false;
					} else {
						if (!ans.empty() && ans[ans.size() - 1] != 'R') {
							if (R == 0) {
								ok = false;
							} else {
								--R;
								ans += 'R';
							}
						} else {
							if (R == 0) {
								ok = false;
							} else {
								ans += "GR";
								--G, --R;
							}
						}
					}
				} else if (V > 0) {
					if (Y == 0) {
						ok = false;
					} else {
						if (!ans.empty() && ans[ans.size() - 1] != 'Y') {
							if (Y == 0) {
								ok = false;
							} else {
								--Y;
								ans += 'Y';
							}
						} else {
							ans += "VY";
							--V, --Y;
						}
					}
				} else {
					if (!ans.empty()) {
						if (ans[0] == 'O') {
							if (B == 0) {
								ok = false;
							} else {
								ans = "B" + ans;
								--B;
							}
							continue;
						} else if (ans[0] == 'G') {
							if (R == 0) {
								ok = false;
							} else {
								ans = "R" + ans;
								--R;
							}
							continue;
						} else if (ans[0] == 'V') {
							if (V == 0) {
								ok = false;
							} else {
								ans = "Y" + ans;
								--Y;
							}
							continue;
						}
					}
					//cout << ans << endl;
					//cout <<  B << " " << R << " " << Y << endl;
					if ((ans.empty() || ans[ans.size() - 1] == 'B')) {
						if (R > Y || (R == Y && (ans.empty() || ans[0] == 'R'))) {
							if (R == 0) {
								ok = false;
							} else {
								--R;
								ans += 'R';
							}
						} else if (Y > 0) {
							--Y;
							ans += 'Y';
						} else {
							ok = false;
						}
					} else if ((ans.empty() || ans[ans.size() - 1] == 'R')) {
						if (B > Y || (B == Y && (ans.empty() || ans[0] == 'B'))) {
							if (B == 0) {
								ok = false;
							} else {
								--B;
								ans += 'B';
							}
						} else if (Y > 0) {
							--Y;
							ans += 'Y';
						} else {
							ok = false;
						}
					} else if ((ans.empty() || ans[ans.size() - 1] == 'Y')) {
						if (B > R || (B == R && (ans.empty() || ans[0] == 'B'))) {
							if (B == 0) {
								ok = false;
							} else {
								--B;
								ans += 'B';
							}
						} else if (R > 0) {
							--R;
							ans += 'R';
						} else {
							ok = false;
						}
					}
				}
			}
		}
		if (ok && !check(ans[0], ans[ans.size() - 1])) {
			ok = false;
		}
		cout << "Case #" << (i + 1) << ": ";
		if (ok) {
			cout << ans << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
			/*if (tk) {
				return 1;
			}*/
		}
	}
	return 0;
}

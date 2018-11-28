#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

char c[1005];

int main() {
	int T; scanf("%d", &T);
	for (int kk = 1; kk <= T; kk++) {
		int n, r, o, y, g, b, v;
		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
		printf("Case #%d: ", kk);
		if (o == b && r + y + g + v == 0) {
			for (int i = 1; i * 2 <= n; i++) {
				putchar('O');
				putchar('B');
			}
			puts("");
		} else if (g == r && o + y + b + v == 0) {
			for (int i = 1; i * 2 <= n; i++) {
				putchar('G');
				putchar('R');
			}
			puts("");
		} else if (v == y && r + o + g + b == 0) {
			for (int i = 1; i * 2 <= n; i++) {
				putchar('V');
				putchar('Y');
			}
			puts("");
		} else if (o > 0 && o >= b || g > 0 && g >= r || v > 0 && v >= y) {
			puts("IMPOSSIBLE");
		} else {
			int bb = b - o;
			int rr = r - g;
			int yy = y - v;
			if (bb > rr + yy || rr > bb + yy || yy > bb + rr) {
				puts("IMPOSSIBLE");
			} else {
				int m = bb + rr + yy, p = 0;
				if (bb >= rr && bb >= yy) {
					if (m % 2 == 0) {
						int t = (yy + rr - bb) / 2;
						for (int i = 0; i < yy - t; i++) {
							c[p++] = 'B'; c[p++] = 'Y';
						} 
						for (int i = 0; i < rr - t; i++) {
							c[p++] = 'B'; c[p++] = 'R';
						}
						for (int i = 0; i < t; i++) {
							c[p++] = 'Y'; c[p++] = 'R';
						}
					} else {
						if (yy >= rr) {
							int t = (yy + rr - bb) / 2;
							for (int i = 0; i < yy - (t + 1); i++) {
								c[p++] = 'B'; c[p++] = 'Y';
							}
							for (int i = 0; i < rr - t; i++) {
								c[p++] = 'B'; c[p++] = 'R';
							}
							for (int i = 0; i < t; i++) {
								c[p++] = 'Y'; c[p++] = 'R';
							}
							c[p++] = 'Y';
						} else {
							int t = (yy + rr - bb) / 2;
							for (int i = 0; i < rr - (t + 1); i++) {
								c[p++] = 'B'; c[p++] = 'R';
							}
							for (int i = 0; i < yy - t; i++) {
								c[p++] = 'B'; c[p++] = 'Y';
							}
							for (int i = 0; i < t; i++) {
								c[p++] = 'R'; c[p++] = 'Y';
							}
							c[p++] = 'R';
						}
					}
				} else if (rr >= yy) {
					if (m % 2 == 0) {
						int t = (yy + bb - rr) / 2;
						for (int i = 0; i < yy - t; i++) {
							c[p++] = 'R'; c[p++] = 'Y';
						} 
						for (int i = 0; i < bb - t; i++) {
							c[p++] = 'R'; c[p++] = 'B';
						}
						for (int i = 0; i < t; i++) {
							c[p++] = 'Y'; c[p++] = 'B';
						}
					} else {
						if (yy >= bb) {
							int t = (yy + bb - rr) / 2;
							for (int i = 0; i < yy - (t + 1); i++) {
								c[p++] = 'R'; c[p++] = 'Y';
							}
							for (int i = 0; i < bb - t; i++) {
								c[p++] = 'R'; c[p++] = 'B';
							}
							for (int i = 0; i < t; i++) {
								c[p++] = 'Y'; c[p++] = 'B';
							}
							c[p++] = 'Y';
						} else {
							int t = (yy + bb - rr) / 2;
							for (int i = 0; i < bb - (t + 1); i++) {
								c[p++] = 'R'; c[p++] = 'B';
							}
							for (int i = 0; i < yy - t; i++) {
								c[p++] = 'R'; c[p++] = 'Y';
							}
							for (int i = 0; i < t; i++) {
								c[p++] = 'B'; c[p++] = 'Y';
							}
							c[p++] = 'B';
						}
					}
				} else {
					if (m % 2 == 0) {
						int t = (bb + rr - yy) / 2;
						for (int i = 0; i < bb - t; i++) {
							c[p++] = 'Y'; c[p++] = 'B';
						} 
						for (int i = 0; i < rr - t; i++) {
							c[p++] = 'Y'; c[p++] = 'R';
						}
						for (int i = 0; i < t; i++) {
							c[p++] = 'B'; c[p++] = 'R';
						}
					} else {
						if (bb >= rr) {
							int t = (bb + rr - yy) / 2;
							for (int i = 0; i < bb - (t + 1); i++) {
								c[p++] = 'Y'; c[p++] = 'B';
							}
							for (int i = 0; i < rr - t; i++) {
								c[p++] = 'Y'; c[p++] = 'R';
							}
							for (int i = 0; i < t; i++) {
								c[p++] = 'B'; c[p++] = 'R';
							}
							c[p++] = 'B';
						} else {
							int t = (bb + rr - yy) / 2;
							for (int i = 0; i < rr - (t + 1); i++) {
								c[p++] = 'Y'; c[p++] = 'R';
							}
							for (int i = 0; i < bb - t; i++) {
								c[p++] = 'Y'; c[p++] = 'B';
							}
							for (int i = 0; i < t; i++) {
								c[p++] = 'R'; c[p++] = 'B';
							}
							c[p++] = 'R';
						}
					}
				}
				bool fB = true, fR = true, fY = true;
				for (int i = 0; i < m; i++) {
					putchar(c[i]);
					if (c[i] == 'B' && fB) {
						fB = false;
						for (int j = 0; j < o; j++) {
							printf("OB");
						}
					} else if (c[i] == 'R' && fR) {
						fR = false;
						for (int j = 0; j < g; j++) {
							printf("GR");
						}
					} else if (c[i] == 'Y' && fY) {
						fY = false;
						for (int j = 0; j < v; j++) {
							printf("VY");
						}
					}
				}
				puts("");
			}
		}
	}
	return 0;
}
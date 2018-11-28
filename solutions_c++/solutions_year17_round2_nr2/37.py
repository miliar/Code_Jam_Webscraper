#include <bits/stdc++.h>

using namespace std;

const int MX = 1000;

char s[MX + 1];

bool bad(char C, char L) {
	if (C == 'R') {
		if (L == 'R' || L == 'O' || L == 'V') return true;
	}
	else if (C == 'Y') {
		if (L == 'Y' || L == 'O' || L == 'G') return true;
	}
	else if (C == 'B') {
		if (L == 'B' || L == 'G' || L == 'V') return true;
	}
	
	return false;
}

bool check(int n, int x, char L, char R, char C) {
	if (bad(C, L)) n--;
	if (bad(C, R)) n--;
	
	return (n + 1) / 2 >= x;
}

bool check(int r, int o, int y, int g, int b, int v, char L, char R) {
	int n = r + o + y + g + b + v;
	
	return check(n, r + o + v, L, R, 'R') && 
	       check(n, y + o + g, L, R, 'Y') && 
	       check(n, b + g + v, L, R, 'B');
}

bool fun(int x, int r, int o, int y, int g, int b, int v, char L, char R, char P = 0) {
	s[x] = 0;
	if (r < 0 || o < 0 || y < 0 || g < 0 || b < 0 || v < 0) return false;
	if (bad(P, L)) return false;
	int n = r + o + y + g + b + v;
	if (n == 0) {
		if (bad(L, R)) return false;
		
		return true;
	}
	if (check(r, o, y, g, b, v, L, R) == false) return false;

	if (fun(x + 1, r - 1, o, y, g, b, v, 'R', R, L)) s[x] = 'R';
	else if (fun(x + 1, r, o - 1, y, g, b, v, 'O', R, L)) s[x] = 'O';
	else if (fun(x + 1, r, o, y - 1, g, b, v, 'Y', R, L)) s[x] = 'Y';
	else if (fun(x + 1, r, o, y, g - 1, b, v, 'G', R, L)) s[x] = 'G';
	else if (fun(x + 1, r, o, y, g, b - 1, v, 'B', R, L)) s[x] = 'B';
	else if (fun(x + 1, r, o, y, g, b, v - 1, 'V', R, L)) s[x] = 'V';
	else assert(false);
	
	return true;
}

void two(char A, char B, int n) {
	for (int i = 0; i < n; i++) s[i] = i % 2 == 0 ? A : B;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		int n, r, o, y, g, b, v;
		scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
		
		const char* ans = s; 
		if (r == g && n == r + g) two('R', 'G', n);
		else if (y == v && n == y + v) two('Y', 'V', n);
		else if (b == o && n == b + o) two('B', 'O', n);
		else if (g >= max(r, 1) || v >= max(y, 1) || o >= max(b, 1)) ans = "IMPOSSIBLE";
		else {
			r -= g;
			y -= v;
			b -= o;
			
			if (fun(1, r - 1, 0, y, 0, b, 0, 'R', 'R')) s[0] = 'R';
			else if (fun(1, r, 0 - 1, y, 0, b, 0, 'O', 'O')) s[0] = 'O';
			else if (fun(1, r, 0, y - 1, 0, b, 0, 'Y', 'Y')) s[0] = 'Y';
			else if (fun(1, r, 0, y, 0 - 1, b, 0, 'G', 'G')) s[0] = 'G';
			else if (fun(1, r, 0, y, 0, b - 1, 0, 'B', 'B')) s[0] = 'B';
			else if (fun(1, r, 0, y, 0, b, 0 - 1, 'V', 'V')) s[0] = 'V';
			else ans = "IMPOSSIBLE";
			
			for (int i = 0; i < n; i++) {
				if (s[i] == 'R') {
					while (g) {
						for (int j = n - 1; j > i + 2; j--) s[j] = s[j - 2];
						s[i + 1] = 'G';
						s[i + 2] = 'R';
						
						g--;
					}
				}
				else if (s[i] == 'Y') {
					while (v) {
						for (int j = n - 1; j > i + 2; j--) s[j] = s[j - 2];
						s[i + 1] = 'V';
						s[i + 2] = 'Y';
						
						v--;
					}
				}
				else if (s[i] == 'B') {
					while (o) {
						for (int j = n - 1; j > i + 2; j--) s[j] = s[j - 2];
						s[i + 1] = 'O';
						s[i + 2] = 'B';
						
						o--;
					}
				}
			}
		}
		
		s[n] = 0;
		printf("Case #%d: %s\n", t, ans);
	}

	return 0;
}

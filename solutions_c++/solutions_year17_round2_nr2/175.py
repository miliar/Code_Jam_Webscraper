#include <stdio.h>
#include <algorithm>
using namespace std;

int T, cas;
int N;
int R, O, Y, G, B, V;
char first;

void dfs(int r, int y, int b, char prefix)
{
	if (prefix == 'R' && G > 0) {
		for (int i = 0; i < G; i++) {
			printf("GR");
		}
		G = 0;
	} else if (prefix == 'Y' && V > 0) {
		for (int i = 0; i < V; i++) {
			printf("VY");
		}
		V = 0;
	} else if (prefix == 'B' && O > 0) {
		for (int i = 0; i < O; i++) {
			printf("OB");
		}
		O = 0;
	}

	if (r == 0 && y == 0 && b == 0)
		return;
	if (prefix == 'R') {
		if (y > b) {
			printf("Y");
			dfs(r, y-1, b, 'Y');
		} else if (y < b) {
			printf("B");
			dfs(r, y, b-1, 'B');
		} else {
			if (first == 'Y') {
				printf("Y");
				dfs(r, y-1, b, 'Y');
			} else {
				printf("B");
				dfs(r, y, b-1, 'B');
			}
		}
	} else if (prefix == 'Y') {
		if (r > b) {
			printf("R");
			dfs(r-1, y, b, 'R');
		} else if (r < b) {
			printf("B");
			dfs(r, y, b-1, 'B');
		} else {
			if (first == 'R') {
				printf("R");
				dfs(r-1, y, b, 'R');
			} else {
				printf("B");
				dfs(r, y, b-1, 'B');
			}
		}
	} else if (prefix == 'B') {
		if (r > y) {
			printf("R");
			dfs(r-1, y, b, 'R');
		} else if (r < y) {
			printf("Y");
			dfs(r, y-1, b, 'Y');
		} else {
			if (first == 'R') {
				printf("R");
				dfs(r-1, y, b, 'R');
			} else {
				printf("Y");
				dfs(r, y-1, b, 'Y');
			}
		}
	} else {
		if (r > y && r > b) {
			first = 'R';
			printf("R");
			dfs(r-1, y, b, 'R');
		} else if (y >= r && y > b) {
			first = 'Y';
			printf("Y");
			dfs(r, y-1, b, 'Y');
		} else {
			first = 'B';
			printf("B");
			dfs(r, y, b-1, 'B');
		}
	}
}

void solve()
{
	if (O+B == N) {
		if (O == B) {
			for (int i = 0; i < O; i++) {
				printf("OB");
			}
		} else {
			printf("IMPOSSIBLE");
		}
		return;
	} else {
		if (O > 0 && B <= O) {
			printf("IMPOSSIBLE");
			return;
		}
		B -= O;
	}

	if (G+R == N) {
		if (G == R) {
			for (int i = 0; i < G; i++) {
				printf("GR");
			}
		} else {
			printf("IMPOSSIBLE");
		}
		return;
	} else {
		if (G > 0 && R <= G) {
			printf("IMPOSSIBLE");
			return;
		}
		R -= G;
	}

	if (V+Y == N) {
		if (V == Y) {
			for (int i = 0; i < V; i++) {
				printf("VY");
			}
		} else {
			printf("IMPOSSIBLE");
		}
		return;
	} else {
		if (V > 0 && Y <= V) {
			printf("IMPOSSIBLE");
			return;
		}
		Y -= V;
	}

	if (R > Y+B) {
		printf("IMPOSSIBLE");
		return;
	}

	if (Y > R+B) {
		printf("IMPOSSIBLE");
		return;
	}

	if (B > R+Y) {
		printf("IMPOSSIBLE");
		return;
	}

	dfs(R, Y, B, 'x');
}

int main()
{
	scanf(" %d", &T);
	for (cas = 1; cas <= T; cas++) {
		scanf(" %d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

		printf("Case #%d: ", cas);
		solve();
		puts("");
	}

	return 0;
}
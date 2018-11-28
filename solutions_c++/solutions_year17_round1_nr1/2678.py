#include <bits/stdc++.h>

#define sz(z) (int)z.size()
#define fo(i,a,b) for (auto (i) = (a); (i) < (b); (i)++)
#define mp make_pair
#define pb push_back

using namespace std;

#define DEBUG

#ifdef DEBUG
#define D(x...) printf(x)
#else
#define D(x...) 
#endif

typedef long long ll;
typedef pair<int,int> ii;

int r, c;

char grid[1234][1234];
int seen[1234];

bool inGrid (int a, int b) {
	return a >= 0 && a < r && b >= 0 && b < c;
}

void clean (int r1, int c1, int r2, int c2, char K) {
	fo(i,r1,r2+1) fo(j,c1,c2+1) {
		grid[i][j] = K;
	}
}
bool check (int r1, int c1, int r2, int c2, char K) {
	if (!inGrid(r1, c1) || !inGrid(r2, c2)) return 0;
	fo(i,r1,r2+1) fo(j,c1,c2+1) {
		if (grid[i][j] != '?' && grid[i][j] != K) return 0;
	}
	return 1;
}

void go () {
	for (int i = r-1; i >= 0; i--) {
		for (int j = c-1; j >= 0; j--) {
			char K = grid[i][j];
			if (K != '?' && !seen[K]) {
				seen[K] = 1;	
				int r1, r2, c1, c2;
				r1 = r2 = i;
				c1 = c2 = j;
				while (check(r1-1, c1, r2, c2,K)) r1--;	
				while (check(r1, c1-1, r2, c2,K)) c1--;	
				while (check(r1, c1, r2+1, c2,K)) r2++;	
				while (check(r1, c1, r2, c2+1,K)) c2++;	
				clean(r1,c1,r2,c2,K);
			}
		}
	}
}

int main() {
	int t;
	scanf("%d\n", &t);
	for (int _ = 1; _ <= t; _++) {
		printf("Case #%d:\n", _);
		scanf("%d %d", &r, &c);
		memset(seen, 0, sizeof(seen));
		fo(i,0,r) scanf("%s", grid[i]);
		go();
		fo(i,0,r) {
			printf("%s\n", grid[i]);
		}
	}
	
	return 0;
}

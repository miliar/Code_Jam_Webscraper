#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

typedef int Grid[100][100];

void andT(Grid &G, int N, int mask, int x, int y) {
	for (int n = 0; n < N; ++n) {
		G[y][n] &= mask;
		G[n][x] &= mask;
	}
}

int countT(Grid &G, int N, int mask, int x, int y) {
	int count = 0;
	for (int n = 0; n < N; ++n) {
		if (G[y][n] & mask) count++;
		if (G[n][x] & mask) count++;
	}
	return count;
}

void andX(Grid &G, int N, int mask, int x, int y) {
	for (int n = 0; n < N; ++n) {
		if (y - n >= 0 && x - n >= 0) G[y - n][x - n] &= mask;
		if (y - n >= 0 && x + n <  N) G[y - n][x + n] &= mask;
		if (y + n <  N && x - n >= 0) G[y + n][x - n] &= mask;
		if (y + n <  N && x + n <  N) G[y + n][x + n] &= mask;
	}
}

int countX(Grid &G, int N, int mask, int x, int y) {
	int count = 0;
	for (int n = 0; n < N; ++n) {
		if (y - n >= 0 && x - n >= 0) if (G[y - n][x - n] & mask) count++;
		if (y - n >= 0 && x + n <  N) if (G[y - n][x + n] & mask) count++;
		if (y + n <  N && x - n >= 0) if (G[y + n][x - n] & mask) count++;
		if (y + n <  N && x + n <  N) if (G[y + n][x + n] & mask) count++;
	}
	return count;
}

// ox+
// 321

void apply(Grid &G, int N, int m, int x, int y) {
	switch (m) {
		case 1:
			// no other cell on this diagonal may be '+' (or 'o')
			andX(G, N, ~1, x, y);
			//G[y][x] |= 1;
			break;
		
		case 2:
			// no other cell in this row or column may be 'x' (or 'o')
			andT(G, N, ~2, x, y);
			//G[y][x] |= 2;
			break;
			
		case 3:
			// 3 is just the same as (x | +)
			apply(G, N, 1, x, y);
			apply(G, N, 2, x, y);
			break;
	}
}

int ctom(char c) {
	switch (c) {
		case '+': return 1;
		case 'x': return 2;
		case 'o': return 3;
	}
}

char mtoc(int m) {
	switch (m) {
		case 0: return '.';
		case 1: return '+';
		case 2: return 'x';
		case 3: return 'o';
	}
}

typedef struct {
	int x, y;
	int m;
} MODEL;

int solve() {
	//fprintf(stderr, "-------------------------------------------------\n");
	int N, M;
	
	Grid G = { 0 };
	Grid H = { 0 };
	Grid V = { 0 };
	
	scanf("%d %d", &N, &M);
	
	for (int y = 0; y < N; ++y)
	for (int x = 0; x < N; ++x) {
		H[y][x] = 3;
	}
	
	for (int m = 0; m < M; ++m) {
		char c;
		int x, y;
		
		scanf("\n%c %d %d", &c, &y, &x);
		
		int mask = ctom(c);
		
		G[y - 1][x - 1] = mask;
		apply(H, N, mask, x - 1, y - 1);
	}
	
	//fprintf(stderr, "INPUT\n");
	for (int y = 0; y < N; ++y) {
		for (int x = 0; x < N; ++x) {
			//fprintf(stderr, "%d ", G[y][x]);
		}
		//fprintf(stderr, "\n");
	}
	
	int  best = 0x7FFFFFFF;
	MODEL model;
	
	while (true) {
		best = 0x7FFFFFFF;
		
		for (int y = 0; y < N; ++y) {
			for (int x = 0; x < N; ++x) {
				if (!H[y][x])
					continue;
				
				if (H[y][x] & 1) {
					int cost = countX(H, N, 1, x, y);
					////fprintf(stderr, "+ %d %d cost: %d\n", x, y, cost);
					if (cost < best) {
						best = cost;
						model.m = 1;
						model.x = x;
						model.y = y;
					}
				}
				
				if (H[y][x] & 2) {
					int cost = countT(H, N, 2, x, y);
					////fprintf(stderr, "x %d %d cost: %d\n", x, y, cost);
					if (cost < best) {
						best = cost;
						model.m = 2;
						model.x = x;
						model.y = y;
					}
				}
			}
		}
		
		if (best == 0x7FFFFFFF) {
			break;
		}
		
		apply(H, N, model.m, model.x, model.y);
		G[model.y][model.x] |= model.m;
		V[model.y][model.x] = G[model.y][model.x];
	}
	
	int score = 0;
	int changes = 0;
	
	//fprintf(stderr, "OUTPUT\n");
	for (int y = 0; y < N; ++y) {
		for (int x = 0; x < N; ++x) {
			if (G[y][x] & 1) score++;
			if (G[y][x] & 2) score++;
			if (V[y][x]) changes++;
			
			//fprintf(stderr, "%d ", G[y][x]);
		}
		//fprintf(stderr, "\n");
	}
	
	printf("%d %d\n", score, changes);
	
	for (int y = 0; y < N; ++y) 
	for (int x = 0; x < N; ++x) {
		if (V[y][x])
			printf("%c %d %d\n", mtoc(V[y][x]), y + 1, x + 1);
	}
	
	return score;
}

int main(int, char **) {
	int T;
	
	scanf("%d", &T);
	
	for (int t = 0; t < T; ++t) {
		printf("Case #%d: ", t + 1);
		solve();
	}
}
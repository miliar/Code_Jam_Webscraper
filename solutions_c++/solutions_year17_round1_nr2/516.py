#include <bits/stdc++.h>

using namespace std;

const int maxN = 55;
const int maxP = 55;

typedef pair<int, int> pii;

#define fs first
#define sc second
#define mp make_pair

int Ceil(int p, int q) {
	return ((p-1)/q)+1;
}

int Floor(int p, int q) {
	return p/q;
}

int N, P;
int R[maxN];
int Q[maxN][maxP];
pii Range[maxN][maxP];
int ps[maxN];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int test = 1; test <= nTests; ++test) {
		scanf("%d %d", &N, &P);
		for (int i = 0; i < N; ++i)
			scanf("%d", &R[i]);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < P; ++j) {
				scanf("%d", &Q[i][j]);
				Range[i][j].fs = Ceil(Q[i][j]*100, R[i]*110);
				Range[i][j].sc = Floor(Q[i][j]*100, R[i]*90);
			}
			sort(Range[i], Range[i]+P);
		}
		// puts("##########");
		// for (int i = 0; i < N; ++i) {
		// 	for (int j = 0; j < P; ++j) 
		// 		printf("[%d %d] ", Range[i][j].fs, Range[i][j].sc);
		// 	puts("");
		// }
		// puts("##########");
		memset(ps, 0, sizeof(ps));
		int kits = 0;
		// puts("$$$$$$$$$$");
		for (int servings = 1; ; ) {
			// printf("%d\n", servings);
			bool stop = false;
			bool notFound = false;
			for (int i = 0; i < N; ++i) {
				while (ps[i] < P && Range[i][ps[i]].sc < servings)
					++ps[i];
				if (ps[i] == P) {
					stop = true;
					break;
				}
				if (Range[i][ps[i]].fs > servings)
					notFound = true;
			}
			if (stop) break;
			if (notFound) ++servings;
			else {
				kits++;
				for (int i = 0; i < N; ++i)
					++ps[i];
			}
		}
		// puts("$$$$$$$$$$");
		printf("Case #%d: %d\n", test, kits);
	}
	return 0;
}
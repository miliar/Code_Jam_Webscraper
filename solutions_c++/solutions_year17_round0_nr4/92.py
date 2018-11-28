#include <cstdio>
#include <memory.h>
#include <vector>
using namespace std;
const int INF = 1000000000;

int Source, Sink, Size;
int Cap[700][700];
bool Visit[700];

bool augment(int x) {
    if (Visit[x]) {
        return false;
    }
    Visit[x] = true;

    if (x == Sink) {
        return true;
    }

    for (int y = 0; y < Size; ++y) {
        if (Cap[x][y] > 0) {
            if (augment(y)) {
                Cap[x][y]--;
                Cap[y][x]++;
                return true;
            }
        }
    }
    return false;
}

bool augment() {
    memset(Visit, 0, sizeof(Visit));
    return augment(Source);
}

int flow() {
    int res = 0;
    while (augment()) {
        res++;
    }
    return res;
}

char A[101][101];
int main() {
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		int N, M;
		scanf("%d%d", &N, &M);

		memset(Cap, 0, sizeof(Cap));
		Source = 6 * N + 1;
		Sink = 6 * N + 2;
		Size = Sink + 1;

		for (int y = 0; y < N; ++y) {
			for (int x = 0; x < N; ++x) {
				A[y][x] = '.';
			}
		}
		for (int m = 0; m < M; ++m) {
			char type[2];
			int y, x;
			scanf("%s%d%d", type, &y, &x);
			A[y - 1][x - 1] = type[0];
		}
		for (int i = 0; i < N; ++i) {
			Cap[Source][i] = 1;
			Cap[N + i][Sink] = 1;
		}
		for (int i = 0; i < 2 * N - 1; ++i) {
			Cap[Source][2 * N + i] = 1;
			Cap[4 * N + i][Sink] = 1;
		}
		int score = 0;
		for (int y = 0; y < N; ++y) {
			for (int x = 0; x < N; ++x) {
				int u = y;
				int v = N + x;
				int p = 2 * N + y + x;
				int q = 4 * N + N - x + y - 1;
				if (A[y][x] == '+') {
					Cap[Source][p] = 0;
					Cap[q][Sink] = 0;
					score += 1;
				} else if (A[y][x] == 'x') {
					Cap[Source][u] = 0;
					Cap[v][Sink] = 0;
					score += 1;
				} else if (A[y][x] == 'o') {
					Cap[Source][p] = 0;
					Cap[q][Sink] = 0;
					Cap[Source][u] = 0;
					Cap[v][Sink] = 0;
					score += 2;
				}
				Cap[p][q] = 1;
				Cap[u][v] = 1;
			}
		}
		score = score + flow();
		vector<pair<char,pair<int,int>>> res;
		int added = 0;
		for (int y = 0; y < N; ++y) {
			for (int x = 0; x < N; ++x) {
				int u = y;
				int v = N + x;
				int p = 2 * N + y + x;
				int q = 4 * N + N - x + y - 1;
				if (Cap[p][q] == 0 && Cap[u][v] == 0) {
					if (A[y][x] == 'x') {
						res.push_back(make_pair('+', make_pair(y+1, x+1)));
					}
					if (A[y][x] == '+') {
						res.push_back(make_pair('x', make_pair(y+1, x+1)));
					}
					if (A[y][x] == '.') {
						res.push_back(make_pair('o', make_pair(y+1, x+1)));
					}
				}
				if (Cap[p][q] == 1 && Cap[u][v] == 0) {
					if (A[y][x] == '+') {
						res.push_back(make_pair('o', make_pair(y+1, x+1)));
					}
					if (A[y][x] == '.') {
						res.push_back(make_pair('x', make_pair(y+1, x+1)));
					}
				}
				if (Cap[p][q] == 0 && Cap[u][v] == 1) {
					if (A[y][x] == 'x') {
						res.push_back(make_pair('o', make_pair(y+1, x+1)));
					}
					if (A[y][x] == '.') {
						res.push_back(make_pair('+', make_pair(y+1, x+1)));
					}
				}
			}
		}
		printf("Case #%d: %d %d\n", tc, score, res.size());
		for (auto& i : res) {
			printf("%c %d %d\n", i.first, i.second.first, i.second.second);
		}
	}
	return 0;
}

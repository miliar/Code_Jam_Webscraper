#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAX = 1024;

double memo[MAX][MAX];
bool seen[MAX][MAX];

struct Cake {
	double height_area;
	double surface_area;
	bool operator<(const Cake& rhs) const {
		if (fabs(surface_area - rhs.surface_area) < 1e-9) return height_area > rhs.height_area;
       return surface_area > rhs.surface_area;
   }
};

Cake cakes[MAX];
int N, K;

const double Pi = 2 * acos(0);

double solve(int cur, int k) {
	if (cur == N) {
		if (k == K) return 0;
		else return -1e15;
	}

	double &ret = memo[cur][k];
	if (seen[cur][k]) return ret;
	seen[cur][k] = true;
	ret = 0;
	// take it
	if (k + 1 <= K) ret = max(ret, cakes[cur].height_area + solve(cur + 1, k + 1));
	// don't take it
	ret = max(ret, solve(cur + 1, k));
	return ret;
}

int main() {
	int tests, R, H;
	scanf("%d", &tests);
	for (int case_no = 1; case_no <= tests; ++case_no) {
		scanf("%d %d", &N, &K);
		for (int i = 0; i < N; ++i) {
			scanf("%d %d", &R, &H);
			cakes[i].height_area = H * 2*Pi*R;
			cakes[i].surface_area  = Pi*R*R;
			for (int k = 0; k <= K; ++k) {
				memo[i][k] = 0;
				seen[i][k] = false;
			}
		}

		sort(cakes, cakes + N);

		double answer = 0;
		for (int i = 0; i < N; ++i) {
			answer = max(answer, cakes[i].height_area + cakes[i].surface_area + solve(i + 1, 1));
		}

		printf("Case #%d: %.9lf\n", case_no, answer);
	}
	return 0;
}
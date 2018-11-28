/******/
#include <cstdio>
#include <cstring>
#include <algorithm>

typedef long long ll;

struct val_t {
	int max, min, s;
	bool operator<(const val_t &a) const {
		if (this->min != a.min) return this->min > a.min;
		if (this->max != a.max) return this->max > a.max;
		return this->s < a.s;
	}
};

int T;
int N, K;
val_t O[1000005];
int Oi;

inline int MAX(int a, int b) { return a > b ? a : b; }
inline int MIN(int a, int b) { return a < b ? a : b; }

void bs(int from, int to) {

	if (from + 1 >= to) {
		O[Oi].max = O[Oi].min = 0;
		O[Oi].s = to;
		Oi++;
		if (from != to) {
			O[Oi].max = 1;
			O[Oi].min = 0;
			O[Oi].s = from;
			Oi++;
		}
		return;
	}
	int mid = (from + to) / 2;
	O[Oi].max = MAX(mid - from, to - mid);
	O[Oi].min = MIN(mid - from, to - mid);
	O[Oi].s = mid;
	Oi++;
	bs(from, mid - 1);
	bs(mid + 1, to);
}

int main() {

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%d %d", &N, &K);
		Oi = 0;
		bs(1, N);

		std::sort(O, O + N);
		printf("Case #%d: %d %d\n", tc, O[K-1].max, O[K-1].min);
	}
	return 0;
}
/*****/
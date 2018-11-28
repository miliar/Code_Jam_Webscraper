#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <utility>

using namespace std;

int n, p;
int R[60];
int Q[60][60];
pair<int, pair<int, int> > pairs[3000];
priority_queue<int> heaps[60];

void read() {
	scanf("%d%d", &n, &p);

	for (int i = 0; i < n; i++) {
		scanf("%d", &R[i]);
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < p; j++) {
			scanf("%d", &Q[i][j]);
		}
	}
}

void process() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < p; j++) {
			pairs[i * p + j] = make_pair(
				(10 * Q[i][j] + 11 * R[i] - 1)/ (11 * R[i]),
				make_pair((10 * Q[i][j]) / (9 * R[i]), i)
			);
		}
	}
	sort(pairs, pairs + n * p);

	for (int j = 0; j < n; j++) {
		while (!heaps[j].empty()) {
			heaps[j].pop();
		}
	}

	int npairs = n * p;
	int res = 0;
	for (int i = 0; i < npairs; i++) {
		int cur_time = pairs[i].first;
		for (int j = 0; j < n; j++) {
			while (!heaps[j].empty() && -heaps[j].top() < cur_time) {
				heaps[j].pop();
			}
		}
		if (pairs[i].second.first >= cur_time) {
			heaps[pairs[i].second.second].push(-pairs[i].second.first);
		}

		int done = true;
		for (int j = 0; j < n; j++) {
			if (heaps[j].empty()) {
				done = false;
				break;
			}
		}
		if (done) {
			res++;
			for (int j = 0; j < n; j++) {
				heaps[j].pop();
			}
		}
	}
	printf("%d\n", res);
}

int main() {

	int cases;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		printf("Case #%d: ", i);
		read();
		process();
	}
	
	return 0;
}
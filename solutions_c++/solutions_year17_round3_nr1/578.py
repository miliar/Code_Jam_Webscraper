#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	double dy[2001];

	int i, j, k;

	int T;
	char buf[512];

	fgets(buf, 512, stdin);

	sscanf(buf, "%d", &T);

	for (i = 0; i < T; ++i) {
		int N, K;
		fgets(buf, 512, stdin);
		sscanf(buf, "%d %d", &N, &K);

		dy[0] = 0;
		vector< pair<int,int> > stacks;

		for (j = 0; j < N; ++j) {
			int R, H;
			fgets(buf, 512, stdin);
			sscanf(buf, "%d %d", &R, &H);
			dy[j] = 0;

			stacks.push_back(make_pair(R, H));
		}
		dy[j] = 0;

		sort(stacks.begin(), stacks.end());
		reverse(stacks.begin(), stacks.end());

		for (j = 1; j <= N; ++j) {
			int R, H;
			R = stacks[j - 1].first;
			H = stacks[j - 1].second;

			double x = (double)R * (double)R * 3.1415926535897931;
			double y = (double)R * 2 * (double)H * 3.1415926535897931;

			for (k = j - 1; k > 0; --k) {
				if (dy[k] + y > dy[k + 1]) {
					dy[k + 1] = dy[k] + y;
				}
			}

			if (x + y > dy[1])
				dy[1] = x + y;
		}

		printf("Case #%d: %.9lf\n", i + 1, dy[K]);
	}
}
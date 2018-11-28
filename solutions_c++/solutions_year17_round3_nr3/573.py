#include <cstdio>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int i, j, k;

	int T;
	char buf[2048];

	fgets(buf, 512, stdin);

	sscanf(buf, "%d", &T);

	for (i = 0; i < T; ++i) {
		int N, K;
		double U;
		double pro[51];

		fgets(buf, 512, stdin);
		sscanf(buf, "%d %d", &N, &K);

		fgets(buf, 512, stdin);
		sscanf(buf, "%lf", &U);

		fgets(buf, 2048, stdin);

		istringstream iss(buf);

		vector<double> st;

		for (j = 0; j < N; ++j) {
			iss >> pro[j];
			st.push_back(pro[j]);
		}

		while (U > 0) {
			sort(st.begin(), st.end());

			if (st[0] > 0.999999999999)
				break;

			for (j = 1; j < N; ++j) {
				if (st[j] > st[0])
					break;
			}

			if (j == N) {
				for (j = 0; j < N; ++j)
					st[j] += U / N;

				U = 0;

				break;
			}

			double gap = st[j] - st[0];

			for (k = 0; k < j; ++k) {
				st[k] += min(U / j, gap);
			}

			U -= min(U, gap * j);
		}

		double res = 1;
		for (j = 0; j < N; ++j) {
			//printf("%d is %lf %lf\n", j, st[j], res);
			res *= st[j];
		}

		printf("Case #%d: %lf\n", i + 1, res);
	}
}
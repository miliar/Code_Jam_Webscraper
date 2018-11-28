#include <cstdio>
#include <utility>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define inf 2e9


int main() {
	int t;

	scanf("%d", &t);


	for(int curT = 1; curT <= t; curT++) {
		int d, n;

		double maxTime = 0;

		scanf("%d %d", &d, &n);

		for(int i = 0; i <n; i++) {
			int k, s;

			scanf("%d %d", &k, &s);

			double finishTime = (double)(d - k) / (double)s;

			if(finishTime > maxTime) {
				maxTime = finishTime;
			}
		}

		printf("Case #%d: %f\n", curT, (double)d/(double)maxTime);
	}
}
#include <cstdio>
#include <algorithm>

using namespace std;

int t;
float maxTime;
int n;
int d;
int pos;
int k;

int main() {

	scanf("%d", &t);
	for(int testcase=1; testcase<=t; testcase++) {
		maxTime=0;
		scanf("%d %d", &d, &n);
		for(int i=0; i<n; i++) {
			scanf("%d %d", &pos, &k);
			int rest=d-pos;
			float cost=float(rest)/k;
			maxTime=max(maxTime, cost);
		}

		printf("Case #%d: %.6f\n", testcase, float(d)/maxTime+0.0000005);
	}

	return 0;
}
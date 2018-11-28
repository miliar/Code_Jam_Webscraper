#include <stdio.h>
#include <algorithm>

void solve() {
	int n, p;
	scanf("%d %d", &n, &p);
	int res = 0;
	int groupSize[4] = { 0 };
	for (int i = 0; i < n; i++) {
		int g;
		scanf("%d", &g);
		groupSize[g % p]++;
	}

	res += groupSize[0];
	int take;
	if (p == 4) {
		take = groupSize[2] / 2;
		groupSize[2] -= take * 2;
		res += take;

		take = std::min(groupSize[3], groupSize[1]);
		res += take;
		groupSize[3] -= take;
		groupSize[1] -= take;

		take = std::min(groupSize[1] / 2, groupSize[2]);
		res += take;
		groupSize[1] -= take * 2;
		groupSize[2] -= take;

		take = groupSize[1] / 4;
		res += take;
		groupSize[1] -= take * 4;

		take = std::min(groupSize[3] / 2, groupSize[2]);
		res += take;
		groupSize[3] -= take * 2;
		groupSize[2] -= take;

		take = groupSize[3] / 4;
		res += take;
		groupSize[3] -= take * 4;

		if (groupSize[1] || groupSize[2] || groupSize[3]) res++;
	}
	else if (p == 3) {
		take = std::min(groupSize[1], groupSize[2]);
		res += take;
		groupSize[1] -= take;
		groupSize[2] -= take;

		take = groupSize[1] / 3;
		res += take;
		groupSize[1] -= take * 3;

		take = groupSize[2] / 3;
		res += take;
		groupSize[2] -= take * 3;

		if (groupSize[1] || groupSize[2]) res++;
	}
	else if (p == 2) {
		take = groupSize[1] / 2;
		res += take;
		groupSize[1] -= take * 2;

		if (groupSize[1]) res++;
	}
	else throw "";

	printf("%d\n", res);
}

int main() {
	int T;
	scanf("%d", &T);
	
	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		solve();
	}

	return 0;
}

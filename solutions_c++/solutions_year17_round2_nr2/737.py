#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

void print(std::pair<int, char> &u) {
	printf("%c", u.second);
	--u.first;
}

int main() {
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		int n;
		int r, o, y, g, b, v;
		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
		printf("Case #%d: ", Case);
		std::vector<std::pair<int, char> > clr;
		clr.push_back(std::make_pair(r, 'R'));
		clr.push_back(std::make_pair(b, 'B'));
		clr.push_back(std::make_pair(y, 'Y'));
		std::sort(clr.begin(), clr.end());
		if (clr[2].first > clr[0].first + clr[1].first) printf("IMPOSSIBLE\n");
		else {
			print(clr[2]);
			if (clr[1].first == 0) {
				printf("\n");
				continue;
			}
			print(clr[1]);
			for (int u = 0; clr[0].first + clr[1].first > clr[2].first; u ^= 1) {
				print(clr[u]);
			}
			while (clr[0].first) {
				print(clr[2]);
				print(clr[0]);
			}
			while (clr[1].first) {
				print(clr[2]);
				print(clr[1]);
			}
			printf("\n");
		}
	}
	return 0;
}

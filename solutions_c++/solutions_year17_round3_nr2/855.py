#include <cstdio>
#include <vector>
using namespace std;
const int INF = 10000;

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int TN=1; TN<=T; ++TN) {
		int ac, aj;
		scanf("%d%d", &ac, &aj);
		vector<int> c(ac), d(ac), j(aj), k(aj);
		for (int i=0; i<ac; ++i)
			scanf("%d%d", &c[i], &d[i]);
		for (int i=0; i<aj; ++i)
			scanf("%d%d", &j[i], &k[i]);
		printf("Case #%d: ", TN);
		if (ac + aj == 1 || ac == 1) {
			puts("2");
		} else if (ac == 2) {
			if (c[0] < c[1] && (d[1]-c[0] <= 720 || d[0]+1440-c[1] <= 720))
				puts("2");
			else if (c[0] > c[1] && (d[0]-c[1] <= 720 || d[1]+1440-c[0] <= 720))
				puts("2");
			else
				puts("4");
		} else {
			if (j[0] < j[1] && (k[1]-j[0] <= 720 || k[0]+1440-j[1] <= 720))
				puts("2");
			else if (j[0] > j[1] && (k[0]-j[1] <= 720 || k[1]+1440-j[0] <= 720))
				puts("2");
			else
				puts("4");
		}
	}
	return 0;
}
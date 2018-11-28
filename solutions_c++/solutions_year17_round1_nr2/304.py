#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>

typedef long long ll;

using namespace std;

struct pack {
	int quant;
	int minS, maxS;
};

bool packCompare(pack lhs, pack rhs) { return lhs.quant < rhs.quant; }


int main() {
	int iC=0, nC;
	scanf("%d", &nC);
	for (iC=1; iC<=nC; iC++) {
		int n, p;
		scanf("%d %d", &n, &p);

		int reqs[n];
		for (int i=0; i<n; i++)
			scanf("%d", &reqs[i]);

		pack _packages[n*p];
		pack *packages[n];
		set<int> points;


		for (int i=0; i<n; i++) {
			packages[i] = &_packages[i*p];
			for (int j=0; j<p; j++) {
				scanf("%d", &packages[i][j].quant);

				int minS = packages[i][j].quant / (1.1*reqs[i]) - 1;
				while (110*minS*reqs[i] < 100*packages[i][j].quant) ++minS;
				int maxS = packages[i][j].quant / (0.9*reqs[i]) + 1;
				while (90*maxS*reqs[i] > 100*packages[i][j].quant) --maxS;

				// printf("%d %d\n", minS, maxS);

				packages[i][j].minS = minS;
				packages[i][j].maxS = maxS;

				points.insert(minS);
				points.insert(maxS);
			}

			sort(packages[i], packages[i]+p, packCompare);
		}

		int c = 0;
		for (int point: points) {
			while(1) {
				// printf("%d\n", point);
				bool validPoint=true;

				for (int i=0; i<n; i++) {
					bool foundPack=false;

					for (int j=0; j<p; j++) {
						if (packages[i][j].quant < 0)
							continue;

						// printf("%d %d %d\n", packages[i][j].minS, point, packages[i][j].maxS);

						if (packages[i][j].minS <= point and point <= packages[i][j].maxS) {
							foundPack = true;
							break;
						}
					}

					if (!foundPack) {
						validPoint = false;
						break;
					}
				}

				if (!validPoint)
					break;

				++ c;

				for (int i=0; i<n; i++) {
					for (int j=0; j<p; j++) {
						if (packages[i][j].quant < 0)
							continue;
						if (packages[i][j].minS <= point and point <= packages[i][j].maxS) {
							packages[i][j].quant = -1;
							break;
						}
					}
				}
			}
		}

		printf("Case #%d: %d\n", iC, c);
	}
	return 0;
}
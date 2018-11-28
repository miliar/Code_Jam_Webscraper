#include <cstdio>
using namespace std;

int start[1000], speed[1000];

double getSpeed(int dest, int nHorse)
{
	int dist;
	double t, maxt;
	maxt = 0;

	for (int i=0; i < nHorse; ++i) {
		dist = dest - start[i];
		t = (double)dist / speed[i];

		if (t > maxt)
			maxt = t;
	}
	return dest / maxt;
}

int main()
{
	int tcase;
	int dest, nHorse;
	scanf("%d", &tcase);

	for (int i=1; i<=tcase; ++i) {
		scanf("%d%d", &dest, &nHorse);

		for (int j=0; j < nHorse; ++j) {
			scanf("%d%d", &start[j], &speed[j]); 
		}

		printf("Case #%d: %.6f\n", i, getSpeed(dest, nHorse));
	}
}

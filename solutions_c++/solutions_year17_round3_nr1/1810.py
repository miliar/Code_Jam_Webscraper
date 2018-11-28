#include <cstdio>
#include <algorithm>
using namespace std;

const double PI=3.1415926535897932384626433832795028841971;

pair<int, int> cake[1000];
int nOrdered, nCake;
double cache[1000][1000];

double getUpside(int r)
{
	return (r * (double)r);
}
double getSide(int r, int h)
{
	return (2 * (double)r * h);
}

double getSurface(int r, int h)
{
	return getUpside(r) + getSide(r, h);
}

double getMaxSurface(int idx, int remain)
{
	double surface;
	double &maxSurface = cache[idx][remain];

	if (maxSurface == 0) {
		if (remain == 1) {
			for (int i = idx; i < nCake; ++i) {
				maxSurface = max(maxSurface, getSurface(cake[i].first, cake[i].second));
			}
		}
		else {
			for (int i = idx; i <= nCake - remain; ++i) {
				surface = getSide(cake[i].first, cake[i].second);
				maxSurface = max(maxSurface, surface + getMaxSurface(i+1, remain-1));
			}
		}
	}
	return maxSurface;
}


int main()
{

	int tcase;

	scanf("%d", &tcase);

	for (int i=1; i<=tcase; ++i) {
		scanf("%d%d", &nCake, &nOrdered);

		for (int j=0; j<nCake; ++j) {
			scanf("%d%d", &cake[j].first, &cake[j].second);
		}

		for (int j=0; j<nCake; ++j) {
			for (int k=0; k<nCake; ++k) {
				cache[j][k] = 0;
			}
		}

		auto compare = [](pair<int, int> smaller, pair<int, int> larger)->int {
			return smaller.first < larger.first ||
				(smaller.first == larger.first && smaller.second < larger.second);
		};

		sort(cake, cake + nCake, compare);

		/*
		for(int k=0; k<nCake; ++k) {
			printf("%d %d\n", cake[k].first, cake[k].second);
		}
		printf("\n");
		*/

		printf("Case #%d: %.9f\n", i, PI * getMaxSurface(0, nOrdered));
	}
}

#include <cstdio>

using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for (int cs = 1; cs <= t; ++cs)
	{
		int D,N;
		double maxHorseTime = 0.0;
		scanf("%d%d",&D,&N);
		for (int i = 0; i < N; ++i)
		{
			int k,s;
			scanf("%d%d",&k,&s);
			double horseTime = (double)(D-k) / (double)s;
			if (horseTime > maxHorseTime) {
				maxHorseTime = horseTime;
			}
		}
		printf("Case #%d: %.8lf\n", cs, (double)D / maxHorseTime);
	}
	return 0;
}
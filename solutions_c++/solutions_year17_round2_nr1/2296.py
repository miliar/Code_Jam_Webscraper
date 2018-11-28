#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for (int z=1; z<=t; z++) {

		double max_val = -1.0;

		long long D;
		int N;
		scanf("%lld %d",&D,&N);

		long long initial, speed;
		for (int i=0; i<N; i++) {
			scanf("%lld %lld",&initial, &speed);
			double pembagi = (double)(D-initial)/(double)speed;
			if (pembagi>max_val) {
				max_val = pembagi;
			}
		}

		printf("Case #%d: %.6lf\n",z, (double)D/max_val);
	}
	return 0;
}
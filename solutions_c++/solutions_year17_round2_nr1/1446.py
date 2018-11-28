#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

void proc(int caseno) {
	int d, n;
	double maxtime = 0;
	scanf("%d %d", &d, &n);

	for (int i = 0; i < n; i++) {
		long long int pos, speed;
		scanf("%lld %lld", &pos, &speed);

		double time = (double)(d * speed)  / (double)(d - pos);
		if (maxtime == 0 || time < maxtime)
			maxtime = time;
	}

	printf("Case #%d: %f\n", caseno, maxtime);
}

int main() {
	int c;

	scanf("%d", &c); 
	for (int i = 0; i < c; i++)
		proc(i + 1);
	return 0;
}

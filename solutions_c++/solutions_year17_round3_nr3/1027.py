#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<deque>
#include<queue>
#include<stack>
#include<numeric>
#include<math.h>
#include<set>
#include<map>
#include<fstream>
#define epsilon 0.000000001
#define cosinusa(a, b, c) ((a * a + b * b - c * c) / (2.0 * a * b));
#define infi 1000000000
using namespace std;

double v[64];
double v1[64];
int n;
double doProduct() {
	double res = 1.0;
	for (int i = 0; i  <n; i++) {
		res *= v[i];
	}
	return res;
}

double solve1(double u) {
	memcpy(v, v1, sizeof(v1));

	double step = 1e-5;
	double tmp;
	double prevProd = doProduct();
	while (u > 0) {
		u -= step;
		double curProd = 0;
		double bestProd = -1;
		int bestIdx = -1;
		for (int i = 0; i < n; i++) {
			tmp = v[i];
			v[i] = min(1.0, v[i] + step);
			if (tmp > epsilon)
				curProd = (prevProd / tmp) * v[i];
			else
				curProd = doProduct();
			if (curProd > bestProd) {
				bestProd = curProd;
				bestIdx = i;
			}
			v[i] = tmp;
		}
		v[bestIdx] = min(1.0, v[bestIdx] + step);
	}
	double maxProd = doProduct();
	return maxProd;
}

double solve2(double u) {
	memcpy(v, v1, sizeof(v1));

	sort(v, v + n);
	for (int i = 1; i < n; i++) {
		double missing = 0.0;
		for (int j = 0; j < i; j++) {
			missing += v[i] - v[j];
		}
		if (missing < u) {
			u -= missing;
			for (int j = 0; j < i; j++) {
				v[j] = v[i];
			}
		} else {
			double toAdd = u / (double) (i);
			for (int j = 0; j < i; j++) {
				v[j] += toAdd;
			}
			return doProduct();
		}
	}
	double toAdd = u / (double)n;
	for (int j = 0; j < n; j++) {
		v[j] += toAdd;
	}
	return doProduct();
}
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numTests;
	cin >> numTests;
	for(int testCounter = 0; testCounter < numTests; ++testCounter)
	{
		printf("Case #%d: ", testCounter + 1);
		int k;
		cin >> n >> k;
		double u;
		cin >> u;
		for (int i = 0; i < n; i++) {
			cin >> v1[i];
		}
		//double maxProd = solve1(u);
		double maxProd = solve2(u);
		printf("%.9lf\n", maxProd);
	}
	return 0;
}



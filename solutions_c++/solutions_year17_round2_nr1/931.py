#include <iostream>
#include <cstdio>
#include <stdint.h>
#include <vector>
#include <algorithm>
using namespace std;
void A()
{
	size_t T, D, N;
	vector<size_t> p, s, t;
	scanf("%d", &T);
	for (size_t cnt = 1; cnt <= T; cnt++)
	{
		scanf("%d %d", &D, &N);
		p.clear();
		s.clear();
		t.clear();
		p.resize(N);
		s.resize(N);
		t.resize(N);
		double max_s = 0;
		double max_t = 0;
		double res = 1e30;
		double answer = 1e30;
		double k, s;
		for (int i = 1; i <= N; ++i) {
			scanf("%Lf%Lf", &k, &s);
			double x = (D * s) / (D - k);
			answer = std::min(answer, x);
		}
		printf("Case #%d: %.6lf\n", cnt, answer);
	}
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	A();
	return 0;
}
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	freopen("c-small-1-attempt0.in", "r", stdin);
	freopen("outs.txt", "wb", stdout);
	int data;
	scanf("%d", &data);
	for (int p = 1; p <= data; p++)
	{
		int num, kai;
		double gen;
		scanf("%d%d%lf", &num, &kai, &gen);
		vector<double>vec;
		for (int i = 0; i < num; i++)
		{
			double z;
			scanf("%lf", &z);
			vec.push_back(z);
		}
		sort(vec.begin(), vec.end());
		double beg = 0.0, end = 1.0;
		for (int q = 0; q < 100; q++)
		{
			double med = (beg + end) / 2.0;
			double s = 0;
			for (int i = 0; i < num; i++)s += max(0.0, med - vec[i]);
			if (s < gen)beg = med;
			else end = med;
		}
		double r = 1;
		for (int i = 0; i < num; i++)r *= max(beg, vec[i]);
		printf("Case #%d: %.10lf\n", p, r);
	}
}
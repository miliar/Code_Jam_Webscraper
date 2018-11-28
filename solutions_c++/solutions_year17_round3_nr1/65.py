#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int r[1000], h[1000];
double pi = 3.14159265358979323;
int main()
{
	freopen("a-large.in", "r", stdin);
	freopen("outl.txt", "wb", stdout);
	int data;
	scanf("%d", &data);
	for (int p = 1; p <= data; p++)
	{
		int num, gen;
		scanf("%d%d", &num, &gen);
		for (int i = 0; i < num; i++)scanf("%d%d", &r[i], &h[i]);
		double maxi = 0;
		for (int i = 0; i < num; i++)
		{
			int x = r[i];
			vector<double>v;
			for (int j = 0; j < num; j++)
			{
				if (i != j)
				{
					if (x >= r[j])v.push_back(double(r[j]) * 2.0*pi*double(h[j]));
				}
			}
			sort(v.begin(), v.end());
			reverse(v.begin(), v.end());
			if (v.size() < gen - 1)continue;
			double s = double(r[i])*double(r[i])*pi + double(r[i])*2.0*pi*double(h[i]);
			for (int j = 0; j < gen - 1; j++)s += v[j];
			maxi = max(maxi, s);
		}
		printf("Case #%d: %.10lf\n", p, maxi);
	}
}
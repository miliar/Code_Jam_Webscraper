#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <unordered_map>
#include <math.h>

using namespace std;
void templ()
{
	int T;
	scanf("%d", &T);
	for (int cnt = 1; cnt <= T; cnt++)
	{
		printf("\n", cnt);
	}
}
struct cake
{
	double r, h;
	cake(){}
	cake(double rr, double hh)
	{
		r = rr;
		h = hh;
	}
};
bool cmp(const cake &c1, const cake&c2)
{
	if (c1.r == c2.r) return c1.h > c2.h;
	return c1.r > c2.r;
}
bool cmp1(const double d1, const double d2)
{
	return d1 > d2;
}
void A()
{
	const double pi = 3.14159265358979323846;
	int T;
	scanf("%d", &T);
	int K, N;
	const int max_n = 1001;
	vector<cake> s;
	vector<double> t;
	for (int cnt = 1; cnt <= T; cnt++)
	{
		scanf("%d%d", &N, &K);
		s.clear();
		s.resize(N);
		double final_res = 0;
		for (int i = 0; i < N; i++)
		{
			double h;
			scanf("%lf%lf", &s[i].r, &h);
			s[i].h = 2 * pi * s[i].r * h;
		}
		sort(s.begin(), s.end(), cmp);
		for (int i = 0; i < N - K + 1; i++)
		{
			t.clear();
			for (int j = 0; j < N; j++)
			{
				if (i == j) continue;
				else if (s[i].r >= s[j].r)
				{
					t.push_back(s[j].h);
				}
			}
			if (t.size() < K - 1) continue;
			else
			{
				sort(t.begin(), t.end(), cmp1);
				double res = pi * s[i].r * s[i].r + s[i].h;
				for (int j = 0; j < K - 1; j++)
				{
					res += t[j];
				}
				final_res = max(final_res, res);
			}
			
		}
		
		printf("Case #%d: %.9lf\n", cnt, final_res);
	}
}
void B()
{

}
void C()
{

}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	//printf("hello world\n");
	A();
	//B();
	//C();
	return 0;
}
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
bool cmp2(const pair<int, int> p1, const pair<int, int> p2)
{
	return p1.first < p2.first;
}
struct state
{
	int change;
	int min_boy;
	int max_boy;
	state(){}
};
void B()
{
	int T;
	scanf("%d", &T);
	vector<std::pair<int, int>> b1, b2;
	vector<pair<int, int>> time_used;
	vector<pair<int, int>> time_remain;
	vector<state> dp[3];
	for (int cnt = 1; cnt <= T; cnt++)
	{
		int res;
		int s, t;
		scanf("%d%d", &s, &t);
		b1.clear();
		b2.clear();
		b1.resize(s);
		b2.resize(t);
		int boy_cost = 0;
		int girl_cost = 0;
		time_used.clear();
		time_remain.clear();
		for (int i = 0; i < 3; i++)
		{
			dp[i].clear();
		}
		
		for (int i = 0; i < s; i++)
		{
			scanf("%d%d", &b1[i].first, b1[i].second);
			boy_cost += b1[i].second - b1[i].first;
			time_used.push_back(make_pair(b1[i].first, b1[i].second));
		}
		sort(b1.begin(), b1.end(), cmp2);
		for (int i = 0; i < t; i++)
		{
			scanf("%d%d", &b2[i].first, b2[i].second);
			girl_cost += b2[i].second - b2[i].first;
			time_used.push_back(make_pair(b2[i].first, b2[i].second));
		}
		sort(b2.begin(), b2.end(), cmp2);
		sort(time_used.begin(), time_used.end(), cmp2);
		int pre = 0;
		for (int i = 0; i < time_used.size(); i++)
		{
			if (pre != time_used[i].first)
			{
				time_remain.push_back(make_pair(pre, time_used[i].first));
			}
		}
		for (int i = 0; i < 3; i++)
		{
			dp[i].resize(time_remain.size());
		}
		if (time_remain.size() == 0)
		{

		}
		else
		{
			// first time gap
			int gap = time_remain[0].second - time_remain[0].first;
			if (time_remain[0].first == b1[0].first)
			{
				// start from boy
			

				dp[0][0].change = 0;
				if (boy_cost + gap > 720)
				{
					dp[0][0].min_boy = 721;
					dp[0][0].max_boy = 721;
				}
				else
				{
					dp[0][0].min_boy = boy_cost + gap;
					dp[0][0].max_boy = boy_cost + gap;
				}
			}
			else
			{
				// start from girl

			}


			//last time gap

		}
		//int res;
		//printf("Case #%d: %d\n", cnt, res);
	}
}
bool DoubleEqual(double d1, double d2)
{
	const double eps = 1e-6;
	if (abs(d1 - d2) < eps)
	{
		return true;
	}
	return false;
}
void C()
{
	int T;
	scanf("%d", &T);
	vector<double> v;
	const double eps = 1e-6;
	for (int cnt = 1; cnt <= T; cnt++)
	{
		int N, K;
		double train;
		
		scanf("%d%d", &N, &K);
		scanf("%lf", &train);
		v.clear();
		v.resize(N);
		for (int i = 0; i < N; i++)
		{
			scanf("%lf", &v[i]);
		}
		while (abs(train) > eps)
		{
			sort(v.begin(), v.end());
			double prev = v[0];
			int the_same = 1;
			for (int i = 1; i < v.size(); i++)
			{
				if (DoubleEqual(v[i], prev))
				{
					the_same++;
				}
				else
				{
					break;
				}
			}
			if (the_same < v.size())
			{
				double gap = v[the_same] - v[0];
				if (gap * the_same < train)
				{
					for (int i = 0; i < the_same; i++)
					{
						v[i] += gap;
					}
					train -= gap * the_same;
				}
				else
				{
					for (int i = 0; i < the_same; i++)
					{
						v[i] += train / the_same;
					}
					train = 0;
					break;
				}
			}
			else
			{
				for (int i = 0; i < the_same; i++)
				{
					v[i] += train / the_same;
					if (v[i] > 1)
					{
						v[i] = 1;
					}
				}
				train = 0;
				break;
			}
		}
		double res = 1;
		for (int i = 0; i < N; i++)
		{
			res *= v[i];
		}
		printf("Case #%d: %.6lf\n", cnt, res);
	}
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	//printf("hello world\n");
	//A();
	//B();
	C();
	return 0;
}
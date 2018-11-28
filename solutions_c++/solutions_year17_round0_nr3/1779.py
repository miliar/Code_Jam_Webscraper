#include <algorithm>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

//#define SMALL_INPUT
#define LARGE_INPUT

#if defined(SMALL_INPUT)
std::ifstream fin("D:\\develop\\GCJ\\data\\small.in");
std::ofstream fout("D:\\develop\\GCJ\\data\\small.out");
#define gin fin
#define gout fout
#elif defined(LARGE_INPUT)
std::ifstream fin("D:\\develop\\GCJ\\data\\large.in");
std::ofstream fout("D:\\develop\\GCJ\\data\\large.out");
#define gin fin
#define gout fout
#else
#define gin cin
#define gout cout
#endif

class Solver
{
public:
	void Solve2(int64_t n, int64_t k, int64_t &a, int64_t &b)
	{
		if (k == 1)
		{
			if (n % 2 == 1)
			{
				a = b = (n - 1) / 2;
			}
			else
			{
				a = n / 2;
				b = n / 2 - 1;
			}

			return;
		}

		if (n % 2 == 1)
		{
			if (k % 2 == 1)
			{
				Solve2((n - 1) / 2, (k - 1) / 2, a, b);
			}
			else
			{
				Solve2((n - 1) / 2, k / 2, a, b);
			}
		}
		else
		{
			if (k % 2 == 1)
			{
				Solve2(n / 2 - 1, (k - 1) / 2, a, b);
			}
			else
			{
				Solve2(n / 2, k / 2, a, b);
			}
		}
	}

	void Solve(int64_t n, int64_t k, int64_t &a, int64_t &b)
	{
		vector<int64_t> ls(n + 2), rs(n + 2), mi(n + 2), ma(n + 2);

		for (int64_t i = 1; i <= n; ++i)
		{
			ls[i] = i - 1;
			rs[i] = n - i;

			mi[i] = min(ls[i], rs[i]);
			ma[i] = max(ls[i], rs[i]);
		}

		for (int64_t i = 0; i < k; ++i)
		{
			Enter(ls, rs, mi, ma, n, a, b);
		}
	}

private:
	void Enter(vector<int64_t> &ls, vector<int64_t> &rs, vector<int64_t> &mi, vector<int64_t> &ma, int64_t n, int64_t &a, int64_t &b)
	{
		int64_t k = 0;
		int64_t u = -1, v = -1;
		for (int64_t i = 1; i <= n; ++i)
		{
			if (mi[i] < 0 || ma[i] < 0) continue;

			if (mi[i] > u || mi[i] == u && ma[i] > v)
			{
				k = i;
				u = mi[i];
				v = ma[i];
			}
		}

		a = max(u, v);
		b = min(u, v);

		ls[k] = rs[k] = mi[k] = ma[k] = -1;

		set<int64_t> ss;
		for (int64_t i = k + 1, j = 0; i <= n; ++i, ++j)
		{
			if (ls[i] < 0) break;
			ls[i] = j;

			ss.insert(i);
		}

		for (int64_t i = k-1, j = 0; i >= 1; --i, ++j)
		{
			if (rs[i] < 0) break;
			rs[i] = j;

			ss.insert(i);
		}

		for (auto ite = ss.begin(); ite != ss.end(); ++ite)
		{
			mi[*ite] = min(ls[*ite], rs[*ite]);
			ma[*ite] = max(ls[*ite], rs[*ite]);
		}
	}
};

int main()
{
	int t;
	gin >> t;

	for (int i = 1; i <= t; ++i)
	{
		int64_t n, k, a, b;
		gin >> n >> k;

		Solver sovler;
		sovler.Solve2(n, k, a, b);

		gout << "Case #" << i << ": ";
		gout << a << " " << b << "\n";
	}

	return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Problem
{
	int D, N;
	vector<pair<int, int>> KS;
	double speed;

	void solve()
	{
		sort(KS.begin(), KS.end());

		double mt = 1.0 * (D - KS[0].first) / KS[0].second;
		double ms = 1.0 * D / mt;

		for (int i = 1; i < N; ++i)
		{
			double t = 1.0 * (D - KS[1].first) / KS[1].second;

			if (mt < t)
			{
				mt = t;
				ms = 1.0 * D / mt;
			}
		}

		speed = ms;
	}
};

istream &operator >>(istream &in, Problem &p)
{
	in >> p.D >> p.N;

	for (int i = 0; i < p.N; ++i)
	{
		int k, s;
		in >> k >> s;
		p.KS.push_back(make_pair(k, s));
	}

	return in;
}

ostream &operator <<(ostream &out, Problem &p)
{
	out << fixed << setprecision(7) << p.speed;
	return out;
}

void test()
{
	int T = 0;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		Problem p;
		cin >> p;
		p.solve();
		cout << "Case #" << i + 1 << ": " << p << endl;
	}
}

int main()
{
//	freopen("in", "rt", stdin);

	test();
	return 0;
}

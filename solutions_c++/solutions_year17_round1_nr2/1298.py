#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Problem
{
	int N, P;
	vector<int> R;
	vector<vector<int>> Q;
	int	K;

	void solve()
	{
		K = 0;

		for (int i = 0; i < N; ++i)
			sort(Q[i].begin(), Q[i].end());

		for (int i = 0; i < Q[0].size(); ++i)
		{
			int mn = Q[0][i] / (R[0] * 1.1), mx = Q[0][i] / (R[0] * 0.9);

			for (int q = mn; q <= mx; ++q)
			{
				if (0.9 * R[0] * q <= Q[0][i] && Q[0][i] <= 1.1 * R[0] * q)
				{
					vector<int> indices;
					indices.reserve(N);
					indices.push_back(i);

					for (int j = 1; j < N && indices.size() == j; ++j)
					{
						for (int k = 0; k < Q[j].size(); ++k)
						{
							if (0.9 * R[j] * q <= Q[j][k] && Q[j][k] <= 1.1 * R[j] * q)
							{
								indices.push_back(k);
								break;
							}
						}
					}

					if (indices.size() == N)
					{
						for (int j = 0; j < N; ++j)
						{
							Q[j].erase(Q[j].begin() + indices[j]);
						}

						++K;
						--i;
						break;
					}
				}
			}
		}
	}
};

istream &operator >>(istream &in, Problem &p)
{
	in >> p.N >> p.P;
	p.R.clear();

	int x;
	for (int i = 0; i < p.N; ++i)
	{
		in >> x;
		p.R.push_back(x);
	}

	p.Q.clear();
	for (int i = 0; i < p.N; ++i)
	{
		p.Q.push_back(vector<int>());

		for (int j = 0; j < p.P; ++j)
		{
			in >> x;
			p.Q[i].push_back(x);
		}
	}

	return in;
}

ostream &operator <<(ostream &out, Problem &p)
{
	out << p.K;
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
//	freopen("test.in", "rt", stdin);

	test();
	return 0;
}

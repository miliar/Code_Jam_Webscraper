#include <iostream>
#include <map>

using namespace std;

struct Problem
{
	long long N, K;
	map<long long, long long, greater<long long>> distances;
	pair<long long, long long> result;

	void solve()
	{
		distances[N] = 1;

		for (int i = 0; K > 0; ++i)
		{
			auto it = distances.begin();
			const long long distance = it->first;
			const long long count = it->second;

			const long long left = (distance - 1) / 2;
			const long long right = distance - left - 1;

			if (K > count)
			{
				distances[left] += count;
				distances[right] += count;

				distances.erase(it);
				K -= count;
			}
			else
			{
				result.second = left;
				result.first = right;

				cerr << "Solved in " << i << " steps" << endl;
				break;
			}
		}
	}
};

istream &operator >>(istream &in, Problem &p)
{
	in >> p.N >> p.K;
	return in;
}

ostream &operator <<(ostream &out, Problem &p)
{
	out << p.result.first << " " << p.result.second;
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
	test();
	return 0;
}

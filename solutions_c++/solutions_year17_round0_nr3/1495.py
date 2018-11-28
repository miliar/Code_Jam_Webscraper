#include <map>
#include <iostream>
using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int cases;
	cin >> cases;
	for (int _case = 0; _case < cases; _case++)
	{
		long long n, k;
		cin >> n >> k;

		map<long long, long long> m;
		m.insert(make_pair(n, 1));
		for (;;)
		{
			auto p = *(m.rbegin());
			if (p.second < k)
			{
				k -= p.second;
				m.erase(p.first);
				if (p.first % 2)
					m[p.first / 2] += 2 * p.second;
				else
				{
					m[p.first / 2] += p.second;
					m[p.first / 2 - 1] += p.second;
				}
			}
			else
			{
				cout << "Case #" << _case + 1 << ": ";
				if (p.first % 2)
					cout << p.first / 2 << ' ' << p.first / 2 << endl;
				else
					cout << p.first / 2 << ' ' << p.first / 2 - 1 << endl;
				break;
			}
		}
	}

	return 0;
}
#include <vector>
#include <iostream>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int cases;
	cin >> cases;
	for (int _case = 1; _case <= cases; _case++)
	{
		int r, c;
		cin >> r >> c;
		vector<string> cake(r);
		for (int i = 0; i < r; i++)
			cin >> cake[i];

		for (int i = 0; i < r; i++)
		{
			vector<int> e;
			for (int j = 0; j < c; j++)
				if (cake[i][j] != '?')
					e.push_back(j);

			int last = 0;
			for (int j = 0; j < e.size(); j++)
			{
				for (int k = last; k < e[j]; k++)
					cake[i][k] = cake[i][e[j]];
				last = e[j] + 1;
			}

			if (e.size() > 0)
				for (int j = last; j < c; j++)
					cake[i][j] = cake[i][e.back()];
		}

		vector<int> e;
		for (int i = 0; i < r; i++)
			if (cake[i][0] != '?')
				e.push_back(i);

		int last = 0;
		for (int i = 0; i < e.size(); i++)
		{
			for (int j = last; j < e[i]; j++)
				cake[j] = cake[e[i]];
			last = e[i] + 1;
		}

		for (int i = last; i < r; i++)
			cake[i] = cake[e.back()];

		cout << "Case #" << _case << ":" << endl;
		for (int i = 0; i < r; i++)
			cout << cake[i] << endl;
	}

	return 0;
}
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <climits>
#include <ctime>
#include <algorithm>
#include <string>
#include <set>
#include <unordered_set>
#include <cmath>
#include <map>
#include <cstdio>

using namespace std;

int mini(int tab[6])
{
	int m = 10000;
	int indice = -1;

	for (int i = 0; i < 6; i++)
	{
		if (tab[i] < m && tab[i] > 0)
		{
			m = tab[i];
			indice = i;
		}
	}
	return indice;
}

int getNext(int tab[6], int previous, int first)
{
	int m = 0;
	int indice = -1;

	for (int i = 0; i < 6; i++)
	{
		if (tab[i] > m && i != previous)
		{
			m = tab[i];
			indice = i;
		}
		else if (tab[i] >= m && i == first && i != previous && tab[i] > 0)
		{
			m = tab[i];
			indice = i;
		}
	}
	return indice;
}

int main()
{
	int t;
	cin >> t;


	for (int i = 0; i < t; i++)
	{
		int n;
		cin >> n;

		int tab[6];

		for (int i = 0; i < 6; i++)
		{
			cin >> tab[i];
		}

		vector<int> ordre;

		int previous = mini(tab);
		int first = previous;

		ordre.push_back(previous);
		tab[previous]--;
		n--;
		bool impossible = false;

		while (n > 0)
		{
			previous = getNext(tab, previous, first);

			if (previous == -1)
			{
				impossible = true;
				break;
			}

			tab[previous]--;
			n--;
			ordre.push_back(previous);
		}
        cout << "Case #" << i + 1 << ": ";

		if (impossible)
			cout << "IMPOSSIBLE" << endl;
		else
		{
			for (int i = 0; i < ordre.size(); i++)
			{
				if (ordre[i] == 0)
					cout << "R";
				else if (ordre[i] == 2)
					cout << "Y";
				else
					cout << "B";
			}
			cout << endl;
		}


	}

	return 0;
}
























#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int minimumNumberOfFlips(string cakes, int flipper)
{
	int n = cakes.size();
	int flips = 0;
	for (int i = 0; i < n - flipper + 1; ++ i)
	{
		if (cakes[i] == '-')
		{
			for (int j = 0; j < flipper; ++ j)
			{
				cakes[i + j] = cakes[i + j] == '+'? '-' : '+';
			}
			++ flips;
		}
	}
	bool possible = true;
	for (int i = n - flipper + 1; i < n; ++ i)
	{
		if (cakes[i] == '-')
		{
			possible = false;
		}
	}
	if (!possible) return -1;
	return flips;
}

int main()
{
	int tc;
	cin >> tc;
	for (int i = 1; i <= tc; ++ i)
	{
		string cakes; int flipper;
		cin >> cakes >> flipper;
		int flips = minimumNumberOfFlips(cakes, flipper);
		cout << "Case #" << i << ": ";
		if (flips == -1) cout << "IMPOSSIBLE" << "\n";
		else cout << flips << "\n";
	}
}


#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool solve(int i, string& n)
{
	if (i + 1 < n.size())
	{
		if (n[i] <= n[i + 1])
		{
			if (solve(i + 1, n))
				return true;
			if (n[i] > n[i + 1])
			{
				n[i]--;
				n[i + 1] = '9';
				return false;
			}
		}
		else
		{
			n[i]--;
			fill(n.begin() + i + 1, n.end(), '9');
			return false;
		}
	}
	return true;
}

int main()
{
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++)
	{
		string n;
		cin >> n;
		solve(0, n);
		cout << "Case #" << c << ": " << stoll(n) << endl;
	}
}

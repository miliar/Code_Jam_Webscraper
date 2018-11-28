#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	int k;
	string s;
	bool isPossible;
	int moves;

	cin >> t;

	for (int x = 1; x<=t; ++x) {
		cin >> s;
		cin >> k;
		isPossible = true;
		moves = 0;
		for (int i = 0; i <= s.length()-k; ++i)
		{
			if (s[i] == '-')
			{
				moves++;
				for (int j = i; j < k+i; ++j)
				{
					if (s[j] == '-')
					{
						s[j] = '+';
					}
					else
					{
						s[j] = '-';
					}
				}
			}
		}
		for (int i = s.length()-k; i < s.length(); ++i)
		{
			if (s[i] == '-')
			{
				isPossible = false;
				break;
			}
		}
		cout << "Case #" << x << ": ";
		if (isPossible)
		{
			cout << moves << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}

	return 0;
}
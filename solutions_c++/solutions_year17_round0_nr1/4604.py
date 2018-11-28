#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		string row;
		int k, result = 0;

		cin >> row >> k;
		for (int i = 0; i < row.length(); ++i)
		{
			if (row[i] == '-')
			{
				if (i + k > row.length())
				{
					result = -1;
					break;
				}

				for (int j = i; j < i + k; ++j)
				{
					if (row[j] == '-')
						row[j] = '+';
					else
						row[j] = '-';
				}
				++result;
			}
		}

		cout << "Case #" << t << ": ";
		if (result == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << result << '\n';
	}
	return 0;
}

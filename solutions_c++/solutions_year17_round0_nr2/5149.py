#include <iostream>
#include <string>

using namespace std;

#define REP(i, n) for (int i = 0; i < n; ++i)
#define FOR(i, a, b) for (int i = a; i <= b; ++i)
#define FORD(i, a, b) for (int i = a; i >= b; --i)

int main()
{
	int T;

	cin >> T;

	cin.ignore();

	REP(t, T)
	{
		string number;

		getline(cin, number);

		t = t;

		REP(i, number.length() - 1)
		{
			if (number[i] > number[i + 1])
			{
				FORD(j, i, 1)
				{
					if (--number[j] >= number[j - 1])
						break;

					else
						number[j] = '9';

					if (j == 1)
						--number[0];
				}

				if (i == 0)
					--number[0];

				FOR(j, i + 1, number.length() - 1)
					number[j] = '9';

				break;
			}
		}

		cout << "Case #" << t + 1 << ": ";

		FOR(i, (number[0] == '0' ? 1 : 0), number.length() - 1)
			cout << number[i];

		cout << endl;
	}

	return 0;
}
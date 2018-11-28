#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int test, Case = 1;

	cin >> test;

	while (test--)
	{
		bool ok = true;

		int k, count = 0;

		string s;

		cin >> s >> k;

		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '-' && (i + k - 1) < s.size())
			{
				count++;

				for (int j = i; j < i + k; j++)
				{
					s[j] == '-' ? s[j] = '+' : s[j] = '-';
				}
			}
		}

		for (int i = 0; i < s.size() && ok; i++)
		{
			if (s[i] == '-') ok = false;
		}

		if (ok) cout << "Case #" << Case++ << ": " << count << endl;

		else cout << "Case #" << Case++ << ": " << "IMPOSSIBLE" << endl;
	}
}
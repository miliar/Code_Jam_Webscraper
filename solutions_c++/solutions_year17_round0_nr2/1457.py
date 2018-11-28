#include <iostream>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int cases;
	cin >> cases;
	for (int _case = 0; _case < cases; _case++)
	{
		long long n;
		cin >> n;
		string s = to_string(n);

		for (int i = 0; i + 1 < s.length(); i++)
			if (s[i] > s[i + 1])
			{
				int p = i - 1;
				while (p >= 0 && s[p] == s[i])
					p--;

				s[p + 1] = (char)((int)s[p + 1] - 1);
				for (int j = p + 2; j < s.length(); j++)
					s[j] = '9';

				break;
			}

		cout << "Case #" << _case + 1 << ": " << stoll(s) << endl;
	}
	return 0;
}
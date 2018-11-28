#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int main()
{
	int T, k;
	string s;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		cin >> s >> k;
		int ans = 0;
		int j = 0;
		bool change[1000] = { false };
		bool impossible = false;
		for (j; j < s.length(); j++)
		{
			if (change[j])
			{
				if (s[j] == '-') s[j] = '+';
				else s[j] = '-';
			}

			if (s[j] == '-')
			{
				if (j > s.length() - k)
				{
					impossible = true;
					break;
				}
				else
				{
					ans++;
					for (int t = j + 1; t < j + k; t++)
						change[t] = !change[t];
				}
			}
		}
		printf("Case #%d: ",i);
		if (impossible)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;

	}
	return 0;
}
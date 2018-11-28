#include <iostream>

using namespace std;

bool rot[1010];

int main()
{
	int tt;
	cin >> tt;
	for (int tc = 1; tc <= tt; tc++)
	{
		cout << "Case #" << tc << ": ";
		string s;
		int k;
		cin >> s >> k;
		int n = s.length();
		int rem = 0;
		int res = 0;
		for (int i = 0; i < n; i++)
		{
			if (i >= k)
				rem -= rot[i - k];
			rot[i] = (rem + (s[i] == '-')) % 2;
			if (i + k <= n)
			{
				res += rot[i];
				rem += rot[i];
			} 
			else if (rot[i])
			{
				res = -1;
				break;
			}
		}
		if (res == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}
}

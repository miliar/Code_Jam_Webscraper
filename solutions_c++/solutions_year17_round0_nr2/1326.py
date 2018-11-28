#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		string s;
		cin >> s;
		int x[20];
		x[0] = s[0] - '0';
		bool extracted = false;
		for (int i = 1; i < s.length(); ++i)
		{
			if (extracted)
			{
				x[i] = 9;
				continue;
			}
			x[i] = s[i] - '0';
			int j = i;
			while ((x[j] < x[j - 1]) && (j > 0))
			{
				x[j] = 9;
				--x[j - 1];
				--j;
				extracted = true;
			}
		}
		long long ans = 0;
		for (int i = 0; i < s.length(); ++i)
		{
			ans *= 10;
			ans += x[i];
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
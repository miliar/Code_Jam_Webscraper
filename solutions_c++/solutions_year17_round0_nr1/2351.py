#include <bits/stdc++.h>
using namespace std;
typedef long long ll;


int main()
{
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int T = 0; T < t; T++)
	{
		cout << "Case #" << T+1 << ": ";
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		for (int i=0; i<(int)s.size(); i++)
			if (s[i] == '-')
			{
				if (i + k > (int)s.size())
				{
					ans = -1;
					break;
				}
				ans++;
				for (int j=0; j<k; j++)
					s[i+j] = (s[i+j] == '-' ? '+' : '-');
			}
		if (ans == -1)
			cout << "IMPOSSIBLE\n";
		else
			cout << ans << "\n";
	}


	return 0;
}

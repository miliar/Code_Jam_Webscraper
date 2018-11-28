#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		string s;
		int K;
		cin >> s >> K;
		int cnt = 0;
		for(int i = 0; i <= s.size() - K; ++i)
		{
			if(s[i] == '+')
				continue;

			++cnt;

			for(int j = 0; j < K; ++j)
			{
				if(s[i+j] == '+')
					s[i+j] = '-';
				else
					s[i+j] = '+';
			}
		}

		bool good = true;
		for(int i = 0; i < s.size(); ++i)
			if(s[i] == '-')
				good = false;

		if(good)
			cout << cnt << "\n";
		else
			cout << "IMPOSSIBLE\n";
	}
}

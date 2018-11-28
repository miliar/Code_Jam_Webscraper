#include <bits/stdc++.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		string S;
		int K;
		cin >> S >> K;
		int S_len = S.size();

		int step = 0;
		for (int i = 0; i <= (S_len-K); i++)
		{
			if (S[i] == '-')
			{
				for (int j = i; j < (i+K); j++)
				{
					S[j] = (S[j] == '-') ? '+' : '-';
				}
				step++;
			}
		}

		int flag = 0;
		for (int i = 0; i < S_len; i++)
		{
			if (S[i] != '+')
			{
				flag = 1;
				break;
			}
		}

		if (flag == 0)
		{
			printf("Case #%d: %d\n", t,step);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
	}
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

unsigned long long f(string st)
{
	unsigned long long n = 0, i = 0;
	while (st[i] != '\0')
	{
		n = n * 10 + ((int)st[i] - 48);
		i++;
	}
	return n;
}

int main()
{
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++)
	{
		string S;
		cin >> S;
		int flag = 0;
		if (S.size() == 1)
		{
			cout << "Case #" << tt << ": " << S << endl;
			continue;
		}
		for (int i = 1; i < S.size(); i++)
		{
			if (S[i] < S[i - 1])
			{
				flag = 1;
				break;
			}
		}
		if (flag == 0)
		{
			cout << "Case #" << tt << ": " << f(S) << endl;
		}
		else
		{
			for (int i = 0; i < S.size() - 1; i++)
			{
				if (S[i] >= S[i + 1])
				{
					S[i] = S[i] - 1;
					for (int j = i + 1; j < S.size(); j++)
					{
						S[j] = '9';
					}
					break;
				}
			}
			cout << "Case #" << tt << ": " << f(S) << endl;
		}
	}
	return 0;
}

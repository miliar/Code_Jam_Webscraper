#include <bits/stdc++.h>
using namespace std;
string S;
int K, i;
long long hitung, it;
bool found = false;
int main()
{
	int T;
	cin >> T;
	for (int x = 1; x <= T; ++x)
	{
		cin >> S >> K;
		hitung = 0;
		for (i = 0; i < S.size()-K+1; ++i)
		{
			if (S[i] == '-')
			{
				++hitung;
				it = K;
				for (int j = i; it--; ++j)
				{
					if (S[j] == '-')
					{
						S[j] = '+';
					}
					else
					{
						S[j] = '-';
					}
				}
			}
		}
		found = false;
		for (i = 0; i < S.size() && !found; ++i)
		{
			found = (S[i] == '-');
		}
		cout << "Case #" << x << ": ";
		if (!found)
		{
			cout << hitung << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
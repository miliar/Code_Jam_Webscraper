#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int tcase = 1; tcase <= T; ++tcase)
	{
		printf("Case #%d: ", tcase);
		
		string arr;
		int K;
		cin >> arr >> K;
		int ans = 0;
		for (size_t i = 0; i < arr.length() - K + 1; ++i)
		{
			if (arr[i] == '-')
			{
				++ans;
				for (size_t j = i; j < i + K; ++j)
				{
					if (arr[j] == '+')
						arr[j] = '-';
					else
						arr[j] = '+';
				}
			}
		}
		for (size_t i = arr.length() - K + 1; i < arr.length(); ++i)
			if (arr[i] != '+')
			{
				ans = -1;
				break;
			}
		if (ans == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}

	return 0;
}

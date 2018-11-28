#include <string>
#include <cstdio>
#include <iostream>
using namespace std;

template <typename T>
void print(T in, int t)
{
	cout << "Case #" << t << ": " << in << endl;
}

int main()
{
	int tce; cin >> tce;
	for (int tc = 1; tc <= tce; tc++)
	{
		string s; cin >> s;
		int pak; cin >> pak;
		int end = s.length() - 1;
		int flag = 0;
		int stat = 0;

		for (int sub = 0; sub <= end; sub++)
		{
			if (s[sub] == '+')
			{
				continue;
			}

			if (s[sub] == '-')
			{
				if (sub + pak > end + 1)
				{
					print("IMPOSSIBLE", tc);
					stat = 1;
					break;
				}

				for (int cnt = sub; cnt < sub + pak; cnt++)
				{
					if (s[cnt] == '-')
					{
						s[cnt] = '+';
						continue;
					}
					if (s[cnt] == '+')
					{
						s[cnt] = '-';
						continue;
					}
				}

				flag++;
			}
		}
		if (stat == 0)
			print(flag, tc);

	}

	return 0;
}
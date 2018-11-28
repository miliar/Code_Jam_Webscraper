#include <cstdio>
#include <iostream>
#include <cstring>
#define NMAX 30
using namespace std;

FILE* in = freopen("date.in", "r", stdin);
FILE* out = freopen("date.out", "w", stdout);
int T;
char N[NMAX];
int main()
{
	int offset = 0;
	cin >> T;
	for (int test = 1; test <= T; test++)
	{
		cin >> N;
		int len = strlen(N);
		offset = 0;
		for (int i = 0; i < len - 1; i++)
		{
			// found an inversion
			if (N[i] > N[i + 1])
			{
				N[i]--;
				// while there are equals behind
				if (N[i] == '0')
				{
					offset = 1;
					for (int j = 1; j < len; j++)
						N[j] = '9';
					break;
				}
				int j;
				for (j = i - 1; N[j] == N[i] + 1 && j >= 0; j--)
					N[j]--;
				// if there was at least one
				if (j != i - 1)
				{
					for (int k = j + 2; k < len; k++)
						N[k] = '9';
				}

				else {
					for (int j = i + 1; j < len; j++)
						N[j] = '9';
				}
				break;
			}
		}
		cout << "Case #" << test << ": ";
		cout << N + offset << '\n';
	}
	return 0;
}
#include <bits/stdc++.h>
using namespace std;
const int N = 1005;

const int R = 1;
const int Y = 2;
const int B = 4;
const int O = R | Y;
const int G = Y | B;
const int V = R | B;

int s[N];

int main()
{
	int T, n, r, o, y, g, b, v;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas)
	{
		memset(s, 0, sizeof s);
		scanf("%d", &n);
		scanf("%d%d%d%d%d%d", &a[R], &a[O], &a[Y], &a[G], &a[B], &a[V]);
		for (int i = 1; i <= 6; ++i)
			if (a[i])
			{
				s[0] = i;
				break;
			}
		for (int i = 1; i < n; ++i)
		{
			if (s[i-1] == O)
			{
			}
			else if (s[i-1] == G)
			{
			}
			else if (s[i-1] == V)
			{
			}
			else if (s[i-1] == R)
			{
			}
			else if (s[i-1] == Y)
			{
			}
			else if (s[i-1] == B)
			{
			}
		}
	}
	return 0;
}

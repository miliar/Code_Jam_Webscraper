#include <cstdlib>
#include <iostream>
#include <cstring>

using namespace std;

const char color[] = "?RYOBVG";
const int R = 1, Y = 2, B = 4, O = R | Y, G = Y | B, V = B | R;
int N, a[7], ans[1005];
inline int l(int x) { return x - 1 > 0 ? x - 1 : N ; }
inline int r(int x) { return x + 1 <= N ? x + 1 : 1; }
void Solve()
{
	memset(ans, 0, sizeof(ans));
	cin >> N;
	cin >> a[R] >> a[O] >> a[Y] >> a[G] >> a[B] >> a[V];
	int index = 1;
	for (int i = 1; i <= a[O] && index <= N; index += 2, ++i) ans[index] = O;
	if (a[O]) ++index;
	for (int i = 1; i <= a[G] && index <= N; index += 2, ++i) ans[index] = G;
	if (a[G]) ++index;
	for (int i = 1; i <= a[V] && index <= N; index += 2, ++i) ans[index] = V;
	for (int i = 1; i <= N; ++i)
		switch (ans[i])
		{
			case O: case G: case V:
				if ((ans[l(i)] && ans[l(i)] != 7 - ans[i]) || (ans[r(i)] && ans[r(i)] != 7 - ans[i]))
				{
					cout << "IMPOSSIBLE" << endl;
					return;
				}
				ans[l(i)] = ans[r(i)] = 7 - ans[i]; break;
			default: break;
		}
	for (int i = 1; i <= N; ++i)
		switch (ans[i])
		{
			case R: case Y: case B: --a[ans[i]]; break;
			default: break;
		}
	int s = 1, e = N;
	while (ans[s]) ++s;
	while (ans[e]) --e;
	if (s == 1)
	{
		if (a[R] >= a[Y] && a[R] >= a[B]) ans[s] = R;
		else if (a[Y] >= a[R] && a[Y] >= a[B]) ans[s] = Y;
		else ans[s] = B;
		--a[ans[s]];
		++s;
	}
	for (int i = s; i <= e; ++i)
		switch (ans[i - 1])
		{
			case R:
				if (a[Y] > a[B] || (a[Y] == a[B] && ans[r(e)] == Y))
					ans[i] = Y, --a[Y];
				else
					ans[i] = B, --a[B];
				break;
			case Y:
				if (a[R] > a[B] || (a[R] == a[B] && ans[r(e)] == R))
					ans[i] = R, --a[R];
				else
					ans[i] = B, --a[B];
				break;
			case B:
				if (a[R] > a[Y] || (a[R] == a[Y] && ans[r(e)] == R))
					ans[i] = R, --a[R];
				else
					ans[i] = Y, --a[Y];
				break;
		}
	if (a[R] < 0 || a[Y] < 0 || a[B] < 0 || ans[e] == ans[r(e)])
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	for (int i = 1; i <= N; ++i)
		cout << color[ans[i]];
	cout << endl;
}

int T;
int main()
{
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		Solve();
	}
	return 0;
}

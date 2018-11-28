#include <iostream>
#include <algorithm>

using namespace std;

struct _magic_
{
	double r, h;
	double power, sp;
	int id;
};

bool cmp(_magic_ m1, _magic_ m2)
{
	if (m1.r != m2.r)
		return m1.r < m2.r;
	if (m1.h != m2.h)
		return m1.h < m2.h;
	return m1.id < m2.id;
}

bool cmp2(_magic_ m1, _magic_ m2)
{
	if (m1.sp != m2.sp)
		return m1.sp > m2.sp;
	return m1.id < m2.id;
}

const double pi = 3.14159265358979;
const int Max = 1111;
int n, k;
_magic_ m[Max];

void solve(int num)
{
	cin >> n >> k;
	for (int i = 1; i <= n; i++)
	{
		cin >> m[i].r >> m[i].h;
		m[i].power = (pi * m[i].r * m[i].r) + (2.0 * pi * m[i].r * m[i].h);
		m[i].sp = 2.0 * pi * m[i].r * m[i].h;
		m[i].id = i;
	}
	cout << "Case #" << num << ": ";
	double answer = 0;
	for (int i = n; i >= k; i--)
	{
		sort(m + 1, m + n + 1, cmp);
		double result = m[i].power;
		if (k > 1)
		{
			sort(m + 1, m + i, cmp2);
			for (int j = 1; j <= k - 1; j++)
			{
				result += m[j].sp;
			}
		}
		if (result > answer)
			answer = result;
	}
	cout.precision(8);
	cout << fixed << answer << endl;
	return;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}
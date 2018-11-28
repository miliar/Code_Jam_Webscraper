#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <set>
#include <algorithm>
#include <map>
#include <cmath>
#include <vector>
#include <queue>
#include <iomanip>
#include <string>

using namespace std;

typedef long long ll;

string t;

struct uni
{
	int n;
	char c;
};

bool operator<(const uni& a, const uni& b)
{
	if (a.n == b.n && t.length()>0)
		return a.c == t[0];
	return a.n > b.n;
}

uni a[10];

void solve()
{
	t = "";
	int n;
	cin >> n;
	for (int i = 1; i <= 6; i++)
		cin >> a[i].n;

		a[1].c = 'R';
		a[2].c = 'O';
		a[3].c = 'Y';
		a[4].c = 'G';
		a[5].c = 'B';
		a[6].c = 'V';

		if (n == 1)
		{
			sort(a + 1, a + 7);
			cout << a[1].c << endl;
			return;
		}

		sort(a + 1, a + 7);

		while (a[1].n > 0)
		{
			sort(a + 1, a + 7);

			if (a[1].n == 1 && a[2].n == 0)
				break;

			if (t == "") {
				t += a[1].c;
				a[1].n--;
				sort(a + 1, a + 7);
				continue;
			}
			if (t[t.length() - 1] != a[1].c)
			{
				t += a[1].c;
				a[1].n--;
				sort(a + 1, a + 7);

			}
			else
			{
				if (a[2].n != 0)
				{
					t += a[2].c;
					a[2].n--;
					sort(a + 1, a + 7);
				}
				else
				{
					cout << "IMPOSSIBLE\n";
					return;
				}
			}
		}

		if (a[1].n == 1 && (a[1].c == t[t.length() - 1] || a[1].c == t[0]))
		{
			cout << "IMPOSSIBLE\n";
			return;
		}

		t += a[1].c;
		cout << t << endl;
		return;

}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ll TC;
	cin >> TC;
	for (ll i = 1; i <= TC; ++i) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
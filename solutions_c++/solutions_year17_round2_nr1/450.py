#include <bits/stdc++.h>
using namespace std;

#pragma GCC diagnostic warning "-Wconversion"

#define pb push_back
#define all(a) begin(a), end(a)
#define has(a, b) (a.find(b) != a.end())
#define fora(i, n) for(int i = 0; i < n; i++)
#define forb(i, n) for(int i = 1; i <= n; i++)
#define forc(a, b) for(const auto &a : b)
#define ford(i, n) for(int i = n; i >= 0; i--)
#define maxval(t) numeric_limits<t>::max()
#define minval(t) numeric_limits<t>::min()

#define dbgs(x) #x << " = " << x
#define dbgs2(x, y) dbgs(x) << ", " << dbgs(y)
#define dbgs3(x, y, z) dbgs2(x, y) << ", " << dbgs(z)
#define dbgs4(w, x, y, z) dbgs3(w, x, y) << ", " << dbgs(z)

typedef long long ll;

double s[1007], k[1007];

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;

	forb(t, T)
	{
		int n;
		double d;
		cin >> d >> n;

		fora(i, n)
		{
			cin >> k[i] >> s[i];
		}

		double ti = 0;

		fora(i, n)
		{
			ti = max(ti, (d - k[i]) / s[i]);
		}

		cout << "Case #" << t << ": " << setprecision(10) <<  (d / ti) << endl;
	}
}

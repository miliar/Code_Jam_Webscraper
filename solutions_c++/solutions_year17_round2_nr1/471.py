#include <cstdlib>
#include <iostream>
#include <iomanip>

using namespace std;

const int MAXN = 1005;

int L, N, x, v;
void Solve()
{
	double ans = 0.0;
	cin >> L >> N;
	for (int i = 1; i <= N; ++i)
	{
		cin >> x >> v;
		double t = (L - x) * 1.0 / v;
		if (t > ans)
			ans = t;
	}
	cout << setprecision(6) << L / ans << endl;
}

int T;
int main()
{
	cout << setiosflags(ios::fixed);
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		Solve();
	}
	return 0;
}

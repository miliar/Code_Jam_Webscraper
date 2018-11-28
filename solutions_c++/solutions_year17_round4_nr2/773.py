#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define rep(i, n)  for (int i = 0; i < (int)n; i++)
#define vec vector

int main(void)
{
	int T;
	cin >> T;
	rep(t, T) {
		cout  << "Case #" << t + 1 << ": ";
		int n, c, m;
		cin >> n >> c >> m;
		vec<vec<int>> p(c, vec<int>(n, 0));
		vec<int> x(n, 0), y(c, 0);
		rep(i, m) {
			int l, r;
			cin >> l >> r;
			l--;
			r--;
			p[r][l]++;
			x[l]++;
			y[r]++;
		}
		int a = max(y[0], max(y[1], p[0][0] + p[1][0]));
		int b = 0;
		rep(i, n - 1) b += max(0, p[0][i + 1] + p[1][i + 1] - a);
		cout << a << " " << b <<  endl;

	}
	return 0;
}


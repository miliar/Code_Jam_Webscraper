#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

#define	For(i,a,b)	for(int i=(a);i<(b);++i)
#define	rep(i,n)	For(i,0,(n))

bool check(const vector<pair<int, double>> horses, int D, long double velocity)
{
	rep(i, horses.size()) {
		if(D > horses[i].first + horses[i].second * D / velocity) {
			return false;
		}
	}
	return true;
}

double solve()
{
	int D, N;

	cin >> D >> N;

	vector<pair<int, double>> horses(N);
	rep(i, N)
		cin >> horses[i].first >> horses[i].second;

	long double mn = 0, mx = long double(1e20);
	rep(i, 10000) {
		long double md = (mn + mx) / 2;

		if(check(horses, D, md))
			mn = md;
		else
			mx = md;
	}

	return mn;
}
int main()
{
	int T;
	cin >> T;

	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << fixed << setprecision(10) << solve() << endl;
}

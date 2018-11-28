#include<bits/stdc++.h>
using namespace std;

long double D, due = 2;
long long N;
vector< pair<long double, long double> > horses;

bool check(long double speed)
{
	long double t = D / speed;
	for(auto& horse: horses) {
		long double tt = (D - horse.first) / horse.second;
		if(t < tt)
			return false;
	}

	return true;
}

long double solve()
{
	horses.clear();
	cin >> D >> N;
	for(int i=0; i<N; ++i) {
		long double x, y;
		cin >> x >> y;
		horses.push_back({x, y});
	}

	long double left = 0, right = D*1e4+1, mid, eps = 1e-6;
	while(right-left>eps) {
		mid = (left+right) / due;
		if(check(mid))
			left = mid;
		else
			right = mid;
	}
	
	return mid;
}

int main()
{
	ios_base::sync_with_stdio(false);
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t;
	cin >> t;
	cout.precision(7);
	cout << fixed;
	for(int caso=1; caso<=t; ++caso) {
		cout << "Case #" << caso << ": " << solve() << "\n";
	}

	return 0;
}


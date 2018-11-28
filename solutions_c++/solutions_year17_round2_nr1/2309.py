#include <bits/stdc++.h>
using namespace std;

// #define endl '\n'
#define ff first
#define ss second
#define mp make_pair
#define pb push_back

typedef long long llong;
typedef pair<int, int> pii;

void process() {
	
	int d, n;
	cin >> d >> n;

	double most_time = 0;
	
	for (int i = 0; i < n; i++) {
		double p, s;
		cin >> p >> s;

		double dist = ((double) d - p);
		double time_taken = dist / s;

		most_time = max(most_time, time_taken);

	}

	double ans = d / most_time;

	cout << fixed << setprecision(10);
	cout << ans;

}

void solve() {

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {

		cout << "Case #" << i + 1 << ": ";
		process();
		cout << endl;

	}

}

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	#ifdef LOCAL
		ifstream in("in");
		cin.rdbuf(in.rdbuf());

		ofstream out("out");
		cout.rdbuf(out.rdbuf());
	#endif

	solve();

	return 0;

}
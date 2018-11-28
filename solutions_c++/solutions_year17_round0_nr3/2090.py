#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define ff first
#define ss second
#define mp make_pair
#define pb push_back

typedef long long llong;
typedef pair<int, int> pii;

void process() {

	llong n, k;
	cin >> n >> k;

	llong even_val = (n % 2 == 0) ? n : n - 1;
	llong odd_val = (n % 2) ? n : n - 1;

	llong even_cnt = (n % 2) ? 0 : 1; 
	llong odd_cnt = (n % 2) ? 1 : 0;

	llong total_operations = 0;

	while (even_cnt + odd_cnt < k) {

		// deduct 
		k -= (even_cnt + odd_cnt);

		llong new_even_cnt = even_cnt;
		llong new_odd_cnt = even_cnt;

		llong odd_val_half = odd_val / 2;

		if (odd_val_half % 2) {
			new_odd_cnt += (llong) odd_cnt * 2LL;
		} else {
			new_even_cnt += (llong) odd_cnt * 2LL;
		}

		even_cnt = new_even_cnt;
		odd_cnt = new_odd_cnt;

		llong new_max_val = even_val / 2;

		if (new_max_val % 2) {
			odd_val = new_max_val;
			even_val = new_max_val - 1;
		} else {
			even_val = new_max_val;
			odd_val = even_val - 1;
		}

	}

	llong len = even_cnt + odd_cnt;
	llong idx = k - 1;
	if (idx < 0) idx += len;

	// cerr << even_val << ' ' << odd_val << endl;
	// llong max_ans = max(even_val, odd_val);

	llong odd_max_ans = odd_val / 2, odd_min_ans = odd_val / 2;
	llong even_max_ans = even_val / 2, even_min_ans = even_max_ans - 1;

	// cerr << "idx: " << idx << " len: " << odd_cnt << ' ' << even_cnt << endl;
	// cerr << max_ans << ' ' << min_ans << endl;

	// if even is greater
	if (even_val > odd_val) {

		// cerr << "Even is greater" << endl;

		if (idx < even_cnt) {
			cout << even_max_ans << ' ' << even_min_ans;
		} else {
			cout << odd_max_ans << ' ' << odd_min_ans;
		}

	// odd is greater
	} else {

		// cerr << "Odd is greater" << endl;

		if (idx < odd_cnt) {
			cout << odd_max_ans << ' ' << odd_min_ans;
		} else {
			cout << even_max_ans << ' ' << even_min_ans;
		}
	}

}

void solve() {

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {

		cout << "Case #" << i + 1 << ": ";
		cout.flush();
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
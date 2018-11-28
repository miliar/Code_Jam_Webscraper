#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

using num = long long int;
//constexpr num INF = 100000000000000;

num getsmallestn(num qty, num div) {
	qty *= 100; div *= 110;
	num result = qty/div;
	if (result*div < qty) result++;
	return result;
}

num isbigenough(num qty, num div, num n) {
	// is qty big enough?
	num needed = n*div;
	needed *= 90; qty *= 100;
	return qty >= needed;
}

int main() {
	int cases;
	cin >> cases;
	for (int casei=1; casei<=cases; casei++) {
		int n, p;
		cin >> n >> p;
		num divs[n];
		for (num& x : divs) cin >> x;
		//num arr[n][p];
		vector<num> arr[n];
		for (int i=0; i<n; i++) for (int j=0; j<p; j++) {
			num x;
			cin >> x;
			arr[i].push_back(x);
			//cin >> arr[i][j];
		}
		for (int i=0; i<n; i++) sort(arr[i].begin(), arr[i].end());
		int is[n];
		for (int& idx : is) idx = 0;
		int result = 0;
		while (1) {
			num thebound = 0;
			for (int i=0; i<n; i++) {
				thebound = max(thebound, getsmallestn(arr[i][is[i]], divs[i]));
			}
			bool ok = true, fail = false;
			for (int i=0; i<n; i++) if (!isbigenough(arr[i][is[i]], divs[i], thebound)) {
				ok = false;
				is[i]++;
				if (is[i] >= p) fail = true;
			}
			if (fail) break;
			if (ok) {
				//cout << thebound << endl;
				result++;
				for (int i=0; i<n; i++) {
					is[i]++;
					if (is[i] >= p) fail = true;
				}
			}
			if (fail) break;
		}
		cout << "Case #" << casei << ": " << result << endl;
	}
	return 0;
}

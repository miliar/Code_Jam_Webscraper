#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

using num = long double;

int main() {
	int cases;
	cin >> cases;
	for (int casei=1; casei<=cases; casei++) {
		int n, k;
		cin >> n >> k;
		assert(k == n);
		num u;
		cin >> u;
		num arr[n];
		for (auto& x : arr) cin >> x;
		sort(arr, arr+n);
		cerr << n << " " << u << endl;
		for (auto x : arr) cerr << x << " ";
		cerr << endl;
		num oldu = u;
		num oldarr[n];
		for (int i=0; i<n; i++) oldarr[i] = arr[i];
		for (int i=0; i<n; i++) {
			num current = arr[i];
			num next = 1;
			if (i+1<n) next = arr[i+1];
			num wanted = (next-current)*(i+1);
			//cerr << "w: " << wanted << endl;
			cerr << "current was " << current;
			if (wanted >= u) {
				current += u/((num)(i+1));
				u = 0;
			} else {
				u -= wanted;
				current = next;
			}
			cerr << " current is " << current << endl;
			for (int j=0; j<=i; j++) arr[j] = current;
			if (u < 0.000000000001L) break;
		}
		{
			num dsum = 0;
			for (int i=0; i<n; i++) dsum += arr[i] - oldarr[i];
			cerr << dsum << " = " << oldu << endl;
			assert(dsum - oldu < 0.000000001L);
			assert(oldu - dsum < 0.000000001L);
		}
		assert(u < 0.000000001L);
		cerr << "u: " << u << endl;
		num result = 1;
		for (int i=0; i<n; i++) result *= arr[i];
		//cout.precision(9);
		//cout << "Case #" << casei << ": " << result << endl;
		printf("Case #%d: %.10Lf\n", casei, result);
	}
}

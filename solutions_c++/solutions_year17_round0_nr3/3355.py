#include <iostream>
#include <queue>
using namespace std;

int main () {
	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti ++) {
		int n, k;
		cin >> n >> k;
		priority_queue<int> q;
		q.push(n);

		for (int i = 0; i < k-1; i ++) {
			int f = q.top();
			q.pop();
			int h = (f-1) / 2;
			q.push(h);
			q.push(f-1-h);
		}
		int f = q.top();
		if (f % 2 == 1) {
			cout << "Case #" << ti << ": " << f / 2 << " " << f / 2 << endl;
		} else {
			cout << "Case #" << ti << ": " << f / 2 << " " << f / 2 - 1<< endl;
		}
		// if (ans != -1) {
			// cout << "Case #" << ti << ": " << ans << endl;
		// } else {
		// 	cout << "Case #" << ti << ": IMPOSSIBLE" << endl; 
		// }
	}
}
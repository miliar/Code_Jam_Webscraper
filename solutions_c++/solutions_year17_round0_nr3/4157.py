#include <iostream>
using namespace std;

int main() {
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T;
	long long n, k, p1, p2, t, q1, q2;
	cin >> T;
	for (int kase = 1; kase <= T; ++kase) {
		cin >> n >> k;
		p1 = 1, p2 = 0, t = n;
		cout << "Case #" << kase << ": ";
		while (k) {
			//cout << endl;
			//cout << p1 << ' ' << p2 << ' ' << t << ' ';
			if (k <= p2) {
				cout << (t + 1) / 2 << ' ' << t / 2 << endl;
				break;
			}
			k -= p2;
			if (k <= p1) {
				cout << t / 2 << ' ' << (t - 1) / 2 << endl;
				break;
			}
			k -= p1;
			if (t == 2) {
				q1 = 0;
				t = 0;
				q2 = p1 + p2 * 2;
			} else if (t == 1) {
				q1 = 0;
				q2 = q2;
				t = 0;
			} else if (t & 1) {
				q1 = p1 * 2 + p2;
				q2 = p2;
				t /= 2;
			} else {
				q1 = p1;
				q2 = p2 * 2 + p1;
				t = t / 2 - 1;
			}
			p1 = q1;
			p2 = q2;
			//cout << k << endl;
		}
	}
	return 0;
}

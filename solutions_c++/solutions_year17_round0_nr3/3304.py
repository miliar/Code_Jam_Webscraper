#include <iostream>
#include <string>
#include <map>

using namespace std;

long long n, k;

int main() {
	long long T;
	long long q;
	map<long long, long long>::iterator it;
	cin >> T;
	for (long long K = 1; K <= T; K++) {
		map<long long, long long> p;
		cin >> n >> k;
		cout << "Case #" << K << ": ";
		if (n == k) {
			cout << "0 0" << endl;
			continue;
		}
		p[n] = 1;
		long long c = 0, a, b;
		while (c < k) {
			it = p.end();
			it--;
			c += it->second;
			q = it->first;
			p[a = q / 2] += it->second;
			p[b = (q - 1) / 2] += it->second;
			p.erase(it);
		}
		cout << a << " " << b << endl;
	}

	return 0;
}

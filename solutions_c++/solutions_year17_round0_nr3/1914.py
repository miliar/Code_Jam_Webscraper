#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		long long n, k;
		cin >> n >> k;
		
		map<long long, long long> e;
		e[n] = 1;
		
		while (k > 1) {
			auto last = --e.end();
			long long next = last->first;
			long long cnt = last->second;
			long long used = min(k - 1, cnt);
			if (used == cnt) {
				e.erase(--e.end());
			} else {
				last->second -= used;
			}

			long long n1 = (next - 1) / 2;
			long long n2 = next - 1 - n1;
			e[n1] += used;
			e[n2] += used;
			k -= used;
		}

		auto last = --e.end();
		long long next = last->first;
		long long n1 = (next - 1) / 2;
		long long n2 = next - 1 - n1;
		cout << "Case #" << test << ": " << n2 << " " << n1 << endl;
	}
}

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <string.h>
#include <stack>
#include <list>

#define IMAX 1234567890

using namespace std;

int main(int argc, const char * argv[]) {
	int t_c = 0;
	cin >> t_c;

	for (int z = 1; z <= t_c; z++) {

		long long n, k;
		cin >> n >> k;

		long long nnum = n;
		pair<long long, long long> p, r;
		p.first = 1;
		p.second = 0;

		long long count = 0;

		while (1) {
			if (count + p.second >= k) {
				if ((nnum + 1) % 2 == 1) {
					r.first = nnum / 2;
					r.second = nnum / 2;
				}
				else {
					r.first = nnum / 2;
					r.second = (nnum + 1) / 2;
				}
				break;
			}
			else if (count + p.first + p.second >= k) {
				if (nnum % 2 == 1) {
					r.first = (nnum - 1) / 2;
					r.second = (nnum - 1) / 2;
				}
				else {
					r.first = (nnum - 1) / 2;
					r.second = nnum / 2;
				}
				break;
			}
			count += p.first;
			count += p.second;

			long long nf = 0, ns = 0;
			if (nnum % 2 == 1) {
				nf += p.second;
				ns += p.second;
				nf += (p.first * 2);
				nnum = (nnum - 1) / 2;
			}
			else {
				ns += (p.second * 2);
				nf += p.first;
				ns += p.first;
				nnum = (nnum - 1) / 2;
			}
			p.first = nf;
			p.second = ns;
		}


		cout << "Case #" << z << ": ";
		cout << max(r.first, r.second) << " " << min(r.first, r.second) << endl;

	}
	return 0;
}
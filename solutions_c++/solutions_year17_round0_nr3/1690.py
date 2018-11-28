#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	long long t, n, k;
	cin >> t;
	
	long long a, b, p, na, nb;
	long long tmp1, tmp2, tmp3;
	for (int q = 0; q < t; q++) {
		cin >> n >> k;
		a = n;
		b = n;
		p = 1;
		na = 0;
		nb = 1;
		
		while (k > p) {
			k -= p;
			p *= 2;
			
			tmp3 = 2 * (na + nb);
			tmp1 = 0;
			tmp2 = nb;
			if ((b - 1) / 2 == b / 2) {
				tmp2 += nb;
			}
			if ((a - 1) / 2 == b / 2) {
				tmp2 += na;
			}
			if (a / 2 == b / 2) {
				tmp2 += na;
			}
			tmp1 = tmp3 - tmp2;
			
			na = tmp1;
			nb = tmp2;
			
			b = b / 2;
			a = b - 1;
		}
		
		cout << "Case #" << q + 1 << ": ";
		(k > nb) ? cout << a / 2 << " " << (a - 1) / 2 : cout << b / 2 << " " << (b - 1) / 2;
		cout << endl;
	}
}
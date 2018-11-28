#include <bits/stdc++.h>
using namespace std;

int main() {
	int t , kase = 0;
	scanf("%d" , &t);
	for( ; t--; ) {
		unsigned long long n , m;
		cin >> n >> m;

		n++;
		unsigned long long p = 0 , l = n , r = n;
		for( ; m; ) {
			n = p ? r : l;
			p = m % 2;

			if(n & 1) l = n / 2 + 1 , r = n / 2;
			else l = r = n / 2;

			m /= 2;
		}

		cout << "Case #" << ++kase << ": " << l - 1 << " " << r - 1 << endl;
	}
	return 0;
}
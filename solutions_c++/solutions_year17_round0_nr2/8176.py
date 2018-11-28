#include <iostream>

using namespace std;

#define forsn(i,s,n) for(int i = (s);i < (int)(n);i++)
#define forn(i,n) forsn(i,0,n)
#define dforsn(i,s,n) for(int i = (n - 1);i >= (int)(s);i--)
#define dforn(i,n) dforsn(i,0,n)

bool is_tidy(int n) {
	int last = 9;
	while (n) {
		if (n % 10 > last) return false;
		last = n % 10;
		n /= 10;
	}
	return true;
}

int main() {
	int T; cin >> T;
	
	forn(caso, T) {
		cout << "Case #" << caso + 1 << ": ";
	
		int n; cin >> n;
		dforsn(i, 1, n + 1) {
			if (is_tidy(i)) {
				cout << i << endl;
				break;
			}
		}
	}
}

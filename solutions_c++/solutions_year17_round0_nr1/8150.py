#include <iostream>

using namespace std;

#define forsn(i,s,n) for(int i = (s);i < (int)(n);i++)
#define forn(i,n) forsn(i,0,n)

int main() {
	int T; cin >> T;
	forn(caso, T) {
		cout << "Case #" << caso + 1 << ": ";
		
		string s;
		int k;
		cin >> s >> k;
		
		int vueltas = 0;
		forn(i, s.size()) {
			if (s[i] == '-') {
				if (i + k > (int)s.size()) {
					vueltas = -1;
					break;
				} else {
					vueltas++;
					forsn(j, i, i + k) {
						s[j] = (s[j] == '+' ? '-' : '+');
					}
				}
			}
		}
		
		if (vueltas == -1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << vueltas;
		}
		
		cout << endl;
	}
}

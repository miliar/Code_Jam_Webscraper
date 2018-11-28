#include <bits/stdtr1c++.h>

using namespace std;

typedef long double ld;
typedef long long ll;
typedef pair<ll, ll> pii;
typedef complex<ld> pt;

char a[30][30];
int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
        cout << "Case #" << ca << ":" << endl;;
		
		int r, c; cin >> r >> c;
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cin >> a[i][j];
			}
		}
		
		for (int i = 0; i < r; i++) {
			char last = 0;
			for (int j = 0; j < c; j++) {
				if (a[i][j] != '?') {
					last = a[i][j];
					continue;
				}
				if (last != 0) {
					a[i][j] = last;
				}
			}
			
			last = 0;
			for (int j = c-1; j >= 0; j--) {
				if (a[i][j] != '?') {
					last = a[i][j];
					continue;
				}
				if (last != 0) {
					a[i][j] = last;
				}
			}
		}
		
		for (int j = 0; j < c; j++) {
			char last = 0;
			for (int i = 0; i < r; i++) {
				if (a[i][j] != '?') {
					last = a[i][j];
					continue;
				}
				if (last != 0) {
					a[i][j] = last;
				}
			}
			
			last = 0;
			for (int i = r-1; i >= 0; i--) {
				if (a[i][j] != '?') {
					last = a[i][j];
					continue;
				}
				if (last != 0) {
					a[i][j] = last;
				}
			}
		}
		
		for (int i = 0; i < r; i++) {
			for (int j = 0; j < c; j++) {
				cout << a[i][j];
			}
			cout << endl;
		}
    }
	return 0;
}
#define F(n) Fi(i,n)
#define Fi(i,n) Fl(i,0,n)
#define Fl(i,l,n) for(int i=(l);i<(n);++i)
#include <bits/stdc++.h>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/priority_queue.hpp>
using namespace std;
// using namespace __gnu_pbds;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t;
	string n, ans;
	cin >> t;
	Fl(cs, 1, t+1) {
		cout << "Case #" << cs << ": ";
		cin >> n;
		for (int i = 0 ; i < (int)(n.length()) - 1 ; ++i)
			if (n[i] > n[i+1]) {
				int j;
				for (j = i ; j >= 0 && n[j] > n[j+1] ; --j)
					n[j] = n[j] - 1;
				for (j = j + 2 ; j < (int)(n.length()) ; ++j)
					n[j] = '9';
				break;
			}
		bool nz = 0;
		for (auto c: n) if (nz || c != '0') {
			nz = 1;
			cout << c;
		}
		cout << '\n';
	}
}
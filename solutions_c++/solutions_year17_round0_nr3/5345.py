#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>

using namespace std;

typedef long long int lint;

int next() {int x; cin >> x; return x;}
lint lnext() {lint x; cin >> x; return x;}

int main() {

	int tests = next();
	for (int test = 1; test <= tests; test++) {
		lint n = lnext();
		lint k = lnext();

		//cout << n << " !!! "<< k << endl;

		set<lint> s;
		s.insert(n);

		map<lint, lint> m;

		m[n] = 1;

		while (true) {
			lint x = *s.rbegin();
			//cout << x << " " << m[x] << endl;
			if (m[x] < k) {
				k -= m[x];
				
				lint y1 = (x - 1)/2;
				lint y2 = x - 1 - y1;

				s.insert(y1);
				s.insert(y2);
				
				m[y1] += m[x];
				m[y2] += m[x];

				s.erase(x);
				m[x] = 0;
			} else {
				lint y1 = (x - 1)/2;
				lint y2 = x - 1 - y1;
				cout << "Case #" << test << ": " << y2 << " " << y1 << "\n";
				break;
			}
		}

		

		//printf("Case #%d:", test);
	}
}
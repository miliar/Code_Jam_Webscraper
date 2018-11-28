#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <iomanip>

using namespace std;

struct Act {
	int f, t;
	bool c;

	bool operator<(const Act& rhs) const {
		return f < rhs.f;
	}
};

int dist(int a, int b) {
	if (a <= b) return b - a;
	return 24 * 60 - (a - b); 
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int ac, aj;
		cin >> ac >> aj;
		//cout << "ACAJ " << ac << " " << aj << endl;

		vector<Act> a(ac + aj);
		for (int i = 0; i < ac; i++) {
			cin >> a[i].f >> a[i].t;
			//cout << "AC " << a[i].f << " " << a[i].t << endl;
			a[i].c = true;
		}

		for (int i = ac; i < ac + aj; i++) {
			cin >> a[i].f >> a[i].t;
			//cout << "AJ " << a[i].f << " " << a[i].t << endl;
			a[i].c = false;
		}

		sort(a.begin(), a.end());

		vector<int> ec, ej;
		int s = 0, tc = 24 * 60, tj = 24 * 60;
		for (int i = 0; i < ac + aj; i++) {
			int j = (i + 1) % (ac + aj);

			if (a[i].c) tj -= a[i].t - a[i].f;
			else tc -= a[i].t - a[i].f;

			if (a[i].c == a[j].c) {
				if (a[i].c) {
					ec.push_back(dist(a[i].t, a[j].f));
					tj -= dist(a[i].t, a[j].f);
				} else {
					ej.push_back(dist(a[i].t, a[j].f));
					tc -= dist(a[i].t, a[j].f);
				}
			} else {
				s++;
			}
		}

		sort(ec.begin(), ec.end());
		sort(ej.begin(), ej.end());

		//cout << tj << " " << tc << endl;

		if (tj >= 12 * 60 && tc >= 12 * 60) {
			cout << "Case #" << t << ": " << s << endl;
		} else if (tj < 12 * 60) {
			int i = ec.size() - 1;
			while (tj < 12 * 60) {
				//cout << "LOOP " << i << " " << tj << endl;
				s += 2;
				tj += ec[i];
				i--;
			}
			cout << "Case #" << t << ": " << s << endl;
		} else {
			int i = ej.size() - 1;
			while (tc < 12 * 60) {
				//cout << "LOOP " << i << " " << tc << endl;
				s += 2;
				tc += ej[i];
				i--;
			}
			cout << "Case #" << t << ": " << s << endl;
		}

	}



	return 0;
}
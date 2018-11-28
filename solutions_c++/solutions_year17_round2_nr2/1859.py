#include <iostream>
#include <assert.h>
#include <algorithm>
#include <vector>

using namespace std;

void fail() {
	cout << "IMPOSSIBLE\n";
	exit(0);
}

void solve(int test) {
	vector <char> c(6);
	c[0] = 'R';
	c[1] = 'Y';
	c[2] = 'B';
	c[3] = 'G';
	c[4] = 'V';
	c[5] = 'O';
	
	cout << "Case #" << test << ": ";

	int n;
	cin >> n;
	vector <int> a(6);
	cin >> a[0] >> a[5] >> a[1] >> a[3] >> a[2] >> a[4];
	for (int i = 0; i < 3; i++) {
		
		if (a[i + 3] > a[i]) {
			cout << "IMPOSSIBLE\n";
			return;
		}

		if (a[i] && a[i + 3] == a[i]) {
				
			if (a[i] + a[i + 3] != n) {
				cout << "IMPOSSIBLE\n";
				return;
			}
			
			for (int it = 0; it < a[i]; it++) {
				cout << c[i] << c[i + 3];
			}

			return;

		}

		a[i] -= a[i + 3];
	}
	
	vector < pair<int, int> > pres(3);
	for (int i = 0; i < 3; i++) {
		pres[i] = make_pair(a[i], i);
	}
	sort(pres.begin(), pres.end());
	
	if (pres[0].first + pres[1].first < pres[2].first) {
		cout << "IMPOSSIBLE\n";
		return;
	}

	vector <int> ans;
	vector <char> used(3);

	for (int i = 0; i < pres[2].first; i++) {
		ans.push_back(pres[2].second);
		int type = pres[2].second;
		
		if (!used[type]) {
			used[type] = 1;
			for (int it = 0; it < a[type + 3]; it++) {
				ans.push_back(type + 3);
				ans.push_back(type);
			}
		}

		int rest = pres[2].first - i - 1;
		if (pres[0].first) {

			ans.push_back(pres[0].second);
			pres[0].first--;

			int type = pres[0].second;
			if (!used[type]) {
				used[type] = 1;
				for (int it = 0; it < a[type + 3]; it++) {
					ans.push_back(type + 3);
					ans.push_back(type);
				}
			}

			if (pres[1].first && pres[0].first + pres[1].first - 1 >= rest) {
				ans.push_back(pres[1].second);
				pres[1].first--;
				type = pres[1].second;
				
				if (!used[type]) {
					used[type] = 1;
					for (int it = 0; it < a[type + 3]; it++) {
						ans.push_back(type + 3);
						ans.push_back(type);
					}
				}

			}
		} else {
			ans.push_back(pres[1].second);
				
			pres[1].first--;
		}
	
	}

	assert(pres[1].first + pres[0].first == 0);

	for (int E : ans) {
		cout << c[E];
	}
	cout << "\n";
}
		
	
	

int main() {
#ifdef KOBRA
//	freopen("input", "r", stdin);
#endif
	int ts = 1;
	cin >> ts;
	for (int i = 1; i <= ts; i++) {
		solve(i);
	}
	return 0;
}

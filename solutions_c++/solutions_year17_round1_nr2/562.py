#include <queue>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <stack>
using namespace std;
#define V vector
#define tD typedef
tD long long ll;
tD V<int> vi;
tD V<vi> vii;
tD V<ll> vll;
tD V<string> vs;
tD long double ld;
tD pair<int, int> pii;
#define prr make_pair
#define fr(x,y) for(int x=0;x<(y); ++x)
#define fi(n) fr(i,n)
#define fj(n) fr(j,n)
#define fk(n) fr(k,n)
#define pb push_back
#define sz size()
#define DEBUG 0

bool works(ll required, pair<int, int> range) {
	if (required >= range.first && required <= range.second) return true;
	return false;
}

bool toolow(ll required, pair<int, int> range) {
	return required < range.first;
}

bool toohigh(ll required, pair<int, int> range) {
	return required > range.second;
}

int main() {
	int T; cin >> T;
	for (int qw = 1; qw <= T; qw++) {
		int n, p; cin >> n >> p;
		vector<int> req(n);
		fi(n) cin >> req[i];
		vector<vector<pair<int, int> > > range(n, vector<pair<int, int> >(p));;
		fi(n) fj(p) {
			int grams; cin >> grams;
			int lo = grams * 9 / 10;
			while (lo * 10 / 9 < grams) ++lo;
			int hi = grams * 10 / 9;
			range[i][j] = prr(lo, hi);
		}
		fi(n) {
			sort(range[i].begin(), range[i].end());
			fj(p) {
				if (DEBUG) cout << range[i][j].first << "," << range[i][j].second << " ";
			}
			if (DEBUG) cout << endl;
		}
		int kits = 0;
		int servings = 1;
		vector<int> col(n, 0);
		bool alldone = false;
		while(!alldone) {
			bool failed = false;
			fi(n) {
				while(toolow(servings * req[i], range[i][col[i]])) {
					if (DEBUG) cout << "failed " << servings << " " << i << " " << col[i] << " " << req[i] << " " << range[i][col[i]].first << " " << range[i][col[i]].second << endl;
					++servings;
					failed = true;
				}
				if (failed) {
					--servings;
					break;
				}
				while(toohigh(servings * req[i], range[i][col[i]])) {
					if (DEBUG) cout << "failed " << servings << " " << i << " " << col[i] << " " << req[i] << " " << range[i][col[i]].first << " " << range[i][col[i]].second << endl;
					if (++col[i] == p) {
						failed = true;
						alldone = true;
						break;
					}
				}
				if (alldone || failed) break;
				if (!works(servings * req[i], range[i][col[i]])) {
					if (DEBUG) cout << "failed " << servings << " " << i << " " << col[i] << " " << req[i] << " " << range[i][col[i]].first << " " << range[i][col[i]].second << endl;
					failed = true;
					break;
				} else {
					if (DEBUG) cout << servings << " " << i << " " << col[i] << " " << req[i] << " " << range[i][col[i]].first << " " << range[i][col[i]].second << endl;
				}
			}
			if (alldone) break;
			if (!failed) {
				if (DEBUG) cout << "Feeding " << servings << " servings." << endl;
				kits++;
				fi(n) {
					++col[i];
					if (col[i] == p) alldone = true;
				}
			} else {
				++servings;
			}
		}
		cout << "Case #" << qw << ": " << kits << endl;
	}
}

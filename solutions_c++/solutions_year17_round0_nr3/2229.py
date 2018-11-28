#include <iostream>
#include <set>
#include <map>
using namespace std;

long long n, k;
set<long long> S;
map<long long, long long> cnt;

void update(long long x, long long y) {
	auto p = S.find(-x);
	if (p != S.end()) {
		S.erase(p);
	}
	cnt[x] += y;
	S.insert(-x);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC;
	cin >> TC;
	for (int tt = 1; tt <= TC; tt++) {
		cin >> n >> k;
		cnt.clear();
		update(n, 1);

		while (S.size()) {
			long long x = -(*S.begin()), y = cnt[x]; S.erase(S.begin());
			//cout << x << endl;
			if (y >= k) {
				cout << "Case #" << tt << ": ";
				cout << (x - 1) - (x - 1) / 2 << " " << (x - 1) / 2 << endl;
				break;
			}
			else {
				if (x & 1) {
					update(x / 2, y * 2);
				} else {
					long long t = (x - 1) / 2;
					update(t, y);
					update(t + 1, y);
				}
			}
			k -= y;
		}
	}
}
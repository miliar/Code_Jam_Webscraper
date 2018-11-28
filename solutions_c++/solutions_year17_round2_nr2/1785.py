#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Mane
{
	Mane(char c, int count) : color(c), count(count) {}

	char color;
	int count;	
};


int main() {
	int t;
	cin >> t;
	for (int ca = 1; ca <= t; ++ca) {
		int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;

		vector<Mane> manes;

		if (R > 0) manes.push_back({'R', R});
		if (O > 0) manes.push_back({'O', O});
		if (Y > 0) manes.push_back({'Y', Y});
		if (G > 0) manes.push_back({'G', G});
		if (B > 0) manes.push_back({'B', B});
		if (V > 0) manes.push_back({'V', V});

		bool ok = true;
		string res;
		char last = '-';
		while (ok and not manes.empty()) {
			sort(manes.begin(), manes.end(), [](const Mane& lhs, const Mane& rhs) {
				return lhs.count > rhs.count;
			});

			ok = false;
			for (auto it = manes.begin(); it != manes.end(); ++it) {
				if (it->color != last) {
					res.append(1, it->color);
					it->count--;
					last = it->color;
					ok = true;
					if (it->count == 0) {
						manes.erase(it);
					}
					break;
				}
			}

			//cerr << "res=" << res << endl;

			if (not ok) {
				res.clear();
				break;
			}
		}

		if (res[0] == res[N-1]) {
			if (res[0] == res[N-2]) {
				res.clear();
			} else if (res[N-1] != res[N-3]) {
				swap(res[N-1], res[N-2]);
			} else {
				res.clear();
			}
		} 

		cout << "Case #" << ca << ": " << (res.empty() ? "IMPOSSIBLE" : res) << endl;
	}

	return 0;
}

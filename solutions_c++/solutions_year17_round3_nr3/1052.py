#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
#include <map>

using namespace std;

int main() {
#ifdef _DEBUG
	std::ifstream in("C:\\Users\\silvio.lazzeretti\\Downloads\\C.in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
#endif
	int T;
	cin >> T;
	int t = 0;
	while (++t <= T) {
		int n, k;
		cin >> n >> k;
		double u;
		cin >> u;
		double miss = 0;
		map<double, int> c;
		for (int i = 0; i < n; ++i) {
			double p;
			cin >> p;
			c[p]++;
			miss += 1 - p;
		}

		double res = 0;
		if (u >= miss) {
			res = 1;
		}
		else {
			while (c.size() > 1) {
				if (u < 0.0000001)
					break;

				auto it = c.begin();
				auto it1 = c.begin();
				++it1;

				double toadd = (it1->first - it->first)*it->second;
				if (toadd > u)
					break;

				u -= toadd;
				it1->second += it->second;
				c.erase(it);
			}

			auto ii = c.begin();
			res = pow(ii->first + u / ii->second, ii->second);
			++ii;
			while (ii != c.end()) {
				res *= pow(ii->first, ii->second);
				ii++;
			}
		}


		cout << "Case #" << t << ": ";
		cout << fixed << setprecision(6) << res;
		cout << endl;
	}
	return 0;
}
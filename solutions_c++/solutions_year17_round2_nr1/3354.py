#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
#include <iomanip>

using namespace std;

int main() {
	int tsts;
	cin >> tsts;
	
	for (int tst = 1; tst <= tsts; ++tst) {
		int d, n;
		cin >> d >> n;
		vector <pair<int, int> > v;
		for (int i = 0; i < n; ++i) {
			pair<int, int> p;
			cin >> p.first >> p.second;
			v.push_back(p);
		}
		sort(v.begin(), v.end(), greater<pair<int, int> >());
		double mint = 0;
		for (auto it = v.begin(); it != v.end(); ++it) {
			double prop = double(d - it->first) / double(it->second);
			if (prop > mint) mint = prop;
		}

		double ans = d / mint;
		cout << setprecision(int(ans)/100 + 8);
		cout << "case #" << tst << ": " << d/mint << "\n";
	}
	//system("PAUSE");
	return 0;
}
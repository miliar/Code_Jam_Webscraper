#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <utility>
#include <algorithm>

#define PI 3.1415926535

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int z = 0; z < T; ++z) {
		int AC, AJ;
		cin >> AC >> AJ;
		vector<int> tcs, tct, tjs, tjt;
		for(int i = 0; i < AC; ++i) {
			int temp;
			cin >> temp;
			tcs.push_back(temp);
			cin >> temp;
			tct.push_back(temp);
		}
		for(int i = 0; i < AJ; ++i) {
			int temp;
			cin >> temp;
			tjs.push_back(temp);
			cin >> temp;
			tjt.push_back(temp);
		}

		sort(tcs.begin(), tcs.end());
		sort(tct.begin(), tct.end());
		sort(tjs.begin(), tjs.end());
		sort(tjt.begin(), tjt.end());

		if(AC+AJ == 1 || AC == AJ) {
			cout << "Case #" << z+1 << ": 2\n";
			continue;
		}

		if(AC == 2) {
			if(tct[1] - tcs[0] <= 720 || 1440 + tct[0] - tcs[1] <= 720) {
				cout << "Case #" << z+1 << ": 2\n";
			}
			else {
				cout << "Case #" << z+1 << ": 4\n";
			}
			continue;
		}

		if(AJ == 2) {
			if(tjt[1] - tjs[0] <= 720 || 1440 + tjt[0] - tjs[1] <= 720) {
				cout << "Case #" << z+1 << ": 2\n";
			}
			else {
				cout << "Case #" << z+1 << ": 4\n";
			}
			continue;
		}
	}
}
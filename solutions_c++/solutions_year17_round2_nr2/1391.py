#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<math.h>
#include<algorithm>
#include<iomanip>

using namespace std;

int main() {
	ifstream ifs("in.txt");
	ofstream ofs("out.txt");
	int n;
	ifs >> n;
	for (int loop = 1; loop <= n; loop++) {
		string ans;
		char maC;
		vector<char> cs;
		int nn ,a, b, c, ab, bc, ca, sum = 0;
		ifs >>nn>> a >> ab >> b >> bc >> c >> ca;
		int ma = a;
		maC = 'R';
		if (ma < b) {
			ma = b;
			maC = 'Y';
		}
		if (ma < c) {
			ma = c;
			maC = 'B';
		}
		sum = a + b + c;
		if (maC != 'R') {
			for (int i = 0; i < a; i++) {
				cs.push_back('R');
			}
		}
		if (maC != 'Y') {
			for (int i = 0; i < b; i++) {
				cs.push_back('Y');
			}
		}
		if (maC != 'B') {
			for (int i = 0; i < c; i++) {
				cs.push_back('B');
			}
		}
		if (ma <= sum - ma) {
			for (int i = 0; i < ma; i++) {
				ans.push_back(maC);
				ans.push_back(cs[i]);
				if (int(cs.size()) - ma  - i > 0) {
					ans.push_back(cs[cs.size() - 1 - i]);
				}
			}
			ofs << "Case #" << loop << ": " << ans << endl;
		}
		else {
			ofs << "Case #" << loop << ": "  << "IMPOSSIBLE" << endl;
		}
		//cout << cs.size() - ma << endl;
	}
	//cin >> n;
	return 0;
}
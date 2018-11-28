#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

char colors[] = "ROYGBV";

bool go(char res[], vector<pair<int, char> > numColor,
		int idx, int n) {
	if (idx == n) {
		if (res[n-1] != res[0]) return true;
	}
	else {
		sort(numColor.begin(), numColor.end());
		for (int i = 5; i >= 0; --i) {
			if (numColor[i].first > 0 && numColor[i].second != res[idx - 1]) {
				res[idx] = numColor[i].second;
				--numColor[i].first;
				if (go(res, numColor, idx + 1, n)) return true;
				++numColor[i].first;
			}
		}
	}

	return false;
}

void findRes(char res[]) {
	int n, num;
	vector<pair<int, char> > numColor;
	numColor.reserve(6);
	cin >> n;
	for (int i = 0; i < 6; ++i) {
		cin >> num;
		numColor.emplace_back(num, colors[i]);
	}

	for (int i = 0; i < 6; ++i) {
		if (numColor[i].first * 2 > n) {
			strcpy(res, "IMPOSSIBLE");
			return;
		}
	}

	sort(numColor.begin(), numColor.end());
	res[0] = numColor[5].second;
	--numColor[5].first;
	if (!go(res, numColor, 1, n)) {
		memset(res, 0, sizeof(res));
		strcpy(res, "IMPOSSIBLE");
	};
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("outpu22t.txt","w", stdout);
    
	int T; cin >> T;
	for (int c = 1; c <= T; ++c) {
		char res[1002] = { 0 };
		findRes(res);
		cout << "Case #" << c << ": " << res << endl;
	}
}
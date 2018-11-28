#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);

		int AC, AJ;
		cin >> AC >> AJ;
		vector<pair<int, int>> CD(AC), JK(AJ);
		for (int i = 0; i < AC; i++) cin >> CD[i].first >> CD[i].second;
		for (int i = 0; i < AJ; i++) cin >> JK[i].first >> JK[i].second;
		if (AC > AJ) {
			swap(AC, AJ);
			CD.swap(JK);
		}

		if (AJ < 2) {
			cout << 2 << endl;
			continue;
		}
		sort(JK.begin(), JK.end());
		if (JK[1].second - JK[0].first > 720 && 
			JK[0].second + 1440 - JK[1].first > 720) {
			cout << 4 << endl;
		}
		else {
			cout << 2 << endl;
		}

	}
	return 0;
}

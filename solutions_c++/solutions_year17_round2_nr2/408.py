#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const string s = "ROYGBV";

string solve(vector <int> arr, int f) {
	string res = "";
	set <int> forb;
	forb.insert(f);
	forb.insert((f - 1 + 6) % 6);
	forb.insert((f + 1) % 6);
	for (int i = 0; i < arr[0]; ++i) {
		vector <int> sum(6);
		for (int j = 1; j < 7; ++j) {
			int prev = j == 1 ? 6 : j - 1;
			int next = j == 6 ? 1 : j + 1;
			sum[j - 1] = arr[prev] + arr[j] + arr[next];
		}
		int ma = -1;
		for (int j = 0; j < 6; ++j)
			if (!forb.count(j) && arr[j + 1] > 0 && (ma == -1 || sum[j] > sum[ma]))
				ma = j;
		if (ma == -1)
			break;
		--arr[ma + 1];
		forb.clear();
		forb.insert(ma);
		forb.insert((ma - 1 + 6) % 6);
		forb.insert((ma + 1) % 6);
		if (i == arr[0] - 2) {
			forb.insert(f);
			forb.insert((f - 1 + 6) % 6);
			forb.insert((f + 1) % 6);
		}
		res.push_back(s[ma]);
	}
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; ++t) {
		vector <int> arr(7);
		for (int i = 0; i < 7; ++i)
			cin >> arr[i];
		cout << "Case #" << t << ": ";
		arr[0]--;
		bool ok = false;
		for (int i = 1; i < 7; ++i)
			if (arr[i] > 0) {
				--arr[i];
				auto res = solve(arr, i - 1);
				if (res.length() == arr[0]) {
					cout << s[i - 1] << res;
					ok = true;
					break;
				}
				++arr[i];
			}
		if (!ok)
			cout << "IMPOSSIBLE";
		cout << endl;
	}
}
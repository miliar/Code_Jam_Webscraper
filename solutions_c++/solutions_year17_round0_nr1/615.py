#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
	int t; cin >> t;
	for (int i = 0; i < t; i++) {
		string s; cin >> s;
		int k; cin >> k;
		vector<int>pancake(s.size());
		for (int i = 0; i < s.size(); i++) {
			if (s[i] == '+')pancake[i] = 1;
			else pancake[i] = 0;
		}

		int cnt = 0;
		bool flag = true;
		for (int i = 0; i < s.size(); i++) {
			if (pancake[i] == 0) {
				if (i + k > s.size()) {
					flag = false;
					break;
				}
				for (int j = i; j < i + k; j++) {
					pancake[j] = !pancake[j];
				}
				cnt++;
			}
		}

		cout << "CASE #" << i + 1 << ": ";
		if (flag)cout << cnt << endl;
		else cout << "IMPOSSIBLE" << endl;
	}



    return 0;
}


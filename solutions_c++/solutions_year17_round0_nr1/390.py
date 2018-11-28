#include <iostream>
#include <vector>


typedef long long ll;
using namespace std;



int main(int argc, char const *argv[]) {
	ll T;
	cin >> T;
	for (ll testcase = 0 ; testcase < T; testcase++) {
		string s;
		ll K;
		cin >> s >> K;
		ll res = 0;

		for (int i = 0; i < s.size(); i++) {
			if (i + K > s.size()) {
				break;
			}

			bool ft = false;
			string filp_map = "";

			if (s[i] == '-') {
				ft = true;
			}

			if (ft) {
				res++;
				for (int j = 0; j < s.size(); j++) {
					if (j == i) {
						for (int x = 0; x < K ; x++) {
							if (s[j] == '-') {
								filp_map += '+';
							} else {
								filp_map += '-';
							}
							j++;
						}
					}
					if (j < s.size()) {
						if (s[j] == '-') {
							filp_map += '-';
						} else {
							filp_map += '+';
						}
					}
				}
				s = filp_map;
			}
		}
		if (s.find('-') != string::npos) {
			cout << "Case #" << testcase + 1 << ": " << "IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << testcase + 1 << ": " << res << endl;
		}
	}
	return 0;
}
#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <map>
#include <set>
#include <set>

#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

typedef long long int64;

using namespace std;

void solve() {
	int n;
	cin >> n;
	int R, O, Y, G, B, V;
	cin >> R >> O >> Y >> G >> B >> V;
	if (O > 0) {
		if (O == B && O + B == n) {
			string answer;
			for (int i = 0; i < n / 2; ++i) {
			    answer += "OB";
			}
			cout << answer << endl;
			return;
		}
		if (O >= B) {
		    cout << "IMPOSSIBLE" << endl;
		    return;
		}
	}
	if (G > 0) {
		if (G == R && G + R == n) {
			string answer;
			for (int i = 0; i < n / 2; ++i) {
			    answer += "GR";
			}
			cout << answer << endl;
			return;
		}
		if (G >= R) {
		    cout << "IMPOSSIBLE" << endl;
		    return;
		}
	}
	if (V > 0) {
		if (V == Y && V + Y == n) {
			string answer;
			for (int i = 0; i < n / 2; ++i) {
			    answer += "VY";
			}
			cout << answer << endl;
			return;
		}
		if (V >= Y) {
		    cout << "IMPOSSIBLE" << endl;
		    return;
		}
	}
	B -= O;
	R -= G;
	Y -= V;
	vector<pair<int, char>> nums;
	map<char, pair<int, int>> add;
	add['B'] = mp(O, 'O');
	add['R'] = mp(G, 'G');
	add['Y'] = mp(V, 'V');
	nums.pb(mp(R, 'R'));
	nums.pb(mp(Y, 'Y'));
	nums.pb(mp(B, 'B'));
	sort(all(nums));
	reverse(all(nums));
	if (nums[0].first > nums[1].first + nums[2].first) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
    string answer;
	for (int i = 0; i < nums[1].first + nums[2].first - nums[0].first; ++i) {
		answer.pb(nums[0].second);
		answer.pb(nums[1].second);
		answer.pb(nums[2].second);
	}
	for (int i = 0; i < nums[0].first - nums[2].first; ++i) {
		answer.pb(nums[0].second);
		answer.pb(nums[1].second);
	}
	for (int i = 0; i < nums[0].first - nums[1].first; ++i) {
		answer.pb(nums[0].second);
		answer.pb(nums[2].second);
	}
	    for (int j = 0; j < 3; ++j) {
			for (int i =0; i < sz(answer); ++i) {
				if (answer[i] == nums[j].second) {
					string add_answer;
					for (int l = 0; l < add[nums[j].second].first; ++l) {
						add_answer.pb(add[nums[j].second].second);
						add_answer.pb(nums[j].second);
					}
					answer = answer.substr(0, i + 1) + add_answer + answer.substr(i + 1);
					break;
				}
			}
		}
	cout << answer << endl;
}

int main() {
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}

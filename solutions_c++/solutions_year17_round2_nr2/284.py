#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define scanf nope
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

void solve() {
	int N;
	int R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	vector<string> RS(R, "R"), YS(Y, "Y"), BS(B, "B");
	auto eat = [](int& var, string ch, vector<string>& from) {
		while (var && sz(from) >= 2) {
			--var;
			string B1 = from.back();
			from.pop_back();
			string B2 = from.back();
			from.pop_back();
			from.push_back(B1 + ch + B2);
		}
	};
	eat(O, "O", BS);
	eat(G, "G", RS);
	eat(V, "V", YS);

	int left = O + G + V + sz(RS) + sz(YS) + sz(BS);
	if (O + G + V > 1) {
		cout << "IMPOSSIBLE" << endl;
	} else if (O + G + V == 1) {
		if (left > 2) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			auto docheck = [](int& var, char ch, vector<string>& from){
				if (var) {
					if (!sz(from)) {
						cout << "IMPOSSIBLE" << endl;
						return true;
					}
					assert(sz(from) == 1);
					cout << ch << from[0] << endl;
					return true;
				}
				return false;
			};
			if (docheck(O, 'O', BS)) return;
			if (docheck(G, 'G', RS)) return;
			if (docheck(V, 'V', YS)) return;
		}
	} else {
		int themax = left / 2;
		if ((left != 1) && (sz(RS) > themax || sz(YS) > themax || sz(BS) > themax)) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			vector<vector<string>> cols = {RS, YS, BS};
			sort(all(cols), [](const vector<string>& a, const vector<string>& b) { return sz(a) > sz(b); });
			vector<int> ans(left, -1);
			vector<string> sans(left);
			int its = sz(cols[0]);
			rep(i,0,its) {
				ans[2*i] = 0;
				sans[2*i] = cols[0].back(); cols[0].pop_back();
			}
			int last = 1;
			for (int i = left - 1; i >= 0; --i) {
				if (cols[last].empty()) last = 3 - last;
				if (ans[i] == -1) {
					ans[i] = last;
					sans[i] = cols[last].back(); cols[last].pop_back();
					last = 3 - last;
				}
			}
			rep(i,0,left) {
				int nx = (i + 1) % left;
				if (left != 1) assert(ans[i] != ans[nx]);
			}
			trav(it, sans) cout << it;
			cout << endl;
		}
	}
}

int main() {
	cin.sync_with_stdio(0);
	cin.exceptions(cin.failbit);

	int TC;
	cin >> TC;
	rep(i,0,TC) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}
}

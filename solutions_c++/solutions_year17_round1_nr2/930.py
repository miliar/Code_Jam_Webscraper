#include <bits/stdc++.h>
using namespace std;

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }
vector<string> split(const string& s, char c) { vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.push_back(move(x)); return v; }
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) { cerr << it->substr((*it)[0] == ' ', it->length()) << " = " << a << '\n'; err(++it, args...); }

#define MAXN 52
int T;
int N, P;
int R[MAXN];
vector<pair<pair<int, int>, int> > intervals;
priority_queue<int> tails[MAXN];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	freopen("B.txt", "r", stdin);
	freopen("B.out", "w", stdout);
	
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cout << "Case #" << tc << ": ";

		cin >> N >> P;

		int ans = 0;

		for (int i = 0; i < N; i++) {
			cin >> R[i];
		}
		intervals.clear();
		for (int i = 0; i < N; i++) {
			while (tails[i].size()) {
				tails[i].pop();
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < P; j++) {
				int q; cin >> q;
				int biggest = q * 10 / 9 / R[i];
				int smallest = ((q * 10 + 10) / 11 + R[i] - 1) / R[i];
				if (smallest <= biggest) {
					intervals.push_back({{smallest, biggest}, i});
				}
			}
		}

		sort(intervals.begin(), intervals.end());
		for (auto p : intervals) {
			tails[p.second].push(p.first.second);
			for (int i = 0; i < N; i++) {
				while (!tails[i].empty() && tails[i].top() < p.first.first) {
					tails[i].pop();
				}
			}
			while (true) {
				bool b = false;
				for (int i = 0; i < N; i++) {
					if (tails[i].empty()) {
						b = true;
						break;
					}
				}
				if (b) break;
				for (int i = 0; i < N; i++) {
					tails[i].pop();
				}
				ans++;
			}
		}

		cout << ans << '\n';
	}

	cout.flush();
	return 0;
}

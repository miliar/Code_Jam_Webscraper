#include <bits/stdc++.h>
using namespace std;

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }
vector<string> split(const string& s, char c) { vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.push_back(move(x)); return v; }
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) { cerr << it->substr((*it)[0] == ' ', it->length()) << " = " << a << '\n'; err(++it, args...); }

int T;
string S;
int N, K;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	freopen("A.txt", "r", stdin);
	freopen("A.out", "w", stdout);

	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cout << "Case #" << tc << ": ";

		cin >> S >> K;
		int N = S.size();
		int ans = 0;
		for (int i = 0; i + K - 1 < N; i++) {
			if (S[i] == '-') {
				ans++;
				for (int j = i; j < i + K; j++) {
					S[j] = (S[j] == '-' ? '+' : '-');
				}
			}
		}

		int happy = true;
		for (int i = 0; i < N; i++) {
			if (S[i] == '-') {
				happy = false;
				break;
			}
		}
		if (happy) {
			cout << ans;
		}
		else {
			cout << "IMPOSSIBLE";
		}

		cout << '\n';
	}

	cout.flush();
	return 0;
}

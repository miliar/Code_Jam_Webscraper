#include <bits/stdc++.h>
using namespace std;

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }
vector<string> split(const string& s, char c) { vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.push_back(move(x)); return v; }
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) { cerr << it->substr((*it)[0] == ' ', it->length()) << " = " << a << '\n'; err(++it, args...); }

#define MAXR 26
int T;
int R, C;
string G[MAXR];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	freopen("A.txt", "r", stdin);
	freopen("A.out", "w", stdout);
	
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cout << "Case #" << tc << ": ";

		cin >> R >> C;
		for (int i = 0; i < R; i++) {
			cin >> G[i];
		}

		int rfletter = -1;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (G[i][j] != '?') {
					rfletter = i;
					break;
				}
			}
			if (~rfletter) {
				break;
			}
		}

		for (int i = rfletter; i < R; i++) {
			int jfletter = -1;
			for (int j = 0; j < C; j++) {
				if (G[i][j] != '?') {
					jfletter = j;
					break;
				}
			}
			if (jfletter == -1) {
				for (int j = 0; j < C; j++) {
					G[i][j] = G[i-1][j];
				}
			}
			else {
				char c = G[i][jfletter];
				for (int j = 0; j < C; j++) {
					if (G[i][j] == '?') {
						G[i][j] = c;
					}
					else {
						c = G[i][j];
					}
				}
			}
		}

		for (int i = rfletter - 1; i >= 0; i--) {
			for (int j = 0; j < C; j++) {
				G[i][j] = G[i+1][j];
			}
		}

		for (int i = 0; i < R; i++) {
			cout << '\n';
			for (int j = 0; j < C; j++) {
				cout << G[i][j];
			}
		}

		cout << '\n';
	}

	cout.flush();
	return 0;
}

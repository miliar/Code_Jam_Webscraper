#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <fstream>

#define int long long
#define MOD7 1000000007
#define MOD9 1000000009

#define rep(i, n) for (int i = 0; i < (n); i++)
#define REP(i, a, n) for (int i = (a); i <= (n); i++)
#define all(a) (a).begin(), (a).end()

using namespace std;

int dx[4] = { 1, 0, -1, 0 };
int dy[4] = { 0, -1, 0, 1 };

int nextInt() {int a; cin >> a; return a;}
char nextChar() {char a; cin >> a; return a;}
double nextDouble() {double a; cin >> a; return a;}
string nextString() {string a; cin >> a; return a;}

template<class T> void inputVector(vector<T>& v, int n) {
    v.resize(n);
    for (int i = 0; i < v.size(); i++) cin >> v[i];
}

bool nondec(string S) {
	char prev = '0';
	rep(i, S.size()) {
		if (S[i] < prev) return false;
		prev = S[i];
	}
	return true;
}

signed main() {
	int T;
	cin >> T;

	ofstream out("output-B-large.txt");
	REP(loop, 1, T) {
		string S, cS;
		cin >> S;

		cS = S;

		while (!nondec(S)) {
			bool flag = false;
			string T = "";
			T += S[0];
			REP(i, 1, S.size() - 1) {
				if (flag) {
					T += '9';
					continue;
				}
				if (S[i] < S[i - 1]) {
					flag = true;
					T += '9';
					T[i - 1]--;
					continue;
				}
				T += S[i];
			}
			while (T[0] == '0') {
				T = T.substr(1);
			}
			S = T;
		}
		out << "Case #" << loop << ": " << S << endl;
		cout << cS << " -> " << S << endl;
	}

    return 0;
}

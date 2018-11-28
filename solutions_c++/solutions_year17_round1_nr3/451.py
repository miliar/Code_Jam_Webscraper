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

signed main() {
	int T;
	cin >> T;

	ofstream out("output-C-small.txt");
	REP(loop, 1, T) {
		int Hd, Ad, Hk, Ak, B, D;
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

		int attackTurn = 0;
		{
			int prev = INT_MAX;
			int num = 0;
			while (1) {
				int turn = (Hk + Ad + B * num - 1) / (Ad + B * num) + num;
				if (turn > prev) break;
				attackTurn = turn;
				prev = turn;
				num++;
			}
		}

		int ans = -1;
		if (Ad >= Hk) {
			ans = 1;
		} else if (Ak - D >= Hd) {
			ans = -1;
		} else {
			ans = INT_MAX;
			rep(num, 100) {
				int Hdc = Hd;
				int Akc = Ak;
				int attackLeft = attackTurn;
				int debuffLeft = num;
				REP(turn, 1, 1000) {
					if (debuffLeft > 0) {
						if (Hdc > Akc - D) {
							Akc -= D;
							Hdc -= Akc;
							debuffLeft--;
						} else {
							Hdc = Hd - Akc;
						}
					} else {
						if (attackLeft == 1) {
							ans = min(ans, turn);
							break;
						} else if (Hdc > Akc) {
							Hdc -= Akc;
							attackLeft--;
						} else {
							Hdc = Hd - Akc;
						}
					}
				}
			}
			if (ans == INT_MAX) ans = -1;
		}

		out << "Case #" << loop << ": " << (ans == -1 ? "IMPOSSIBLE" : to_string(ans)) << endl;
		cout << "Case #" << loop << ": " << (ans == -1 ? "IMPOSSIBLE" : to_string(ans)) << endl;
	}

    return 0;
}

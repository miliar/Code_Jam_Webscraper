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

	string imp = "IMPOSSIBLE";

	REP(loop, 1, T) {
		int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;

		int M = N;
		int Rc = R, Oc = O, Yc = Y, Gc = G, Bc = B, Vc = V;

		string ret;
		if (R < G || Y < V || B < O) ret = imp;
		else {
			if (R > 0 && R == G) {
				if (N != R + G) ret = imp;
				else {
					ret = "";
					rep(i, N / 2) {
						ret += "RG";
					}
					G = 0;
				}
			} else if (Y > 0 && Y == V) {
				if (N != Y + V) ret = imp;
				else {
					ret = "";
					rep(i, N / 2) {
						ret += "YV";
					}
					V = 0;
				}
			} else if (B > 0 && B == O) {
				if (N != B + O) ret = imp;
				else {
					ret = "";
					rep(i, N / 2) {
						ret += "BO";
					}
					O = 0;
				}
			} else {
				R -= G;
				Y -= V;
				B -= O;
				N = R + Y + B;
				if (2 * R > N || 2 * Y > N || 2 * B > N) ret = imp;
				else {
					ret = string(N, '.');
					int pt = 0;
					rep(j, 3) {
						if (R + Y + B == 0) break;
						if (R >= Y && R >= B) {
							rep(i, R) {
								ret[pt] = 'R';
								pt += 2;
								if (pt >= N) pt = 1;
							}
							R = 0;
						} else if (Y >= R && Y >= B) {
							rep(i, Y) {
								ret[pt] = 'Y';
								pt += 2;
								if (pt >= N) pt = 1;
							}
							Y = 0;
						} else if (B >= R && B >= Y) {
							rep(i, B) {
								ret[pt] = 'B';
								pt += 2;
								if (pt >= N) pt = 1;
							}
							B = 0;
						}
					}
				}
			}
		}

		if (ret != imp) {
			rep(i, M) {
				if (ret[i] == 'R' && G > 0) {
					ret.insert(ret.begin() + i + 1, 'R');
					ret.insert(ret.begin() + i + 1, 'G');
					G--;
				} else if (ret[i] == 'Y' && V > 0) {
					ret.insert(ret.begin() + i + 1, 'Y');
					ret.insert(ret.begin() + i + 1, 'V');
					V--;
				} else if (ret[i] == 'B' && O > 0) {
					ret.insert(ret.begin() + i + 1, 'B');
					ret.insert(ret.begin() + i + 1, 'O');
					O--;
				}
			}
		}

		cout << "Case #" << loop << ": " << ret << endl;

		if (ret != imp) {
			if (M != ret.size()) {
				cout << " ERROR : ret.size is invalid!" << endl;
			}
			rep(i, ret.size()) {
				if (ret[i] == 'R') Rc--;
				else if (ret[i] == 'O') Oc--;
				else if (ret[i] == 'Y') Yc--;
				else if (ret[i] == 'G') Gc--;
				else if (ret[i] == 'B') Bc--;
				else if (ret[i] == 'V') Vc--;
			}
			if (Rc != 0) cerr << " ERROR : number of R is invalid! : Rc=" << Rc << endl;
			if (Oc != 0) cerr << " ERROR : number of O is invalid! : Oc=" << Oc << endl;
			if (Yc != 0) cerr << " ERROR : number of Y is invalid! : Yc=" << Yc << endl;
			if (Gc != 0) cerr << " ERROR : number of G is invalid! : Gc=" << Gc << endl;
			if (Bc != 0) cerr << " ERROR : number of B is invalid! : Bc=" << Bc << endl;
			if (Vc != 0) cerr << " ERROR : number of V is invalid! : Bc=" << Vc << endl;
			rep(i, ret.size() - 1) {
				if (ret[i] == 'R' &&
					(ret[i + 1] == 'R' || ret[i + 1] == 'O' || ret[i + 1] == 'V')) {
					cerr << " ERROR : same color error! index:" << i << endl;
				} else if (ret[i] == 'Y' &&
					(ret[i + 1] == 'Y' || ret[i + 1] == 'G' || ret[i + 1] == 'O')) {
					cerr << " ERROR : same color error! index:" << i << endl;
				} else if (ret[i] == 'B' &&
					(ret[i + 1] == 'B' || ret[i + 1] == 'G' || ret[i + 1] == 'V')) {
					cerr << " ERROR : same color error! index:" << i << endl;
				} else if (ret[i] == 'O' && ret[i + 1] != 'B') {
					cerr << " ERROR : same color error! index:" << i << endl;
				} else if (ret[i] == 'G' && ret[i + 1] != 'R') {
					cerr << " ERROR : same color error! index:" << i << endl;
				} else if (ret[i] == 'V' && ret[i + 1] != 'Y') {
					cerr << " ERROR : same color error! index:" << i << endl;
				}
			}
			{
				if (ret[0] == 'R' &&
					(ret[M - 1] == 'R' || ret[M - 1] == 'O' || ret[M - 1] == 'V')) {
					cerr << " ERROR : same color error! index:" << M - 1 << endl;
				} else if (ret[0] == 'Y' &&
					(ret[M - 1] == 'Y' || ret[M - 1] == 'G' || ret[M - 1] == 'O')) {
					cerr << " ERROR : same color error! index:" << M - 1 << endl;
				} else if (ret[0] == 'B' &&
					(ret[M - 1] == 'B' || ret[M - 1] == 'G' || ret[M - 1] == 'V')) {
					cerr << " ERROR : same color error! index:" << M - 1 << endl;
				} else if (ret[0] == 'O' && ret[M - 1] != 'B') {
					cerr << " ERROR : same color error! index:" << M - 1 << endl;
				} else if (ret[0] == 'G' && ret[M - 1] != 'R') {
					cerr << " ERROR : same color error! index:" << M - 1 << endl;
				} else if (ret[0] == 'V' && ret[M - 1] != 'Y') {
					cerr << " ERROR : same color error! index:" << M - 1 << endl;
				}
			}
		}
	}

    return 0;
}

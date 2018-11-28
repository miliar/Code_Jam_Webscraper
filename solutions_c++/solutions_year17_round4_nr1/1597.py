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

	REP(loop, 1, T) {
		int N, P;
		cin >> N >> P;

		vector<int> G;
		inputVector(G, N);

		int cnt[4];
		memset(cnt, 0, sizeof(cnt));
		rep(i, N) {
			cnt[G[i] % P]++;
		}

		int ret = cnt[0];
		if (P == 2) {
			ret += (cnt[1] + 1) / 2;
		} else if (P == 3) {
			int num = min(cnt[1], cnt[2]);
			ret += num;
			cnt[1] -= num;
			cnt[2] -= num;

			ret += (cnt[1] + 2) / 3;
			ret += (cnt[2] + 2) / 3;
		}

		cout << "Case #" << loop << ": " << ret << endl;
	}

    return 0;
}

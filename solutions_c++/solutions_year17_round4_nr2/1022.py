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

int positionCount[1010];

class Buyer {
public:
	vector<int> position;
	int posCount[1010];

	Buyer() {
		memset(posCount, 0, sizeof(posCount));
	}

	bool operator< (const Buyer &a) const {
		return position.size() > a.position.size();
	}
};

signed main() {
	int T;
	cin >> T;

	REP(loop, 1, T) {
		memset(positionCount, 0, sizeof(positionCount));

		int N, C, M;
		cin >> N >> C >> M;

		vector<Buyer> buyers(C);
		rep(i, M) {
			int P, B;
			cin >> P >> B;
			B--;
			buyers[B].position.push_back(P);
			positionCount[P]++;
			buyers[B].posCount[P]++;
		}

		int ride = max(buyers[0].position.size(), buyers[1].position.size());
		int prom = 0;
		int left = M;
		REP(i, 1, 1000) {
			int tmp = 0;
			rep(j, 2) {
				int p1 = j;
				int p2 = 1 - j;
				int hojo = max(0LL, (int)buyers[p1].position.size() - (int)buyers[p2].position.size());
				tmp = max(tmp, max(0LL, buyers[p1].posCount[i] - ((int) buyers[p2].position.size() + hojo - buyers[p2].posCount[i])));
			}
			if (i == 1) {
				ride += tmp;
			} else {
				prom += tmp;
			}
		}

		cout << "Case #" << loop << ": " << ride << " " << prom << endl;
	}

    return 0;
}

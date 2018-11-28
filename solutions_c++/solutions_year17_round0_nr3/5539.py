#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <iomanip>
#include <utility>
#include <stack>
#include <memory.h>
#include <ctime>
#include <cstdlib>
#include <sstream>
#include <unordered_set>
#include <unordered_map>
#include <cstring>
#include <inttypes.h>

#define FILE "C-small-1-attempt2"
#define fi first
#define se second
#define pb push_back
#define matrix(type) vector<vector<type>>
#define sqr(x) ((x)*(x))
using namespace std;

typedef long long LL;
typedef long double LD;

const int INF = 2e9;
const LD PI = 3.14159265358979323846;
const LD EPS = 1e-10;
const int MOD = 1e9 + 7;

const int N = 1e3 + 10;
const int M = 1e5 + 10;

vector<int> u;

struct p {
	int pos, dl, dr;
};

bool isbetter(p a, p b) {
	if (min(a.dl, a.dr) > min(b.dl, b.dr)) return true;
	if (min(a.dl, a.dr) < min(b.dl, b.dr)) return false;
	if (max(a.dl, a.dr) > max(b.dl, b.dr)) return true;
	if (max(a.dl, a.dr) < max(b.dl, b.dr)) return false;
	return a.pos < b.pos;
}

pair<int, int> solvehard(int n, int k) {
	p res = { -1,-1,-1 };
	u.push_back(-1);
	u.push_back(n);
	for (int i = 0; i < k; ++i){
		for (int j = 0; j < u.size() - 1; ++j){
			int l = u[j], r = u[j + 1];
			int curpos = (l + r) / 2;
			int froml = curpos - l - 1, fromr = r - curpos - 1;
			p cur = { curpos, froml, fromr };
			if (res.pos == -1 || isbetter(cur, res)) {
				res = cur;
			}
		}
		u.push_back(res.pos);
		sort(u.begin(), u.end());
		if (i != k - 1) res = { -1,-1,-1 };
	}
	u.clear();
	return{ max(res.dl, res.dr), min(res.dl, res.dr) };
}

int main() {
	//ios_base::sync_with_stdio(false);
	freopen(FILE".in", "r", stdin); freopen(FILE".out", "w", stdout);
	int t, n, k;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", i);
		auto p = solvehard(n, k);
		printf("%d %d\n", p.first, p.second);
	}
	return 0;
}
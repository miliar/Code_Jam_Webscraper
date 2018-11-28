#include <queue>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>
#include <stack>
#include <cstdio>
using namespace std;
#define V vector
#define tD typedef
tD long long ll;
tD V<int> vi;
tD V<vi> vii;
tD V<ll> vll;
tD V<string> vs;
tD V<double> vd;
tD long double ld;
tD pair<int, int> pii;
#define prr make_pair
#define fr(x,y) for(int x=0;x<(y); ++x)
#define fi(n) fr(i,n)
#define fj(n) fr(j,n)
#define fk(n) fr(k,n)
#define pb push_back
#define sz size()
#define DEBUG 0

int P;
map<pair<vector<int>, int>, int> cache;

int best(const vector<int>& left, int leftover) {
	if (cache.count(prr(left, leftover))) {
		return cache[prr(left, leftover)];
	}
	if (left == vector<int>(P + 1, 0)) return 0;
	int most = 0;
	fi (left.sz) {
		if (left[i] != 0) {
			vector<int> nextleft = left;
			nextleft[i]--;
			int nextleftover = (leftover - i + P) % P;
			most = max(most, best(nextleft, nextleftover) + (leftover==0?1:0));
		}
	}
	return cache[prr(left, leftover)] = most;
}

int main() {
    int T; cin >> T;
    for (int qw = 1 ; qw <= T; qw++) {
		cache.clear();
		int N; cin >> N >> P;
		vector<int> left(P + 1, 0);
		fi(N) {
			int a; cin >> a; left[a % P]++;
		}
		
		int zero = left[0]; left[0] = 0;
		//int zero = 0;
		int most = best(left, 0) + zero;
        printf("Case #%d: ", qw);
        printf("%d\n", most);
    }
}

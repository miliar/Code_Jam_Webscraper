#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

void clear(int i) {

}

int solution(int nTest) {
	priority_queue<pii> q;
	int n, k;
	scanf("%d%d", &n, &k);
	q.push(mp(n, -0));
	int MAX, MIN;
	For (i, 0, k) {
		pii f = q.top();
		q.pop();
		int l = -f.second;
		int r = l + f.first - 1;
		int m = (r + l) / 2;
		int sl = m - l;
		int sr = r - m;
//cerr << l << " " << m << " " << r << "(" << sl << "," << sr << ")" << endl;

		q.push(mp(sl, -(l)));
		q.push(mp(sr, -(m + 1)));
		MAX = max(sl, sr);
		MIN = min(sl, sr);
	}
	printf("%d %d\n", MAX, MIN);

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	

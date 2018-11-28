#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 0

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

struct S {
	int s;
	int e;
	int c;
	S(int s, int e, int c) : s(s), e(e), c(c) {}
};

bool operator<(const S &a, const S &b) {
	return a.s < b.s;
}


int solve(vector<S> v) {
	int must = 0;
	int mustTime = 0;

	int cTime = 0;
	int jTime = 0;

	vector<int> can;
	For (i, 1, sz(v)) {
		int diff = v[i].s - v[i-1].e;
		if (v[i].c == v[i-1].c) {
			can.pb(diff);
			if (v[i].c) {
				cTime += diff;
			} else {
				jTime += diff;
			}
		} else {
			must++;
			mustTime += diff;
		}
	}
	For (i, 0, sz(v)) {
		if (v[i].c) {
			cTime += v[i].e - v[i].s;
		} else {
			jTime += v[i].e - v[i].s;
		}
	}
	cerr << cTime << " " << jTime << " " << must << ":" << mustTime << endl;
	For (i, 0, sz(can)) cerr << can[i] << ", " ; cerr << endl;

	int diff = abs(cTime - jTime);
	double t = diff - mustTime;
	t /= 2;
	cerr << "diff" << diff << "  t" << t << endl;
	sort(all(can));
	int res = must;
	while (t > 0) {
		cerr << "newT" << t << endl;;
		if (sz(can) == 0) {
			cerr << "FUUUU" << endl;
			return -1;
		}
		t -= can.back();
		can.pop_back();
		res += 2;
	}
	return res;
}

int solution(int nTest) {
	cerr << "Test " << nTest << endl;
	int ac, aj;
	scanf("%d%d", &ac, &aj);
	vector<S> v;
	For (i, 0, ac) {
		int s, e;
		scanf("%d%d", &s, &e);
		v.pb(S(s, e, 1));
	}
	For (i, 0, aj) {
		int s, e;
		scanf("%d%d", &s, &e);
		v.pb(S(s, e, 0));
	}

	sort(all(v));


	vector<S> v1 = v;
	v1.insert(v1.begin(), S(0, 0, 0));
	v1.pb(S(1440, 1440, 0));
	int res1 = solve(v1);

	vector<S> v2 = v;
	v2.insert(v2.begin(), S(0, 0, 1));
	v2.pb(S(1440, 1440, 1));
	int res2 = solve(v2);

	int res = min(res1, res2);
	printf("%d\n", res);


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
	

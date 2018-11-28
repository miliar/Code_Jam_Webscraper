#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i >= (b); --i)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define fi first
#define se second

const int N = 1010;

int tc[N], tv[N], ti[N];
int n,m,k;

bool ok(int w) {
	FOR(i,k) if (tv[i] < i/w) return false;
	return true;
}

void test() {
	scanf("%d%d%d", &n, &m, &k);
	FOR(i,N) ti[i]=0;
	FOR(i,N) tc[i]=0;
	FOR(i,k) {
		int pp, bb;
		scanf("%d%d", &pp, &bb);
		pp--; bb--;
		ti[bb]++;
		tv[i] = pp;
		tc[pp]++;
	}
	sort(tv,tv+k);
	int lo = 0, hi = k;
	FOR(i,m) lo = max(lo, ti[i]-1);
	while (lo+1 < hi) {
		int mi = (lo+hi) / 2;
		if (ok(mi)) hi = mi;
		else lo = mi;
	}
	int tot = 0;
	for (int i=n-1; i>=0; i--) {
		if (tc[i] > hi) {
			int v = tc[i] - hi;
			tot += v;
		}
	}
	printf("%d %d\n", hi, tot);
}

int main() {
	int ttn;
	scanf("%d", &ttn);
	FORI(i,ttn) {
		printf("Case #%d: ", i);
		test();
	}
	return 0;
}

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

char s[1010];

void test() {
	int n,k,res=0;
	scanf("%s%d", s, &k);
	for (n=0; s[n]; n++) ;
	FOR(i,n-k+1) if (s[i]=='-') {
		res++;
		FOR(j,k) s[i+j] = '-' + '+' - s[i+j];
	}
	FOR(i,n) if (s[i]=='-') {
		printf("IMPOSSIBLE\n");
		return;
	}
	printf("%d\n", res);
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

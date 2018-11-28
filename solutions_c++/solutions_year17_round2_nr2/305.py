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

string lett = "ROYGBV";
int t[7];
int num[333];
char s[12345];

void test() {
	int n;
	scanf("%d", &n);
	FOR(i,6) scanf("%d", &t[i]);
	FOR(i,3) t[2*i] -= t[(2*i+3)%6];
	if (t[0] > t[2] + t[4] || t[2] > t[0] + t[4] || t[4] > t[0] + t[2]) {
		printf("IMPOSSIBLE\n");
		return;
	}
	if (t[0]==0 && t[2]==0 && t[4]==0) {
		int nn=0;
		if (t[1]) nn++;
		if (t[3]) nn++;
		if (t[5]) nn++;
		if (nn>1) {
			printf("IMPOSSIBLE\n");
			return;
		}
		FOR(i,3) if (t[(2*i+3)%6]) {
			FOR(j,n/2) {
				s[2*j] = lett[2*i];
				s[2*j+1] = lett[(2*i+3)%6];
			}
			s[n]=0;
			printf("%s\n", s);
			return;
		}
	}
	int ma = 0;
	if (t[2] > t[0]) ma = 2;
	if (t[4] > t[ma]) ma = 4;
	int pos=0, prv=-1;
	for (; pos<n; ) {
		while (prv != -1 && t[(prv+3)%6]>0) {
			s[pos++] = lett[(prv+3)%6];
			s[pos++] = lett[prv];
			t[(prv+3)%6]--;
		}
		int nxt=-2;
		if (prv != ma) nxt = ma;
		FOR(i,3) if (2*i!=prv) {
			if (nxt==-2 || t[nxt]<t[2*i]) nxt=2*i;
		}
		t[nxt]--;
		s[pos++] = lett[nxt];
		prv = nxt;
	}
	s[n] = 0;
	printf("%s\n", s);
}

int main() {
	FOR(i,6) num[lett[i]]=i;
	int ttn;
	scanf("%d", &ttn);
	FORI(i,ttn) {
		printf("Case #%d: ", i);
		test();
	}
	return 0;
}

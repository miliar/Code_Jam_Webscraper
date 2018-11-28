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

char s[123];

void test() {
	int n;
	scanf("%s", s);
	for (n=0; s[n]; n++) ;
	int pos = -1;
	FOR(i,n-1) if (s[i]>s[i+1]) {
		pos = i;
		break;
	}
	if (pos==-1) {
		printf("%s\n", s);
		return;
	}
	char dig = s[pos];
	while (pos>=0 && s[pos] == dig) pos--;
	s[pos+1]--;
	for (int i=pos+2; i<n; i++) s[i]='9';
	if (s[0]=='0') printf("%s\n", s+1);
	else printf("%s\n", s);
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

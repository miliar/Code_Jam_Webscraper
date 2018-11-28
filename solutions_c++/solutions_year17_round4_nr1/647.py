#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

int n, p;
int k[10];
int pd[5][110][110][110];

void read() {
	scanf("%d %d", &n, &p);

	memset(k,0,sizeof(k));
	for (int i = 0; i < n; i++) {
		int c; scanf("%d", &c);
		k[c%p]++;
	}
}

int rec(int cur, int o, int tw, int th) {
	if (o+tw+th == 0) return 0;

	int& ans = pd[cur][o][tw][th];
	if (ans == -1) {
		ans = 0;
		if (o) ans = max(ans, rec((cur+1)%p, o-1, tw, th));
		if (tw) ans = max(ans, rec((cur+2)%p, o, tw-1, th));
		if (th) ans = max(ans, rec((cur+3)%p, o, tw, th-1));
		
		ans += (cur == 0);
	}
	return ans;
}

void solve() {
	memset(pd,-1,sizeof(pd));
	int ans = k[0];
	ans += rec(0, k[1], k[2], k[3]);
	printf("%d\n", ans);
}


























int myMod = 0;
int howMany = 1;

int main(int argc, char** argv) {
	if (argc > 1) {
		stringstream ss; ss << argv[1]; ss >> myMod;
		ss.str(""); ss.clear();
		ss << argv[2]; ss >> howMany;
	}

	int cases;
	scanf("%d", &cases);
	for (int i = 0; i < cases; i++) {
		read();
		if (i % howMany == myMod) {
			printf("Case #%d: ", i+1);
			solve();
		}
	}
}
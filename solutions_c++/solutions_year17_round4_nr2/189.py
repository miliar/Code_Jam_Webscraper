#include <bits/stdc++.h>
using namespace std;

#define LL 					long long
#define ULL 				unsigned long long
#define pii 				pair<int,int>
#define fi 					first
#define se 					second
#define mp 					make_pair
#define vi 					vector<int>
#define psb 				push_back
#define ppb 				pop_back
#define all(x)			 	(x).begin(),(x).end()
#define sz 					size()
#define endln 				printf("\n")
#define gc					getchar_unlocked
#define setmin(x)			memset((x), -1, sizeof((x)))
#define setnul(x)			memset((x), 0, sizeof((x)))
#ifndef getchar_unlocked
#define getchar_unlocked 	getchar
#endif
const int inf = (1<<30)-1+(1<<30);
const int mod = 1e9 + 7;

void gi( int &ret ) {
	ret = 0; char inp=gc(); int kl=1;
	while (inp<'0' || inp>'9') {if (inp=='-') kl=-1; inp=gc();}
	while ('0'<=inp && inp<='9') ret=(ret<<3)+(ret<<1)+(int)(inp-'0'), inp=gc();
	if (kl<1) ret=-ret;
}

const int MAXN = 1e3 + 5;
int n, p, m, val[MAXN], jml[MAXN], sum[MAXN];

int main() {
	int tc; gi(tc);
	for (int cs=1; cs<=tc; cs++) {
		gi(n); gi(p); gi(m);
		setnul(val); setnul(jml);
		int a, b, ans = 0;
		while (m--) {
			gi(a); gi(b);
			val[a]++; jml[b]++;
			ans = max(ans, jml[b]);
		}
		for (int i=1; i<=n; i++) {
			sum[i] = sum[i-1] + val[i];
			int tp = sum[i] / i;
			if (sum[i]%i) tp++;
			ans = max(ans, tp);
		}
		int move = 0;
		for (int i=1; i<=n; i++) 
			if (val[i]>ans) move += val[i] - ans;
		printf ("Case #%d: %d %d\n", cs, ans, move);
	}
	return 0;
}



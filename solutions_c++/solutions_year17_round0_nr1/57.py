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

const int maxn = 1005;
int val[maxn], n,k, ans = 0;
char inp[maxn];

int lm () {
	for (int i=0; i<n; i++) 
		if (!val[i]) return i;
	return -1;
}
int rm() {
	for (int i=n-1; i>=0; i--)
		if (!val[i]) return i;
	return -1;
}
bool solve() {
	int ll = lm();
	while ((ll+k) <= n && ll>=0) {
		for (int i=0; i<k; i++) 
			val[ll+i] ^= 1;
		ans++;
		ll = lm();
	}
	int rr = rm();
	while ((rr-k+1)>=0) {
		for (int i=0; i<k; i++)
			val[rr-i] ^= 1;
		ans++;
		rr = rm();
	}
	if (rm()==-1) return 1;
	else return 0;
}

int main() {
	int tc; gi(tc);
	for (int cs=1; cs<=tc; cs++) {
		scanf("%s %d", inp, &k);
		setnul(val);
		ans = 0;
		n = strlen(inp);
		for (int i=0; i<n; i++) 
			if (inp[i]=='+') val[i] = 1;
		if (solve()) {
			printf ("Case #%d: %d\n", cs, ans);
		} else printf ("Case #%d: IMPOSSIBLE\n", cs);
	}
	return 0;
}



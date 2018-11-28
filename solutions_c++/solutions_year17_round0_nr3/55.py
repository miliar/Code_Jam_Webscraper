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

LL n, k, jml[100][2], val[100][2];

LL solve() {
	setnul(jml); setnul(val);
	jml[0][n&1LL] = 1LL; val[0][n&1LL] = n;
	jml[0][(n&1LL)^1LL] = 0LL; val[0][(n&1LL)^1LL] = 0LL;
	int l = 0;
	LL nex;
	while (val[l][0] || val[l][1]) {
		if (val[l][0] && val[l][1]) {
			if (val[l][0] > val[l][1]) {
				if (jml[l][0] >= k) return val[l][0];
				else k -= jml[l][0];
				if (jml[l][1] >= k) return val[l][1];
				else k -= jml[l][1];
			} else {
				if (jml[l][1] >= k) return val[l][1];
				else k -= jml[l][1];
				if (jml[l][0] >= k) return val[l][0];
				else k -= jml[l][0];
			}	
		} else if (val[l][0]) {
			if (jml[l][0] >= k) return val[l][0];
			else k -= jml[l][0];
		} else {
			if (jml[l][1] >= k) return val[l][1];
			else k -= jml[l][1];	
		}
		if (val[l][1]) {
			nex = val[l][1]>>1LL;
			val[l+1][nex&1] = nex;
			jml[l+1][nex&1] += jml[l][1]<<1LL;
		}
		if (val[l][0]) {
			nex = val[l][0]>>1LL;
			val[l+1][nex&1] = nex;
			jml[l+1][nex&1] += jml[l][0];
			nex--;;
			val[l+1][nex&1] = nex;
			jml[l+1][nex&1] += jml[l][0];
		}
		l++;
	}
	assert(false);
}

int main() {
	int tc; gi(tc);
	for (int cs=1; cs<=tc; cs++) {
		scanf("%lld %lld", &n, &k);
		LL ans = solve(), a, b;
		if (ans&1) a = b = (ans>>1LL);
		else {
			a = (ans>>1LL);
			b = (a-1);
		}
		printf ("Case #%d: %lld %lld\n", cs, max(a,b), min(a,b));
	}
	return 0;
}



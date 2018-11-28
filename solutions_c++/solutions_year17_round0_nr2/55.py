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

LL pk[20];
int binser(LL x) {
	int l = 0, r = 18;
	while (l<r) {
		int mid = (l+r)>>1;
		if (pk[mid] < x) l = mid+1;
		else r = mid;
	}
	if (pk[l]>x) l--;
	return l;
}

int n, dp[20][10][2], val[20];
pii nex[20][10][2];

int coba (int now, int bef, int kd) {
	if (now>n) return 1;
	int &ret = dp[now][bef][kd];
	if (ret != -1) return ret;
	pii &nx = nex[now][bef][kd];
	ret = 0; nx = mp(-1,-1);
	for (int i=bef; i<=9; i++) {
	//	if (now==2 && bef==2 && kd==1) printf ("i = %d\n", i);
		if (!kd && i>val[now]) break;
		int id = kd;
		if (!kd && i<val[now]) id = 1;
		if (coba(now+1, i, id)) {
			ret = 1;
			nx = mp(i,id);
		}
	}
	return ret;
}

LL backtrack() {
	LL ret = 0LL;
	int now = 0, bf = 0, kk = 0;
	while (now <= n) {
		ret *= (LL) 10;
		pii nf = nex[now][bf][kk];
	//	printf ("now = %d, bf = %d, kk = %d, nex = %d %d\n", now, bf, kk, nf.fi, nf.se);
		ret += (LL) nf.fi;
		bf = nf.fi; kk = nf.se;
		now++;
	}
	return ret;
}

int main() {
	pk[0] = 1LL;
	for (int i=1; i<=18; i++)
		pk[i] = pk[i-1] * (LL) 10;
	int tc; gi(tc);
	for (int cs=1; cs<=tc; cs++) {
		LL x; scanf("%lld", &x);
		n = binser(x);
	//	printf ("n = %d\n", n);
		for (int i=n; i>=0; i--) {
			val[i] = x%10;
			x /= 10;
		}
		setmin(dp);
		printf ("Case #%d: ", cs);
		if (coba(0,0,0)) {
			LL ans = backtrack();
			printf ("%lld\n", ans);
		} else assert(false);
	}
	return 0;
}



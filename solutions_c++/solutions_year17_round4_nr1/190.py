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

int n, p, a[5];

int main() {
	int tc; gi(tc);
	for (int cs=1; cs<=tc; cs++) {
		setnul(a);
		gi(n); gi(p);
		for (int i=0; i<n; i++) {
			int x; gi(x);
			a[x%p]++;
		}
		int ans = 0;
		ans += a[0];
		if (p==2) {
			ans += a[1]/2;
			a[1] %= 2;
			if (a[1]) ans++;
		} else if (p==3) {
			if (a[1]&&a[2]) {
				int mn = min(a[1], a[2]);
				ans += mn;
				a[1] -= mn;
				a[2] -= mn;
			}
			int ss = max(a[1],a[2]);
			ans += ss/3;
			ss %= 3;
			if (ss) ans++;
		} else if (p==4) {
			if (a[1] && a[3]) {
				int mn = min(a[1],a[3]);
				ans += mn;
				a[1] -= mn;
				a[3] -= mn;
			}
			if (a[2]) {
				ans += a[2]/2;
				a[2] %= 2;
			}
			if (a[3]) a[1] = a[3];
			if (a[1]) {
				if (a[2]) {
					if (a[1]>=2) {
						a[2]--;
						ans++;
						a[1]-=2;
					} else if (a[1]==1) {
						a[2]--;
						a[1]--;
						ans++;
					}
				}
				ans += a[1]/4;
				a[1] %= 4;
				if (a[1]) ans++;
			} else if (a[2]) {
				ans++;
			}
		}
		printf ("Case #%d: %d\n",cs,ans);
	}
	return 0;
}



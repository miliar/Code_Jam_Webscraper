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

void gi( int &ret ) {
	ret = 0; char inp=gc(); int kl=1;
	while (inp<'0' || inp>'9') {if (inp=='-') kl=-1; inp=gc();}
	while ('0'<=inp && inp<='9') ret=(ret<<3)+(ret<<1)+(int)(inp-'0'), inp=gc();
	if (kl<1) ret=-ret;
}

int d, n, k, s;

int main() {
	int tc; gi(tc);
	for (int cs=1; cs<=tc; cs++) {
		gi(d); gi(n);
		double tmp = 0.00000;
		for (int i=0; i<n; i++) {
			gi(k); gi(s);
			tmp = max(tmp, (double)(d-k)/(double)s);
		}
		double ans = (double)d/tmp;
		printf ("Case #%d: %.7lf\n", cs, ans);
	}
	return 0;
}


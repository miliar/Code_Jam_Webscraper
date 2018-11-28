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

const int MAXN = 1005;
int n, a[3], b[3], no[3], isi[MAXN];
char tp[] = {'R','Y','B'};

bool cmp (int x, int y) {
	return a[x] > a[y];
}

void cetak(int x) {
	printf ("%c", tp[x]);
	if (b[x]) {
		b[x]--;
		if (x==0) printf("GR");
		else if (x==1) printf ("VY");
		else printf ("OB");
	}
	return;
}

int main() {
	int tc; gi(tc);
	no[0] = 0; no[1] = 1; no[2] = 2;
	for (int cs=1; cs<=tc; cs++) {
		setnul(a); setnul(b);
		int o,g,v;
		scanf("%d %d %d %d %d %d %d", &n, &a[0], &b[2], &a[1], &b[0], &a[2], &b[1]);
		bool bs = 1;
		for (int i=0; i<3; i++) {
			a[i] -= b[i];
	//		printf ("-%d", a[i]);
			if (a[i]<b[i]) bs = 0;
		}
	//	endln;
		sort(no, no+3, cmp);
	//	for (int i=0; i<3; i++) {
	//		printf ("%d-", a[no[i]]);
	//	}
	//	endln;
		if (a[no[0]] > (a[no[1]]+a[no[2]])) bs = 0;
		if (!bs) {
			printf ("Case #%d: IMPOSSIBLE\n", cs);
			continue;
		}
		printf ("Case #%d: ", cs);
		int lst = 0;
		for (int i=0; a[no[0]]; i+= 2) {
			lst = i;
			isi[i] = no[0];
			a[no[0]]--;
		}
		for (int i=1; i<=(lst+1); i+= 2) {
			if (a[no[1]]) {	
				isi[i] = no[1];
				a[no[1]]--;
			} else {
				isi[i] = no[2];
				a[no[2]]--;
			}
		}
		for (int i=0; i<=lst+1; i++) {
			cetak(isi[i]);
			if (a[no[2]]) {
				cetak(no[2]);
				a[no[2]]--;
			}
		}
		endln;
	}
	return 0;
}


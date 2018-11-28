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

const int maxn = 30;
int tg, lb, area[maxn][maxn], baris[maxn];
char inp[maxn];

int main() {
	int tc; gi(tc);
	for (int cs=1; cs<=tc; cs++) {
		gi(tg); gi(lb);
		setmin(area); setmin(baris);
		for (int i=0; i<tg; i++) {
			scanf("%s", inp);
			for (int j=0; j<lb; j++) {
				if (inp[j]=='?') continue;
				area[i][j] = (int) (inp[j] - 'A');
				baris[i] = i;
			}
		}
		for (int i=1; i<tg; i++) 
			if (baris[i]<0) baris[i] = baris[i-1];
		for (int i=tg-2; i>=0; i--)
			if (baris[i]<0) baris[i] = baris[i+1];
		for (int i=0; i<tg; i++) {
			if (baris[i] != i) continue;
			for (int j=1; j<lb; j++) 
				if (area[i][j]<0) area[i][j] = area[i][j-1];
			for (int j=lb-2; j>=0; j--) 
				if (area[i][j]<0) area[i][j] = area[i][j+1];
		}
		printf ("Case #%d:\n", cs);
		for (int i=0; i<tg; i++){
			int y = baris[i];
			for (int j=0; j<lb; j++) printf ("%c", area[y][j]+'A');
			endln;
		}
	}
	return 0;
}



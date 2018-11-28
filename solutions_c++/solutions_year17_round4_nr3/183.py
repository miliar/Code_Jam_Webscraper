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

const int MAXN = 55;
int tg, lb, val[MAXN][MAXN], ad[MAXN][MAXN], cover[MAXN][MAXN];
char inp[MAXN];
char tipe[] = {'.', '-', '|', '#', '/'};

int analize (char x) {
	for (int i=0; i<5; i++) 
		if (x==tipe[i]) {
			if (i==1 || i==2) return -1;
			return i;
		}
	return 4;
}
int laser (int y, int x) {
	if (val[y][x]<0 || val[y][x]==1 || val[y][x]==2) return 1;
	return 0;
}

bool cek_kolom () {
	for (int i=1; i<=tg; i++) {
		int aw = 1, ak = 1, cnt, st;
		while (aw<=lb) {
			if (val[i][aw]==3) {
				aw++; ak++;
				continue;
			}
			cnt = 0;
			while (ak<=lb && val[i][ak]!=3) {
				if (laser(i,ak)) cnt++;
				ak++;
			}
	//		printf ("aw = %d, ak = %d, cnt = %d\n", aw, ak, cnt);
			while (aw<ak) {
				if (cnt>=2 && laser(i,aw)) {
					if (val[i][aw]==1) return 0;
					val[i][aw] = 2;
					st = i-1;
					while (st>=1 && val[st][aw]!=3) {
						if (laser(st,aw)) return 0;
						ad[st][aw] = 1;
						st--;
					}
					st = i+1;
					while (st<=tg && val[st][aw]!=3) {
						if (laser(st,aw)) return 0;
						ad[st][aw] = 1;
						st++;
					}
				} else cover[i][aw] += cnt;
				aw++;
			}
		}
	}
//	printf ("berhasil\n");
//	for (int i=1; i<=tg; i++) {
//		for (int j=1; j<=lb; j++) printf ("%2d ", val[i][j]);
//		endln;
//	}
	return 1;
}

bool cek_baris() {
	for (int i=1; i<=lb; i++) {
		int aw = 1, ak = 1, cnt, st;
		while (aw<=tg) {
			if (val[aw][i]==3) {
				aw++; ak++;
				continue;
			}
			cnt = 0;
			while (ak<=tg && val[ak][i]!=3) {
				if (laser(ak,i)) cnt++;
				ak++;
			}
//			printf ("aw = %d, ak = %d, cnt = %d\n", aw, ak, cnt);
			while (aw<ak) {
				if (cnt>=2 && laser(aw,i)) {
					if (val[aw][i]==2) return 0;
					val[aw][i] = 1;
					st = i-1;
					while (st>=1 && val[aw][st]!=3) {
						if (laser(aw,st)) return 0;
						ad[aw][st] = 1;
						st--;
					}
					st = i+1;
					while (st<=lb && val[aw][st]!=3) {
						if (laser(aw,st)) return 0;
						ad[aw][st] = 1;
						st++;
					}
				} else cover[aw][i] += cnt;
				aw++;
			}
		}
	}
//	printf ("berhasil\n");
//	for (int i=1; i<=tg; i++) {
//		for (int j=1; j<=lb; j++) printf ("%2d ", val[i][j]);
//		endln;
//	}
	return 1;
}

int needlr (int y, int x) {
	int st = x-1, dpt = 0;
	while (st>=1 && val[y][st]!=3) {
		if (ad[y][st]) { st--; continue; }
		if (cover[y][st]==1) return 1;
		dpt = 1;
		st--;
	}
	st = x+1;
	while (st<=lb && val[y][st]!=3) {
		if (ad[y][st]) { st++; continue; }
		if (cover[y][st]==1) return 1;
		dpt = 1;
		st++;
	}
	if (dpt) return 2;
	return 0;;
}

int needud (int y, int x) {
	int st = y-1, dpt = 0;
	while (st>=1 && val[st][x]!=3) {
		if (ad[st][x]) { st--; continue; }
		if (cover[st][x]==1) return 1;
		st--;
	}
	st = y+1, dpt = 0;
	while (st<=tg && val[st][x]!=3) {
		if (ad[st][x]) { st++; continue; }
		if (cover[st][x]==1) return 1;
		st++;
	}
	if (dpt) return 2;
	return 0;
}

void applylr (int y, int x) {
	val[y][x] = 1;
	int st = x-1;
	while (st>=1 && val[y][st]!=3) ad[y][st--] = 1;
	st = x+1;
	while (st<=lb && val[y][st]!=3) ad[y][st++] = 1;
	return;
}
void applyud (int y, int x) {
	val[y][x] = 2;
	int st = y-1;
	while (st>=1 && val[st][x]!=3) ad[st--][x] = 1;
	st = y+1;
	while (st<=tg && val[st][x]!=3) ad[st++][x] = 1;
	return;
}

bool ceka () {
	for (int i=1; i<=tg; i++) 
		for (int j=1; j<=lb; j++) {
			if (val[i][j]>=0) continue;
			int nlr = needlr(i,j), nud = needud(i,j);
		//	printf ("%d %d -> %d %d\n", i, j, nlr, nud);
			if (nlr==1 && nud==1) return 0;
			if (nlr==1) applylr(i,j);
			else if (nud==1) applyud(i,j);
			else if (nlr==2) applylr(i,j);
			else applyud(i,j);
		}
	return 1;
}

bool cekb() {
//	for (int i=1; i<=tg; i++) {
//		for (int j=1; j<=lb; j++) printf ("%d", ad[i][j]);
//		endln;
//	}
	for (int i=1; i<=tg; i++) 
		for (int j=1; j<=lb; j++) 
			if (val[i][j]==0 && !ad[i][j]) return 0;
	return 1;
}


int main() {
	int tc; gi(tc);
	for (int cs=1; cs<=tc; cs++) {
		gi(tg); gi(lb);
		setnul(ad); setnul(cover);
		for (int i=1; i<=tg; i++) {
			scanf("%s", inp);
			for (int j=0; j<lb; j++) 
				val[i][j+1] = analize(inp[j]);
		}
		printf ("Case #%d: ", cs);
		if (!cek_kolom() || !cek_baris() || !ceka() || !cekb()) {
			printf ("IMPOSSIBLE\n");
			continue;
		}
		printf ("POSSIBLE\n");
		for (int i=1; i<=tg; i++) {
			for (int j=1; j<=lb; j++) {
				assert(val[i][j]>=0);
				printf ("%c", tipe[val[i][j]]);
			}
			endln;
		}
		
	}
	return 0;
}



#include<stdio.h>
#include<stdlib.h>

// testowe rozwiazanie, ktore sluzy do wyswietlena wartosci ciagu
// oraz do zaliczenia pierwszego rozwiazania (small 1)

bool stall[1002];	// czy budka wolna
int n;

// funkcja sprawdzajaca dla danej pozycj min i max
bool check(int pos, int& res_min, int &res_max) {
	if(!stall[pos]) return false;	// bledne sprawdzanie kabina juz zajeta

	int l=pos;
	while(stall[l-1]) --l;
	int r=pos;
	while(stall[r+1]) ++r;
	
	l=pos-l;
	r=r-pos;
	if(l>r) {
		res_min=r; res_max=l;
	} else {
		res_min=l; res_max=r;
	}
	return true;
}

int find_next(int& res_min, int &res_max) {

	int best=-1;
	int best_min=0;
	int best_max=0;
	// sprawdzamy glupio wszystkie mozliwosci
	for(int i=1;i<=n;++i) {
		if(!stall[i]) continue;
		
		check(i, res_min, res_max);
		if(best_min<res_min) {
			best=i;	// nowy najmineszy
			best_min=res_min;
			best_max=res_max;
		} else if(best_min==res_min) {
			if(best_max<res_max) {
				best=i;	// nowy najlepszy
				best_max=res_max;
			}
		}
	}
	if(best==-1) return -1;
	stall[best]=false;	// zajmujemy miejsce, wiec nie jest juz wolna
	res_min=best_min;
	res_max=best_max;
	return best;
}

int main(int argc, char** argv) {
	int t;

	scanf("%d",&t);
	stall[0]=false;
	for(int tst=0;tst<t;++tst) {
		int k;
		int res_max, res_min;
		scanf("%d %d", &n, &k);
		for(int i=0;i<n;++i) stall[i+1]=true;
		stall[n+1]=false;	// straznik

		for(int i=0;i<k;++i) {
			int p=find_next(res_min, res_max);
			//printf("N=%d, K=%d, Step=%d, At=%d, Max=%d, Min=%d\n", n, k, i, p, res_max, res_min);
		}
		
		printf("Case #%d: %d %d\n", tst+1, res_max, res_min);
	}
}

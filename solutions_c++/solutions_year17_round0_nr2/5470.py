#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
#include <inttypes.h>

int64_t calc(int64_t in, int64_t val, int limit, int64_t m) {
	if(in==0) return val;	// koniec obliczen, bo juz wszystko przetworzono

	int last=in%10;	// ostatnia cyfra dla aktualnej liczby
	int64_t next_in=in/10;

	if(last>=limit) {	// jezeli ostatnia cyrfa jest wieksza od obecnego limitu cyfry
		val+=limit*m;	// to ja wybieramy, bo nie ma lepszego rozwiazania
		return calc(next_in, val, limit, m*10);	// i przetwarzamy dalsza cyfre
	}
	// gdy ostatnia cyfra aktalnego stanu jest mniejsza od limitu, to sa dwie mozliwosci
	int64_t a=calc(next_in, val+last*m, last, m*10);	// opcja 1 - zmniejszamy limit i testujemy w takim trybie
	// opcja 2 - zmniejszamy wartosci kolejnej liczby i wowczas ostatnia liczba moze byc 9-tka
	--next_in;
	if(next_in>=0) {	// opcja 2 ma sens, jak jest z czego pozyczyc
		int64_t b=calc(next_in, val+limit*m, limit, m*10);
		if(a>b) return a;
		else return b;
	} else {
		return a;
	}
}

int main(int argc, char** argv) {
	int t;

	scanf("%d", &t);
	for(int n=0;n<t;++n) {
		int64_t in;
		scanf("%"PRId64, &in);
		
		int64_t res=calc(in, 0, 9, 1);

		printf("Case #%d: %"PRId64"\n", n+1, res);
	}
	return 0;
}

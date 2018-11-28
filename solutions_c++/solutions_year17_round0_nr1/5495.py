#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char** argv) {
	char in[1005];
	bool fl[2002];	// tablica informacji o obrotach (true) - w tym miejscu konczy sie obrot
	int k,t;

	scanf("%d", &t);
	for(int n=0;n<t;++n) {
		scanf("%s %d", in, &k);
		int len=strlen(in);
		for(int i=0;i<len;++i) fl[i]=false;

		bool st=true;	// stan obrucenia - true - brak obrotu, stan oryginalny
		int res=0;
		for(int i=0;i<len;++i) {
			bool v;
			if(fl[i]) st=!st;		// koniec jakios obortu, wiec aktualizujemy stan

			if(in[i]=='+') v=st;
			else v=!st;

			if(!v) {	// jezeli jest na -, to musimy obrocic
				if(i>len-k) { res=-1; break; } 	// juz nie mozna zrobic obrotu, wiec koniec
				++res;		// zliczamy obrot
				st=!st;	// aktualizujemy stan obecny
				fl[i+k]=true;		// zapisujemy gdzie skonczy sie obrot
			}
		}
		printf("Case #%d: ", n+1);
		if(res==-1) {
			printf("IMPOSSIBLE\n");
		} else {
			printf("%d\n",res);
		}
	}
	return 0;
}

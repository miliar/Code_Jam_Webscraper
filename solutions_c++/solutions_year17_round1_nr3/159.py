#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

/* Real Main */
void ___() {
	int Hd, Ad, Hk, Ak, B, D;
	int turn = -1;
	scanf("%d %d %d %d %d %d", &Hd, &Ad, &Hk, &Ak, &B, &D);

	int i, ii; /* Buff */
	int j, jj; /* Debuff */
	int k;
	for(i=0;i<=100;i++) {
		for(j=0;j<=100;j++) {
			int hd=Hd, ad=Ad, hk=Hk, ak=Ak;
			ii = 0, jj = 0;
			for(k=0;k<1000;k++) {
				if(hk-ad <= 0) hk -= ad;
				else if((jj >= j && hd - (ak) <= 0) ||
					 (jj < j && hd - (ak-D) <= 0)) {
					hd = Hd;
				} else if(jj < j) {
					jj++, ak -= D;
					if(ak < 0) ak = 0;
				} else if(ii < i) {
					ii++, ad += B;
				} else {
					hk -= ad;
				}
				if(hk <= 0) break;
				hd -= ak;
				if(hd <= 0) break;
			}
			if(hk <= 0 && (turn == -1 || turn > k + 1)) turn = k + 1;
		}
	}

	if(turn == -1) printf("IMPOSSIBLE\n");
	else printf("%d\n", turn);
}



/* Fake Main */
int main() {
	int T, i;
	/* Test Case */
	scanf("%d", &T);
	for(i=0;i<T;i++) {
		printf("Case #%d: ", i + 1);
		___();
	}
	return 0;
}

#include <stdio.h>
#include <string.h>

//int check[15];
//int check[110];

/*
void flip(int si, int checking) {

	for (int i = 0; i <= si; i++) {
		check[i] = checking;
	}
}

int flipPancake(int si, int fi, int checking, int& dab) {

	//end recursive
	if (si == fi) {
		if (check[fi] == 0) {
			dab++;
			return dab;
		}
		else  return dab;
	}

	//for recursive
	for (int i = si; i <= fi; i++) {
		if (check[i] != checking) {
			si = i;
			checking = check[i];
			break;
		}

		if (i == fi) {
			if (check[i] == 0)	return ++dab;
			else return dab;
		}

	}

	dab++;
	flip(si - 1, checking);
	dab = flipPancake(si, fi, checking, dab);

	return dab;

}
*/

int main(void)
{
	int t, n, dab;
	int check[3];
	//char small[10];
	//char large[1000];

	FILE *fin = fopen("B-small-attempt5.in", "r");
	FILE *fout = fopen("B-small-attempt5.out", "w");
	fscanf(fin, "%d", &t);
	//scanf("%d", &t);

	for (int i = 1; i <= t; i++) {

		dab = 0;
		fscanf(fin, "%d", &n);
		//scanf("%d", &n);
		//fscanf(fin, "%d", k);
		//scanf("%d", k);

		//n = strlen(small);	//string length

		int length = 1;
		int temp = n;

		if (n < 10) {
			dab = n;
		}
		else if (n >= 999) {
			dab = 999;
		}
			
		else {
			while (temp >= 10) {
				temp /= 10;
				length++;
			}

			temp = n;

			for (int j = 0; j < length; j++) {
				check[j] = temp % 10;
				temp /= 10;
			}
			temp = n;

			if (length == 3) {
				if (check[0] >= check[1]) {
					if (check[1] >= check[2]) dab = n;	
					else dab = (check[2] - 1) * 100 + 99;
				}
				else {
					if (check[1] > check[2]) dab = check[2] * 100 + (check[1] - 1) * 10 + 9;
					else dab = (check[2] - 1) * 100 + 99;
				}
			}

			else {
				if (n == 99) dab = 99;
				else if (check[0] >= check[1]) {
					dab = n;
				}
				else {
					dab = (check[1] - 1) * 10 + 9;
				}
			}

		}
		

		fprintf(fout, "Case #%d: %d\n", i, dab);
		//printf("Case # %d: %d\n", i, dab);

	}

	fclose(fin);
	fclose(fout);

}
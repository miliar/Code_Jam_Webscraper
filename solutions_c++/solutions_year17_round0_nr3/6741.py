#include<bits/stdc++.h>
using namespace std;

#define MAXN 1000

bool bath[MAXN+5];

struct place {
	int a, b, c;
};

place compare (place p1, place p2) {

	if (p1.a > p2.a) return p1;
	else if (p1.a == p2.a) {

		if (p1.b > p2.b) return p1;
		else if (p1.b == p2.b){
			if (p1.c < p2.c) return p1;
			return p2;
		}
		else if (p1.b < p2.b) return p2;
	}
	else if (p1.a < p2.a) return p2;

}

int main () {
	
	int t=0, n=0, k=0, i=0, j=0;
	int sr=0, sl=0, chico=0, grande=0, res1=0, res2=0, pos=0;

	scanf("%d", &t);

	for (int c=1; c<=t; c++) {

		scanf("%d %d", &n, &k);

		memset(bath, 0, sizeof(bath));

		bath[0] = bath[n+1] = 1;
		

		for (int idx=0; idx<k; idx++) {

			//res1 = INT_MIN;
			//res2 = INT_MIN;
			//chico = INT_MIN;
			//grande = INT_MIN;
			//pos = -1;

			place p1, p2;
			p1.a = p1.b = p1.c = -1;
			p2.a = p2.b = p2.c = -1;


			//look available
			for (i=1; i<=n; i++) {
				
				if (bath[i] == 0) {

					//look left
					for (j=i-1; j>=0; j--)
						if (bath[j] == 1){
							sl = j;
							sl = abs(i-j)-1;
							break;
						}

					//look right
					for (j=i+1; j<=n+1; j++)
						if (bath[j] == 1){
							sr = j;
							sr = abs(i-j)-1;
							break;
						}

					/*
					//get maximal of minimun
					int aux2 = max(chico, min(sr, sl)); 
					//get maximal of maximal
					if (aux2 > chico) { 
						chico = aux2;
						grande = max(grande, max(sr, sl));
						pos = i;
					}
					else if (chico == min(sr, sl)) { // CHECK THIS IF !!!
						int aux = max (grande, max(sr, sl));
						if (aux > grande) { //new pos
							pos = i;
							grande = aux;
						}
					}
					*/

					p2.a = min(sr, sl);
					p2.b = max(sr, sl);
					p2.c = i;

					p1 = compare(p1, p2);

					//printf("%d %d %d\n", p1.a, p1.b, p1.c);

					//printf("sl = %d sr = %d chico = %d grande = %d pos = %d\n", sl, sr, chico, grande, pos);
				}

				
			}

			bath[p1.c] = 1;
			//cout << "taken " << p1.c << endl;

			
			
			

			//give answer
			if (idx == k-1) {

				//for (j=0; j<=n+1; j++) cout << bath[j]<<" ";
				//cout << endl;

				for (j=p1.c-1; j>=0; j--)
					if (bath[j] == 1){
						sl = j;
						sl = abs(p1.c-j)-1;
						break;
					}

				//look right
				for (j=p1.c+1; j<=n+1; j++)
					if (bath[j] == 1){
						sr = j;
						sr = abs(p1.c-j)-1;
						break;
					}

				res1 = max(sl, sr);
				res2 = min(sl, sr);
				cout << "Case " << (char)(35) << c << (char)(58) << " " << res1 << " " << res2 << endl;
			}
		}

	}


	return 0;
}
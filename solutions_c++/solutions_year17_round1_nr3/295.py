#include<bits/stdc++.h>
using namespace std;

const int INF = 2e+9;
int TC, TCs;
int Hd, Ad, Hk, Ak, B, D;
int condition[110][110][2];/*D, B, curHd, roundsPassed*/
int ans[110][110];
int i, x, y, c, fAns;

int AttackPower(int a, int de){
	if (a>de) return a-de;
	return 0;
}

int main(){
	scanf("%d", &TCs);
	for (TC=1; TC<=TCs; TC++){
		printf("Case #%d: ", TC);
		scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);
		
		for (i=0; i<=100; i++) for (x=0; x<=100; x++) ans[i][x] = INF;
		
		condition[0][0][0] = Hd;
		condition[0][0][1] = 0;
		
		/* Debuff */
		for (i=1; i<=100; i++){
			condition[i][0][0] = condition[i-1][0][0] - AttackPower(Ak, i*D);
			condition[i][0][1] = condition[i-1][0][1]+1;
			if (condition[i][0][0]<=0){
				condition[i][0][0] = Hd - AttackPower(Ak, (i-1)*D);
				condition[i][0][1] = condition[i-1][0][1]+1;
				condition[i][0][0] -= AttackPower(Ak, i*D);
				condition[i][0][1] ++;
				if (condition[i][0][0]<=0){
					condition[i][0][0] = 0;
					condition[i][0][1] = INF;
				}
			}
		}
		
		/* Buff */
		for (i=0; i<=100; i++) for (x=1; x<=100; x++){
			condition[i][x][0] = condition[i][x-1][0] - AttackPower(Ak, i*D);
			condition[i][x][1] = condition[i][x-1][1]+1;
			if (condition[i][x][0]<=0){
				condition[i][x][0] = Hd - AttackPower(Ak, i*D);
				condition[i][x][1] = condition[i][x-1][1]+1;
				condition[i][x][0] -= AttackPower(Ak, i*D);
				condition[i][x][1] ++;
				if (condition[i][x][0]<=0){
					condition[i][x][0] = 0;
					condition[i][x][1] = INF;
				}
			}
		}
		
		/* Attack */
		for (i=0; i<=100; i++) for (x=0; x<=100; x++) if (condition[i][x][0]){
			int curHd = condition[i][x][0];
			int curAd = Ad+x*B;
			int curHk = Hk;
			int curAk = AttackPower(Ak, i*D);
			int curT = condition[i][x][1];
			
			if (curHk<=curAd){
				ans[i][x] = curT+1;
				continue;
			}
			if (Hd<=curAk){
				ans[i][x] = INF;
				continue;
			}
			
			while(curHk||curHd){
				if (curHk<=curAd){
					curT++;
					break;
				}
				
				/* Cure */
				if (curHd<=curAk){
					curHd = Hd-curAk;
					curT++;
				}
				
				/* Check Cure */
				if (Hd<=curAk*2){
					curT = INF;
					break;
				}
				
				/* Attack */
				curHk -= curAd;
				curHd -= curAk;
				curT++;
			}
			
			ans[i][x] = curT;
		}
		
		fAns = INF;
		for (i=0; i<=100; i++) for (x=0; x<=100; x++) fAns = min(fAns, ans[i][x]);
		if (fAns==INF) puts("IMPOSSIBLE");
		else printf("%d\n", fAns);
		
/*
puts("Hd before Attack");
for (i=0; i<10; i++){
	for (x=0; x<10; x++) printf("%d ", condition[i][x][0]);
	puts("");
}
puts("rounds before Attack");
for (i=0; i<10; i++){
	for (x=0; x<10; x++) printf("%d ", condition[i][x][1]);
	puts("");
}
puts("rounds after Attack");
for (i=0; i<10; i++){
	for (x=0; x<10; x++) printf("%d ", ans[i][x]);
	puts("");
}*/

		
	}
	
	return 0;
}

/*
4 11 5 16 5 0 0 3 1 3 2 2 0 3 1 3 2 1 0 2 1 5 1 1 1
*/

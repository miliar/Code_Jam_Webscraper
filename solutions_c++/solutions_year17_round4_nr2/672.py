#include<bits/stdc++.h>
using namespace std;

int TCs, TC;
int seats, N, M;
int ticket[1010][1010];
int countS[1010];
int i, x, y, c, ansR, ansP;

int main(){
	scanf("%d", &TCs);
	for (TC=1; TC<=TCs; TC++){
		printf("Case #%d: ", TC);
		
		scanf("%d%d%d", &seats, &N, &M);
		memset(ticket, 0, sizeof(ticket));
		memset(countS, 0, sizeof(countS));
		
		for (i=0; i<M; i++){
			int P, B;
			scanf("%d%d", &P, &B);
			ticket[B][P]++;
		}
		
		ansR = 0;
		ansP = 0;
		
		// For each person
		for (i=1; i<=N; i++){
			c = 0;
			for (x=1; x<=seats; x++) c += ticket[i][x];
			ansR = max(ansR, c);
		}
		
		// For each position
		c = 0;
		for (i=1; i<=seats; i++){
			for (x=1; x<=N; x++) countS[i] += ticket[x][i];
			c += countS[i];
			ansR = max(ansR, (c+i-1)/i);
		}
		
		// ansR completed
		for (i=1; i<=seats; i++) ansP += max(0, countS[i]-ansR);
		
		printf("%d %d\n", ansR, ansP);
	}
	
	return 0;
}

/*
5
2 2 2 2 1 2 2
2 2 2 1 1 1 2
2 2 2 1 1 2 1
1000 1000 4 3 2 2 1 3 3 3 1
3 3 5 3 1 2 2 3 3 2 2 3 1
*/

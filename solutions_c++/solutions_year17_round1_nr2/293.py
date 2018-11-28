#include<bits/stdc++.h>
using namespace std;

int TC, TCs;
int N, P;
int setFood[60];
int food[60][60];
int xF[60];
int minP[60];
int maxP[60];
int i, x, y, ans, curMin;

void Update(int i, int x){
	minP[i] = (food[i][x]*10+setFood[i]*11-1)/(setFood[i]*11);
	maxP[i] = (food[i][x]*10)/(setFood[i]*9);
	if (minP[i]>curMin) curMin = minP[i];
//printf("Update: food %d %d min %d max %d\n", i, x, minP[i], maxP[i]);
	return ;
}

int Check(){
	for (i=0; i<N; i++) if (maxP[i]<curMin){
		xF[i]++;
		if (xF[i]>=P) return 0;
		
		Update(i, xF[i]);
		return 1;
	}
	
	ans++;
	for (i=0; i<N; i++){
		xF[i]++;
		if (xF[i]>=P) return 0;
		
		Update(i, xF[i]);
	}
	
	return 1;
}

int Compute(){
	ans = 0;
	
	curMin = 0;
	
	for (i=0; i<N; i++){
		Update(i, 0);
		xF[i] = 0;
		if (minP[i]>curMin) curMin = minP[i];
	}
	
	while(Check());
	return ans;
}

int main(){
	scanf("%d", &TCs);
	for (TC=1; TC<=TCs; TC++){
		printf("Case #%d: ", TC);
		scanf("%d%d", &N, &P);
		for (i=0; i<N; i++) scanf("%d", &setFood[i]);
		for (i=0; i<N; i++){
			for (x=0; x<P; x++) scanf("%d", &food[i][x]);
			sort(food[i], food[i]+P);
		}
		
		printf("%d\n", Compute());
		
/*puts("food");
for (i=0; i<N; i++){
	for (x=0; x<P; x++) printf("%d ", food[i][x]);
	puts("");
}*/
	}
	
	return 0;
}

/*
6 2 1 500 300 900 660 2 1 500 300 1500 809 2 2 50 100 450 449 1100 1101 2 1 500 300 300 500 1 8 10 11 13 17 11 16 14 12 18 3 3 70 80 90 1260 1500 700 800 1440 1600 1700 1620 900
*/

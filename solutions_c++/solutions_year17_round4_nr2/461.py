#include<iostream>
#include<stdio.h>
#include<string.h>
#include <algorithm>
#define FR(i,a,b) for(i=a;i<b;++i)
#define FRS(i,a,b,s) for(i=a;i<b;i+=s)
#define FRE(i,a,b) for(i=a;i<=b;++i)
#define FRES(i,a,b,s) for(i=a;i<=b;i+=s)
// 0->tt-1		FR(i, 0, tt) printf(" 1");
// 0,2,4->tt-1	FRS(i, 0, tt, 2) printf(" 2");
// 0->tt		FRE(i, 0, tt) printf(" 3");
// 0,2,4->tt	FRES(i, 0, tt, 2) printf(" 4");
using namespace std;

int i, j, x, y, z;
long long n, c, m;
int tt;
int perCust[1005];
int perSeat[1005];
int sumSeat[1005];
	
void run(){
	cin >> n >> c >> m;
	FR(i, 0, 1002) perSeat[i] = 0;
	FR(i, 0, 1002) perCust[i] = 0;
	int maxx = 0;
	int pr = 0;
	FR(i, 0, m) {
		cin >> x >> y;
		perSeat[x]++;
		perCust[y]++;
	}
	FRE(i, 1, c) if(perCust[i] > maxx) { maxx = perCust[i]; pr=0; };
	sumSeat[0] = 0;
	FRE(i, 1, n) {
		sumSeat[i] = sumSeat[i-1] + perSeat[i];
		if(sumSeat[i] > i * maxx) {
			maxx = (sumSeat[i] + i - 1)/ i;
//printf(" m:%d %d", maxx, i);
		}
	}
	FRE(i, 1, n){
		if(perSeat[i] > maxx) pr+= perSeat[i] - maxx;
	}
	printf(" %d %d", maxx, pr);
}

int main(){
	int T;
	scanf("%d", &T);
	for(tt =1; tt<=T; tt++){
		printf("Case #%d:",tt); // standard
		run();
		printf("\n"); // endline
	}
	return 0;
}

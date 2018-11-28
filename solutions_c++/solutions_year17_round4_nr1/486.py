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

int i, j,p,x,y,z;
long long n, k;
int tt;

int num[5];
	
void run(){
	cin >> n >> p;
	FR(i,0,5) num[i] = 0;
	FR(i,0,n) {
		cin >> j;
		num[j % p]++;
	}
//FR(i,0,p) {printf("%d ;", num[i]);}
	long cnt = num[0];
	num[0] = 0;
	if(p==2){
		cnt += (num[1]+1)/2;
	} else if (p==3){
		x = (num[1] < num[2]) ? num[1] : num[2];
		num[1] -= x;
		num[2] -= x;
		cnt += x;
		cnt += (num[1] + num[2] + 2) / 3;
	} else if(p==4) {
		x = num[2]/2;
		cnt += x;
//printf("%ld ", cnt);
		num[2] -= x * 2;
		x = (num[1] < num[3]) ? num[1] : num[3];
		num[1] -= x;
		num[3] -= x;
		cnt += x;
		if(num[2] > 0){
			if(num[1] > 1) { num[1] -=2; num[2]--; cnt++;}
			else if(num[3] > 1) { num[3] -=2; num[2]--; cnt++;}
			else {cnt++; num[1] = num[3] = 0;}
//printf("%ld ", cnt);
		}
		cnt += (num[1] + num[3] + 3) / 4;
	}
	printf(" %ld", cnt);
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

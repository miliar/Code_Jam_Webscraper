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

// R O Y G B V
// BOBOB
// RGRGR
// YVYVY

int i, j, r, o, y, g, b, v;
long long n, k;
int tt;
	
void run(){
	cin >> n >> r >> o >> y >> g >> b >> v;
	if(n==1){
		if(r>0) printf(" R");
		else if (o>0) printf(" O");
		else if (y>0) printf(" Y");
		else if (g>0) printf(" G");
		else if (b>0) printf(" B");
		else if (v>0) printf(" V");
		return;
	}

	bool ok = true;
	if(o >0 && (o > b || (o==b && o+b !=n))) ok = false;
	if(g >0 && (g > r || (g==r && g+r !=n))) ok = false;
	if(v >0 && (v > y || (v==y && v+y !=n))) ok = false;
	
	if( (b-o) + (r -g) < (y - v)) ok = false;
	if( (r-g) + (y-v) < (b-o)) ok = false;
	if( (y-v) + (b-o) < (r-g)) ok = false;
	printf(" ");
	if(!ok) {
		printf("IMPOSSIBLE"); 
		return;
	}

	char last  = ' ';
	char first = ' ';
	while( r + o + y + g + b + v > 0){
		//printf("%d %d %d %d %d %d\n", r, o, y, g, b, v);
		if(b >0 && (b-o > r-g || (b-o == r-g && (first == 'B' || first == ' ')) || last == 'R') && (b-o > y-v || (b-o == y-v && (first == 'B' || first == ' ')) || last == 'Y') && last != 'B'){
			if(o >0){
				FR(i,0,o) printf("BO");
				b -= o;
				o -= o;
				if(first == ' ') first = 'B';
				last = 'O';
			}
			if (b > 0) {
				printf("B");
				b--;
				last = 'B';
			}
		}
		//else if (r > 0 && (r-g > b-o || (r-g == b-o && first == 'R') || last == 'B') && (r-g > y-v || (r-g == y-v && first == 'R') || last == 'Y') && last != 'R'){
		else if (r > 0 && (r-g > y-v || (r-g == y-v && (first == 'R' || first == ' ')) || last == 'Y') && last != 'R'){
			if(g >0){
				FR(i,0,g) printf("RG");
				r -= g;
				g -= g;
				if(first == ' ') first = 'R';
				last = 'G';
			}
			if(r > 0) {
				printf("R");
				r--;
				last = 'R';
			}
		}
		else {
			if(last == 'Y') printf("======");
			if(v >0){
				FR(i,0,v) printf("YV");
				y -= v;
				v -= v;
				if(first == ' ') first = 'Y';
				last = 'V';
			}
			if (y > 0 ) {
				printf("Y");
				y--;
				last = 'Y';
			}
		}
		if(first == ' ') first = last;
	}
	if(first == last) printf("===");
	return;
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

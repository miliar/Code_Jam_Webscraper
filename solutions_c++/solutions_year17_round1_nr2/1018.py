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

bool debug = false;

int i, j,k;
int n,p;
int tt;
int q[51][51]; // n,p
int r[51];
bool used[51][51];
int ava[51];
int occ[51];

void run(){
	cin >> n >> p;
	FR(i,0,n) cin >> r[i];
	FR(i,0,n) FR(j,0,p) cin >> q[i][j];
	FR(i,0,n) sort(q[i], q[i]+p);
	
	FR(i,0,n) FR(j,0,p) used[i][j] = false;
	FR(i,0,n) ava[i] = 0;
	FR(i,0,n) occ[i] = -1;

	int cnt = 0;
	j = 1;
if(debug) printf("\n");
	FR(i,0,p)
	{
		if(j < q[0][i] * 10 / (r[0] * 11)) j = q[0][i] * 10 / (r[0] * 11);
if (debug)		printf("!!! %d %d\n", j, q[0][i] * 11 / r[0] / 10);
		for(; j <= q[0][i] * 10 / (r[0] *9); j++){ 
		// assume take q[0][i], j is the possible package
		//FR(j,q[0][i] * 9 / r[0] / 10, q[0][i] * 11 / r[0] / 10 + 1){
			// at most 10^6 / 10 * 2 = 20000
if (debug)		printf("@@@ j: %d\n", j);
			FR(k,0,n){
				long long needed = r[k];
				long long minP = needed, maxP = needed;
				minP = minP * j * 9 / 10;
				maxP = maxP * j * 11 / 10;
if(debug)				printf("!!! k: %d, min: %lld, max: %lld\n", k, minP, maxP);
				for(;ava[k] < p && q[k][ava[k]] <= maxP; ava[k]++){
					if(q[k][ava[k]] < minP) continue; 
					break;
				}
				if(ava[k] == p || q[k][ava[k]] > maxP){
if(debug)	printf("!!! not match for k: %d, ava[k]: %d, q[k][ava[k]]: %d\n", k, ava[k], q[k][ava[k]]);
					break;
				}
			}
			if(k==n) {
if(debug){
				printf("=== Matched\n");
				printf("=== using: ");
				FR(k,0,n) printf(" %d", ava[k]);
				printf("\n");
}
				cnt++;
				//FR(k,0,n) ava[k] = occ[k];
				FR(k,0,n) ava[k]++;
				break; // as matching found
			}
		}
	}
	printf(" %d", cnt);
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

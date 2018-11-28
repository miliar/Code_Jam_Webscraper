#include<stdio.h>
#include<iostream>
#include<utility>
#define fi first
#define se second
#define mp make_pair
#define llu unsigned long long int
#define repn(i,a,b) for(int i=a; i<b; i++)
using namespace std;

pair<llu, llu> solve ( int N, int K ) {
	if ( N==K ) return mp(0, 0);
	
	int n = N-1;
	int ls_n = n/2;
	int rs_n = n-ls_n;
	
	int k = K-1;
	int ls_k = k/2;
	int rs_k = k-ls_k;
	
	if ( K==1 ) return mp(rs_n, ls_n);
	if ( K==2 ) return solve(rs_n, 1);
	if ( n%2==0 ) return solve(rs_n, rs_k);
	else if ( k%2==0 ) return solve(ls_n, ls_k);
	else return solve(rs_n, rs_k);
}


int main ( ) {
	freopen("C-small-2-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int qq; scanf("%d", &qq);
	repn(tt,1,qq+1) {
		llu n, k;
		scanf("%llu %llu", &n, &k);
		
		pair<llu, llu> answer = solve(n, k);
		printf("Case #%d: %llu %llu\n", tt, answer.fi, answer.se);
	}
}

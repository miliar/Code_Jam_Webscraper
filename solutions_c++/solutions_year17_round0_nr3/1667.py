// Lupus Nocawy
// 2017-04-08
// Google Code Jam
// Qualification Round 2017
// https://code.google.com/codejam
// https://code.google.com/codejam/contest/3264486/dashboard
// Problem C. Bathroom Stalls

#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long int lli;

lli chooseMiddle(lli n){
	lli q = (n-1)/2 + 1;
	return q;
}

void solve(int c){
	lli n, k;
	lli l=0, r=0;
	scanf("%lli %lli ", &n, &k);
	while(k>0){
		lli q = chooseMiddle(n);
		l = q-1;
		r = n-q;
		k--;
		if(k%2==1)
			n = max(l,r);
		else
			n = min(l,r);
		k = k/2 + k%2;
	}
	printf("%lli %lli\n", max(l,r), min(l,r));
}

int main(void){
	int t;
	scanf("%d ", &t);
	for(int c=1; c<=t; ++c){
		printf("Case #%d: ", c);
		solve(c);
	}
	return 0;
}

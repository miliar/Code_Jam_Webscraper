// Lupus Nocawy
// 2017-04-08
// Google Code Jam
// Qualification Round 2017
// https://code.google.com/codejam
// https://code.google.com/codejam/contest/3264486/dashboard
// Problem B. Tidy Numbers

#include <cstdio>
using namespace std;
typedef long long int lli;

bool isTidy(lli n){
	int d = n%10;
	n /= 10;
	while(n){
		if(n%10>d)
			return 0;
		d = n%10;
		n /= 10;
	}
	return 1;
}

void solve(int c){
	long long int n;
	scanf("%lli ", &n);
	lli k=10;
	while(not isTidy(n)){
		n -= n%k+1;
		k*=10;
	}
	printf("%lli\n", n);
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

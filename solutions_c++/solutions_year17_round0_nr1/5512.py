#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#define FOR(i,a,b) for(i=a; i<=b; i++)
#define FOR2(i,n) FOR(i,0,n-1)
#define TFOR(i,a,b) for(i=a; i>=b; i--)
#define f first
#define s second
#define all(x) x.begin(),x.end() 
#define MAXN 1005
using namespace std;
typedef pair < int , int > pii;
int read(){ int res(0),sign(1); char c;
	while(1){ c = getchar(); if('0' <= c && c <= '9') { res = c - '0'; break; } else if(c == '-') { sign = -1; break; } }
	while(1){ c = getchar(); if('0' <= c && c <= '9') res = res*10 + c - '0'; else break; }
	return res * sign;
}
char A[MAXN];
void solve() {

	int K,i,j,res(0);

	scanf("%s" , A+1);
	int N = strlen(A+1);
	scanf("%d" , &K);

	FOR(i,1,N-K+1)
		if(A[i] == '-') {
			FOR(j,i,i+K-1)
				A[j] = '+' + '-' - A[j];
			res++;
		}

	FOR(i,1,N)
		if(A[i] == '-') {
			printf("IMPOSSIBLE\n");
			return;
		}

	printf("%d\n" , res);


}
int main()
{
	int T = read(), i;
	FOR(i,1,T){
		printf("Case #%d: " , i);
		solve();
	}
	return 0;
}

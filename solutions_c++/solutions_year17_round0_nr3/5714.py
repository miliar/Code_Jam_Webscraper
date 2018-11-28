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
int K,N;
bool A[MAXN];
int L[MAXN], R[MAXN];

int add(){

	int i,x(-1),t1,t2;
	FOR(i,1,N)
		if(!A[i]){
			if(x == -1) x = i;
			t1 = min(i-L[i],R[i]-i);
			t2 = min(x-L[x],R[x]-x);
			if(t1 > t2)
				x = i;
			else if(t1 == t2 && max(i-L[i],R[i]-i) > max(x-L[x],R[x]-x))
				x = i;
		}

	A[x] = true;

	FOR(i,x+1,R[x]) L[i] = x;

	FOR(i,L[x],x-1) R[i] = x;

	return x;


}
#include <cstdlib>
void solve() {

	int i,x;
	memset( A , 0 , sizeof A );
	memset( L , 0 , sizeof L );
	memset( R , 0 , sizeof R );
	A[0] = A[N+1] = true;
	FOR(i,1,N) R[i] = N+1;
	FOR(i,1,K) x = add();

	printf("%d %d\n", max(x-L[x],R[x]-x) - 1, min(x-L[x],R[x]-x) - 1);


}
int main()
{
	int T = read(), i;
	FOR(i,1,T){
		printf("Case #%d: " , i);
		scanf("%d %d", &N , &K);
		solve();
	}
	return 0;
}

#include <bits/stdc++.h>
using namespace std;

#define ll unsigned long long
#define test(t) int t; scanf("%d", &t); while(t--)
#define forr(I, a, b) for(int I = a; I < b; I++)
#define pb push_back

ll stall(ll number){
	ll n = 1;
	while(n <= number)
		n = n*2;
	n =n/2;
	return n;
}
 
int main(){
	int T;
	scanf("%d",&T);
	forr(i, 0, T){
		ll N,M;
		scanf("%lld %lld",&N, &M);
		ll base = stall(M);
		ll val = (N-M + base)/base;
		ll x = val/2;
		ll y = (val-1)/2;
		printf("Case #%d: %lld %lld\n",i + 1, x ,y);
	}
	return 0;
}
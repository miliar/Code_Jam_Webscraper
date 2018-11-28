#include <bits/stdc++.h>

using namespace std;

const int N=1000070; //10e6

#define ll long long int
#define inf 0x3f3f3f3f
#define pb push_back
#define eb emplace_back
#define fi first
#define se second
#define ii tuple<int, int>
#define all(x) (x).begin(), (x).end()

void solve(ll k, ll n){
	priority_queue<ll>pq;
	pq.push(n);
	ll aux=0;
	ll a1, a2;

	while(k--){
		aux=pq.top();
		pq.pop();
		if(aux%2){
			pq.push(aux/2);
			a1=a2=aux/2;
			pq.push(aux/2);
		}else{
			a1=aux/2;
			a2=(aux-1)/2;
			pq.push((aux-1)/2);
			pq.push((aux)/2);
		}
	}

	printf("%lld %lld\n", a1, a2);
}

int main(int argc, char const *argv[]){
	int t;
	scanf("%d", &t);
	int counter=1;
	while(t--){
		ll k, n;
		scanf("%lld %lld", &n, &k);
		printf("Case #%d: ", counter++);
		solve(k, n);

	}
	return 0;
}
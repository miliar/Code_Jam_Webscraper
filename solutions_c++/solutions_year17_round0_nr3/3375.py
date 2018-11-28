#include <bits/stdc++.h> // PLEASE

using namespace std;
typedef long long ll;
typedef pair <int, int> pp;
#define MAXN 1005
#define MAXM 1005
#define MAXP 25
#define INF 2000000000
#define HAX 10000000 
#define A first
#define B second
#define MP make_pair
#define PB push_back
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define re(i, n) FOR(i, 1, n)
#define rep(i, n) for(int i = 0; i<(n); ++i)
#define fore(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
ll N, K;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		cin >> N >> K;
		if(N == K) {
			printf("Case #%d: 0 0\n", t);
			continue;
		}
		priority_queue <ll> PQ;
		PQ.push(N);
		while(K--) {
			ll x = PQ.top();
			PQ.pop();
			if(x%2) {
				PQ.push(x/2);
				PQ.push(x/2);
			}
			else {
				PQ.push(x/2);
				PQ.push(x/2-1);
			}
			x--;
			ll a = (x+1)/2;
			ll b = (x)/2;
			if(K == 0) {
				printf("Case #%d: %lld %lld\n", t, a, b);
				break;
			}
		}
	}
	
	
}

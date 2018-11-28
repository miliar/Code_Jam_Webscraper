#include <bits/stdc++.h>

#define FOR(i, a, n) for(int i = (int)(a); i < (int)(n); ++i)
#define REP(i, n) FOR(i, 0, n)
#define all(a) a.begin(),a.end()
#define pb push_back
#define LSOne(S) (S & (-S))
#define dbg(x) cerr << ">>>> " << x << endl;
#define _ << " , " <<
#define mp make_pair
#define f first
#define s second
#define ii pair<int,int>
#define maxn 7777

typedef unsigned long long llu;
typedef long long int ll;
typedef long double ld;

const int INF = 0x3f3f3f3f;
const double EPS = 1e-6;

using namespace std;

int main(){
	int t;
	scanf("%d", &t);
	for(int caso = 1; caso <= t; caso++){
		llu n,k,top;
		scanf("%llu %llu", &n, &k);
		map<llu, llu> order; order.insert(mp(n,1));
		while(k){
			llu chave = order.rbegin()->first;
			llu life = order[chave];
			llu left = chave/2, right = max((chave-1)/2, 0LLU);
			if(life >= k){
				k = 0;
				printf("Case #%d: %llu %llu\n", caso, left, right);
			} else {
				k -= life;
				if(order.find(left) == order.end()) order.insert(mp(left, life));
				else order[left] += life;
				
				if(order.find(right) == order.end()) order.insert(mp(right, life));
				else order[right] += life;
				
				order.erase(order.rbegin()->first);
			}
		}
	}
	return 0;
}






















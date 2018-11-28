#include <bits/stdc++.h>

//LIFE IS NOT A PROBLEM TO BE SOLVED

using namespace std;

#define rep(i,a,b) for(int i = int(a); i < int(b) ; i++)
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef long long int ll;
typedef unsigned long long int ull;
typedef pair < ll, ll > ii;
typedef pair < ll, ii > iii;

const int INF = 0x3f3f3f3f;
const ll LINF = 1LL<<58;

ll N, K, m, M;

priority_queue <ll> pq;
map <ll, ll> mapa;

void solve(){
	
	ll ini=0, fim=N+1, mid=(ini+fim)/2;
	pq.push(fim-ini); mapa[fim-ini]=1;
	
	while(K){
		mid=pq.top(); pq.pop();
		
		ll qt=mapa[mid];
		ll go=mid/2; m=go, M=mid-go, K-=qt;
		
		if(K<=0) break;
		
		if(mapa.count(go)){
			mapa[go]+=qt;
		}else{
			mapa[go]=qt;
			pq.push(go);
		}
		
		if(mapa.count(go+(mid&1))){
			mapa[go+(mid&1)]+=qt;
		}else{
			mapa[go+(mid&1)]=qt;
			pq.push(go+(mid&1));
		}
		
	}
	
	return;
	
}

int main()
{
	
	freopen("CB.in", "r", stdin);
	freopen("CB.sol", "w", stdout);
	
	int T, z=1; cin >> T;
	
	while(T--){
		
		m=1, M=1;
		scanf("%lld %lld", &N, &K);
		
		mapa.clear();
		while(!pq.empty()) pq.pop();
		
		if(N!=K) solve();
		
		printf("Case #%d: %lld %lld\n", z++, M-1, m-1);
		
	}
	
	return 0;
	
}

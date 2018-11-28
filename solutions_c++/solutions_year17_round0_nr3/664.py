#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for(int i = a; i < (b); i++) 
#define fi first
#define se second
#define pb push_back
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d %d", &a, &b)
#define sc3(a,b,c) scanf("%d %d %d", &a, &b)
#define pri(a) printf("%d\n", a)
#define mp make_pair
#define DESYNC ios_base::sync_with_stdio(false)

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef long long int ll;

const int INF = 0x3f3f3f3f;
const ll LINF = 0x3f3f3f3f3f3f3f3f;
const int MOD = 1000000007;
const double PI = acos(-1);

int main(){
	ll t;
	ll n, k;
	ll mini, maxi;
	map<ll, ll> s;
	
	cin>>t;
	
	fr(caseNum, 1, t+1){
		cin>>n>>k;
		s.clear();
		s[n] = 1;
		while(k > 0){
			map<ll,ll>::iterator it = s.end();
			it--;
			ll gap = it->fi;
			ll qtd = it->se;
			s.erase(it);
			
			gap--;
			mini = gap/2;
			maxi = (gap+1)/2;
			s[mini] += qtd;
			s[maxi] += qtd;
			k -= qtd;
		}
		printf("Case #%d: %lld %lld\n", caseNum, maxi, mini);
		
	}
	
	return 0;
}

#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sz(a) ((int)(a).size())
#define rep(i, a, b) for(int (i) = (a); (i) < (b); (i)++)
#define dec(i, a, b) for (int (i) = (a); (i) >= (b); (i)--)
#define clr(a,v) memset(a, v, sizeof(a))
#define all(a) (a).begin(),(a).end()
#define MAXN 101010
#define LOGN 20
#define EPS 1e-10
#define fcin ios_base::sync_with_stdio(false)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

ll n, k;
map<ll,ll> qt;

int main(){
	int t;
	scanf("%d", &t);
	rep(caso,1,t+1){
		scanf("%lld%lld", &n, &k);
		qt.clear();
		qt[n] = 1;
		ll a, b;
		while(k>0){
			ll v = qt.rbegin()->x, q = qt.rbegin()->y;
			qt.erase(qt.find(v));
			k -= q;
			a = v/2, b = v-a-1;
			if(b) qt[b] += q;
			if(a) qt[a] += q;
		}
		printf("Case #%d: %lld %lld\n", caso, a, b);
	}
}


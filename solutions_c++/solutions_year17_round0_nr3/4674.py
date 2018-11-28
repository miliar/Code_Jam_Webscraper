using namespace std;
#include <bits/stdc++.h>
#define rep(i,n) for(int i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define rite(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define clr clear()
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9
typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef long long ll;

#define mx 0
#define INF 10e9+7
typedef pair<ll, ll> pl;
ll maxi (ll a, ll b){return a>b?a:b;}
ll mini (ll a, ll b){return a<b?a:b;}

pl go(ll N, ll K){
	ll i = 0;
	ll j = N;
	ll mid;
	ll x = 1;
	ll lK = (ll)log2(K) + 1;
	//printf("%lld\n", lK);
	ll c = 1;
	while(i<=j){
		mid = (i+j)/2;
		//ll s = (ll) pow(2, x++);
		//printf("%lld\n", s);
		//printf("%lld %lld\n", j, mid);
		if(lK==x++) return pl(mid-i, j-mid-1);

		//if(K>s) return pl(-1, -1); 
		else{
			if(K%2==0){
				j = mid;
			}else{
				i = mid+1;
			}

			K/=2;
		}
	}
	return pl(-2, -2);

}
int main() {
   	ios_base::sync_with_stdio(0);cin.tie(NULL);
   	//Solution
	ll T;
	scanf("%lld", &T);
	for (ll t = 1; t <= T; ++t)
	{
		
		ll N, K;
		scanf("%lld %lld", &N, &K);
		pl res = go(N, K);
		printf("Case #%d: %lld %lld\n",t,  res.xx, res.yy);
	}
   	
   	
   	return 0;
}


//g++-4.9 bath.cpp -o bath && ./bath < bath.in > bath.txt


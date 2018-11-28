#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<char> vc;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;
const double EPS = 1e-9;
const int INF = 1 << 29;
#define mp make_pair
#define el putchar('\n')
#define sp putchar(' ')
#define Fill(a,val) memset(a,val,sizeof a)
#define all(a) a.begin(),a.end()
#ifndef ONLINE_JUDGE
#define tr(a, it) for (decltype(a.begin()) it = a.begin(); it != a.end(); ++it)
#else
#define tr(a, it) for (typeof(a.begin()) it = a.begin(); it != a.end(); ++it)
#endif
#define in(n) scanf("%d",&n)
#define inl(n) scanf("%lld",&n)
#define out(n) printf("%d",n);
#define outl(n) printf("%lld",n);

ll MoPela(map<ll, ll>magya){
	ll ret = 0;
	tr(magya, it){
		if (it->first)
			ret += it->second;
	}
	return ret;
}

int main(){
	freopen("ip.in", "r", stdin);
	freopen("op.out", "w", stdout);
	int t; in(t);
	for (int bia = 1; bia <= t; ++bia){
		ll n, k; inl(n); inl(k); --k;
		
		map<ll, ll>magya;
		magya[n] = 1;
		ll tatti;
		while ((tatti=MoPela(magya)) <= k){
			map<ll, ll>nn;
			tr(magya, it){
				ll numberrrr = it->first;
				ll cnt = it->second;
				ll numberrrr1 = (numberrrr >> 1ll) - ((numberrrr & 1ll) == 0);
				if(numberrrr1 > 0)nn[numberrrr1] += cnt;
				ll numberrrr2 = (numberrrr >> 1ll);
				if (numberrrr2 > 0)nn[numberrrr2] += cnt;
			}
			magya = nn;
			k -= tatti;
		}
		vector<pair<ll, ll> > runudaari;
		tr(magya, it){
			runudaari.push_back(mp(it->first, it->second));
		}
		sort(all(runudaari));
		ll sz = runudaari.size();
		bool moBanda = false; printf("Case #%d: ", bia);
		for (ll i = sz - 1; i >= 0; --i){
			ll numberrrr = runudaari[i].first, cnt = runudaari[i].second;
			if (cnt <= k){
				k -= cnt; continue;
			}
			outl(numberrrr >> 1ll); sp; outl((numberrrr >> 1ll) - ((numberrrr & 1ll) == 0)); el; moBanda = true; break;
		}
		if (!moBanda){
			puts("0 0");
		}
	}
	return 0;
}
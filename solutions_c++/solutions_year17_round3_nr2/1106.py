//Shubham Vijayvargiya

#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;

#define pb push_back
#define mp make_pair
#define eb emplace_back
#define F first
#define S second
#define sz(a) (int)(a.size())
#define set(a,b) memset(a,b,sizeof(a))
#define let(x,a) __typeof(a) x(a)
#define rep(i, begin, end) for (ll i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define all(v) (v).begin(),(v).end()
#define sll(x) { scanf("%lld",&x); }
#define si(x) { scanf("%d",&x); }
#define slf(x) { scanf("%lf",&x); }
#define pll(x) { printf("%lld\n",x); }
#define pi(x) { printf("%d\n",x); }
#define tcases() long long testcases; cin>>testcases ; while(testcases--)

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
    cerr << name << " = " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " = " << arg1<<" | ";__f(comma+1, args...);
}

#else
#define trace(...)
#endif

template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;

typedef long long ll;
typedef long double ld;
typedef pair<long long,long long> pll;
typedef vector<long long> vll;
typedef vector<pll> vpll;
typedef vector<vll> vvll;

const ll mod=1000000007;
//----------------------------------------------------------------------------------------------------------------------------------------------//

pll a[102],b[102];

int main(){
//	ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	ll tc;
	sll(tc);
	ll TC=tc;
	while(tc--){
		ll n,m;
		sll(n);sll(m);
		rep(i,0,n){
			sll(a[i].F);sll(a[i].S);
		}
		rep(i,0,m){
			sll(b[i].F);sll(b[i].S);
		}
		ll ans;
		if(n==m || n+m==1){
			ans=2;
		}
		else{
			if(n>0){
				sort(a,a+n);
				if((a[1].S-a[0].F)>12*60 && (a[1].F-a[0].S)<12*60)
					ans=4;
				else
					ans=2;
			}
			if(m>0){
				sort(b,b+m);
				if((b[1].S-b[0].F)>12*60 && (b[1].F-b[0].S)<12*60)
					ans=4;
				else
					ans=2;
			}
		}
		cout<<"Case #"<<TC-tc<<": "<<ans<<endl;
	}
	return 0;
}


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
//-----------------------------------------------------------------------------------------------------------------------------------------------//


int main()
{
//	ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	ll ttt;
	sll(ttt);
	for(int tc=1;tc<=ttt;tc++){
		cout<<"Case #"<<tc<<": ";
		map<pll,ll> m;
		ll n,k;
		sll(n);sll(k);
		queue<pll> q;
		q.push({n,k});
		m[mp(n,k)]=1;
		ll ansn=n;
		while(!q.empty()){
			pll p=q.front();
			ll nn=p.F;ll kk=p.S;
//			trace(nn,kk);
			q.pop();
//			m[p]=1;
			ll l=(nn-1)>>1;
			ll r=nn>>1;
			ll lk=(kk-1)/2;
			ll rk=kk/2;
			if(lk==1){
				if(ansn>l)
					ansn=l;
			}
			if(rk==1){
				if(ansn>r)
					ansn=r;
			}
			if(lk!=0 && m[mp(l,lk)]==0)
				q.push({l,lk});
			if(rk!=0 && m[mp(r,rk)]==0)
				q.push({r,rk});
			m[mp(l,lk)]=1;
			m[mp(r,rk)]=1;
		}
		cout<<ansn/2<<" "<<(ansn-1)/2<<endl;
//		cout<<sz(m)<<endl;
	}
	return 0;
}



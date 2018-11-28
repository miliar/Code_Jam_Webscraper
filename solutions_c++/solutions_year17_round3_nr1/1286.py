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
//--------------------------------------------------------------------------------------------------------------------------------------------
#define PI acos(-1.0)
//ld PI=3.14159265;
pair<ld,ld> a[1009];

int main(){
//	ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	ll tc;
	sll(tc);
	ll TC=tc;
	while(tc--){
		ll n,k;
		ld ans2=0.0;
		sll(n);sll(k);
		rep(i,0,n){
			cin>>a[i].F>>a[i].S;
			if(k==1){
//				trace(2.0*PI*(a[i].F*a[i].S),PI*(a[i].F*a[i].F));
				ans2=max(ans2,2.0*PI*(ld)(a[i].F*a[i].S)+PI*(ld)(a[i].F*a[i].F));
			}
//			trace(ans2);
		}
		sort(a,a+n);
		ld ans=0.0;
		rep(i,0,n){
			if(i+k-1>=n)
				break;
			set<ld> s;
			ld sum=0.0;
			rep(j,i+1,i+k-1){
				s.insert(a[j].F*a[j].S);
				sum+=a[j].F*a[j].S;
			}
			sum+=a[i].F*a[i].S;
			rep(j,i+k-1,n){
				ans=max(ans,2.0*PI*(ld)(sum+a[j].F*a[j].S)+PI*(ld)(a[j].F*a[j].F));
				if(!s.empty()){
					if(*(s.begin())<a[j].F*a[j].S){
						ld p=*(s.begin());
						sum-=p;
						s.erase(s.begin());
						s.insert(a[j].F*a[j].S);
						sum+=a[j].F*a[j].S;
					}
				}
			}
		}
		if(k==1)
			ans=ans2;
		cout<<fixed<<setprecision(9);
		cout<<"Case #"<<TC-tc<<": "<<ans<<endl;
	}
	return 0;
}


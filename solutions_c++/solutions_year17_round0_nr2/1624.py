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
#define INF 1e15
ll n,dp[20][10][2],ans;
string s;

ll recur(ll i,ll j,ll x,ll cur){
//	if(i==2 && x==9)
//		trace(i,j,x,cur,dp[i][x][j]);
	if(i==n){
		ans=max(ans,cur);
		return 0;
	}
	if(j==0 && (s[i]-'0')<x){
		return dp[i][x][j]=-INF;
	}
	if(dp[i][x][j]!=-1){
		ans=max(ans,cur+dp[i][x][j]);
//		if(ans==1008)
//			trace(i,j,x,cur,dp[i][x][j]);
		return dp[i][x][j];
	}

	dp[i][x][j]=0;
	for(int k=0;k<=9-x;k++){
//		trace(i,j,k,x);
		if(j==0 && (x+k)>(s[i]-'0'))
			break;
		ll tmp=1;
		for(int l=i;l<n;l++){
			tmp=tmp*10;
		}
		tmp--;
		tmp/=9;
		tmp*=k;
		ll ret=0;
		if(x+k<(s[i]-'0')){
			ret=recur(i+1,1,x+k,cur+tmp);
		}
		else{
			ret=recur(i+1,j,x+k,cur+tmp);
		}
//		if(i==2 && x==9)
//			trace(k,tmp,ret);
		dp[i][x][j]=max(dp[i][x][j],ret+tmp);
	}
	return dp[i][x][j];
}

int main()
{
//	ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	ll ttt;
	sll(ttt);

	for(int tc=1;tc<=ttt;tc++){
		printf("Case #%d: ",tc);
		set(dp,-1);
		cin>>s;
		n=sz(s);
		ans=0;
		recur(0,0,0,0);
		cout<<ans<<endl;
	}
	return 0;
}



#include<bits/stdc++.h>

using namespace std;

#define TRACE
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1) {
  cerr << name << " : " << arg1 << endl;
}

template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args) {
  const char* comma = strchr(names + 1, ',');
  cerr.write(names, comma - names) << " : " << arg1<<" | ";
  __f(comma+1, args...);
}
#else
#define trace(...)
#endif

#define all(a) a.begin(), a.end()
#define endl '\n'
#define mp make_pair
#define pb push_back
#define f first
#define s second
#define boost  ios_base::sync_with_stdio(false);
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)

typedef long long llint;
typedef long long ll ;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;

const ll mod = 1e9 + 7 ;
ll powmod(ll a,ll b) {ll res=1;if(a>=mod)a%=mod;for(;b;b>>=1){if(b&1)res=res*a;if(res>=mod)res%=mod;a=a*a;if(a>=mod)a%=mod;}return res;}
ll gcd(ll a , ll b){return a==0?b:gcd(b%a,a);}
/*---------------------------------------------------------------------------------------------------------------------*/
const int maxn = 100010;
const int inf = INT_MAX;
vector<ll> n[20];
int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	ll num = 0;
	ll i, j;
	for(i = 1; i <= 18; i++) {
		num = num * 10 + 1;
		for(j = 0; j <= 9; j++)
			n[i].pb(num * j);
		n[i].pb(mod * 1LL * mod);
	}
	ll t = 0, tt = 0;
	cin >> t;
	while(t--) {
		tt++;
		cout << "Case #" << tt << ": ";	
		ll N;
		ll cur = 0;
		cin >> N;
		for(i = 18; i; i--) {
			for(j = 0; cur + n[i][j] <= N && 9 >= cur % 10 + n[i][j] % 10; j++) {

			}
			cur += n[i][j - 1];
		}
		cout << cur << endl;
	}
	cin.get();
	cin.get();
    return 0;
}
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#ifdef DEBUG
    #define cek(x) cout<<x
#else
    #define cek(x) if(false){}
#endif // DEBUG

#define fi first
#define se second
#define INF 1000000000
#define INFLL 1000000000000000000LL
#define EPS 1e-9
#define PI acos(-1.0)
#define pb push_back
#define TC() while(tc--)
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORN(i,n) for(int i=0;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define REPN(i,a,b) for(int i=a;i<=b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define SORTA(v,n) sort(v, v + n)
#define SZ(v) (int) v.size()
#define sc(x) scanf("%d",&x)

void open(){
	freopen("D:/OneDrive/Code/GCJ/C-large.in","r",stdin);
	freopen("D:/OneDrive/Code/GCJ/out_coba.txt", "w", stdout);
}

int main(void){
	open();
	int tc;
	sc(tc);

	for(int ct = 1; ct <= tc; ct++){
		ll n, k;		
		ll kk;
		cin >> n >> k;
		kk = k;
		ll minus = 1;
		map<ll,ll> mp;
		mp[n] = 1;
		
		while(k > 1){
			map<ll,ll> tmp;
			for(map<ll,ll>::iterator it = mp.begin(); it != mp.end(); it++){
				ll num = it->first;
				tmp[num/2] += it->second;
				tmp[(num-1)/2] += it->second;
			}
			
			mp = tmp;
			
			k/=2;
			kk -= minus;
			minus *= 2;
		}

	
		ll tot = 0;
		for(map<ll,ll>::reverse_iterator it = mp.rbegin(); it != mp.rend(); it++){
			if(tot + it->second >= kk){
				n = it->first;
				printf("Case #%d: %lld %lld\n", ct, (n/2), (n-1)/2);
				break;
			}
			tot += it->second;
		}

		
	
		cerr << "Test " << ct << " done \n";
	}
    return 0;
}



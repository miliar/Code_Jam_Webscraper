#include <bits/stdc++.h>
#define X first
#define Y second
#define psb push_back
#define pob pop_back
#define mp make_pair
#define ll long long
#define scand(n) scanf("%d",&n)
#define scanld(n) scanf("%lld",&n)
#define printd(n) printf("%d\n",n)
#define printld(n) printf("%lld\n",n)
#define all(x) x.begin(),x.end()
#define SET( arr, val) memset(arr,val,sizeof(arr))
#define ITR iterator
#define SZ(arr) arr.size()
#define FOR( i, L, U ) for(int i=(int)L ; i<(int)U ; ++i )
#define FORI( i, L, U ) for(int i=(int)L ; i<=(int)U ; ++i )
#define FORD( i, U, L ) for(int i=(int)U ; i>=(int)L ; --i )
#define Tcases(t) int t;cin>>t;while(t--)
#define INPFILE freopen("input.in","r",stdin)
#define OUTFILE freopen("output.txt","w",stdout)
#define debug(x) cerr << "[DEBUG] " << #x << " = " << x << endl

using namespace std;

typedef vector<int> vi;
typedef pair<int,int> pii;

ll mpow(ll a, ll n,ll mod)
{ll ret=1;ll b=a;while(n) {if(n&1)
    ret=(ret*b)%mod;b=(b*b)%mod;n>>=1;}
return (ll)ret;
}

int T;
ll n,k;
map<ll,ll> m;

ll mn,mx;

void grv(){
	while(k>0){
		auto it=m.rbegin();
		ll cur=it->X;
		ll val=it->Y;
		m.erase(it->X);

		mx=mn=cur/2;
		if((cur&1) == 0)
			--mn;
		if(mx)
			m[mx]+=val;
		if(mn)
			m[mn]+=val;
		k-=val;

//        cout<< cur<<" "<<val<<" "<<mx<<" "<<mn<<endl;
	}
}

int main() {
freopen("inp3.in","r",stdin);
freopen("output3.txt","w",stdout);
	cin>>T;
	FORI(t,1,T){
		cin>>n>>k;
		m.clear();
		++m[n];

        grv();

		cout<<"Case #"<<t<<": "<<mx<<" "<<mn<<endl;

	}

	return 0;
}

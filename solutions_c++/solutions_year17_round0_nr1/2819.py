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

string s;
int T,k,sz,ans;

void flip(int st){
    FOR(i,0,k)
        s[st+i]=(s[st+i]=='+'?'-':'+');
}

int main() {
freopen("inp.in","r",stdin);
freopen("output.txt","w",stdout);
	cin>>T;
	FORI(t,1,T){
        cin>>s>>k;
        sz=s.size();
        ans=0;
        FOR(i,0,sz){
            if(s[i]=='-'){
                if(i>sz-k){
                    ans=-1;
                    break;
                }
                ans++;
                flip(i);
            }
        }
        cout<<"Case #"<<t<<": ";
        if(ans<0)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<ans<<endl;
	}

	return 0;
}

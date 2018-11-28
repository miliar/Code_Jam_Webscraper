/*
*  Author : pritish.thakkar 
*/
#include<bits/stdc++.h>
#define pb push_back
#define mkp make_pair
#define inf 10000000070000000
#define rep(i,n) for(int i=0;i<n;i++)
#define fr first
#define sc second
#define clr(a) memset(a,0LL,sizeof a);
#define sn(t) scanf("%lld",&t)
#define pn(t) printf("%lld",t)
#define WHITE 0
#define BLACK 1
using namespace std;
typedef unsigned long long ull;
typedef  long long ll;
typedef vector<ll> vi;
typedef pair<ll,ll> ii;
typedef vector<ii> vii;
bool isUpper(char c) {return (c >= 'A' && c <= 'Z');}
bool isLower(char c) {return (c >= 'a' && c <= 'z');}
bool isalpha(char c) {return (c >= 'A' && c <= 'Z')||(c >= 'a' && c <= 'z');}
bool isalnum(char c) {return (c >= 'A' && c <= 'Z')||(c >= 'a' && c <= 'z')||(c >= '0' && c <= '9');}
char toUpper(char c){return isUpper(c)?c:c-'a'+'A';}
char toLower(char c){return isLower(c)?c:c+'a'-'A';}
ll hcf(ll a,ll b){return ((b == 0) ? a : hcf(b, a%b));} 
ll modpow(ll base, ll expo, ll mod){
    base  = base % mod;
    ll ret = 1LL;
    while(expo > 0){
        if(expo & 1LL)
                ret =( ret * base) % mod;
        base = (base * base )% mod;
        expo >>= 1LL;
    }
    return ret;
}
 
//-----------------------------------------------------------------------------------------------------------------------------
// Enter Your code here
 
ll sieve_size;
bitset <1000010> bs;
vector<ll> primes;
  
void sieve(ll upperbound){
sieve_size=upperbound+1;
bs.reset(),bs.flip();//set all nos. to 1
bs.set(0,false);bs.set(1,false);//except 0 ans 1
for(ll i=2;i<=sieve_size;i++){
    if(bs.test((size_t)i)){
        for(ll j=i*i;j<=sieve_size;j+=i){
            bs.set((size_t)j,false);
        }
        primes.push_back((ll)i);
        }
    }
}
 
// ------------------------------------------


void solve(){
  freopen("in","r",stdin);
  freopen("out","w",stdout);
    int t;
    cin>>t;
    for(int tt = 1; tt <= t; tt++){
        ll d,n;
        cin>>d>>n;
        vii v;
        for(int i=0;i<n;i++){
            ll x,y;
            cin>>x>>y;
            v.pb(ii(x,y));
        }
        sort(v.begin(), v.end());
        double dist = 1.00*v[n-1].fr;
        double speed = 1.00*v[n-1].sc;
        double ans = 1.00*(speed * d) / (d - dist);
        for(int i=n-2;i>=0;i--){
            ii p1 = v[i];
            if(1.00*(d - dist)/speed > 1.00*(d - p1.fr)/p1.sc){
                double tim = 1.00 * ( dist - p1.fr ) * (p1.sc - speed);
                dist += speed * tim;
                tim += (d-dist)/speed;
                ans = 1.000 * (d) / tim; 
            }else{  
                speed = p1.sc;
                dist = p1.fr;
                ans = 1.0000000 * (speed * d) / (d - dist);
            }
        }    
        cout<<setprecision(6)<<fixed;
        cout<<"Case #"<<tt<<": "<<ans<<endl; 

    }  

}

//-----------------------------------------------------------------------------------------------------------------------------
int main(){
std::ios::sync_with_stdio(0);
solve();
}  
//    AND NOW IT BEGINS      //
#include<bits/stdc++.h>
using namespace std;
#define SF(x)	scanf("%d", &x)
#define SFL(x) scanf("%lld",&x)
#define sf(x) scanf("%Lf",&x)
#define sc(x) scanf(" %c",&x)
#define PF(x)	printf("%d", x)
#define PFL(x) printf("%lld",x);
#define psp     printf(" ")
#define pnl     printf("\n")
#define pie     cout<<" # "<<endl
#define pii pair< int, int >
#define pb(x) push_back(x)
#define test int t; scanf("%d",&t);while(t--)
#define forall(i,a,b) for(int i=(a);i<=(b);++i)
#define gcd(a,b)   __gcd(a,b)
#define bss binary_search
#define ersort(x)       (sort((x).rbegin(), (x).rend()))
#define rev(v)      (reverse(v.begin(),v.end()))
#define vmax(v)     (*max_element(v.begin(),v.end()))
#define vmin(v)     (*min_element(v.begin(),v.end()))
#define MAX		400050
#define INF		1e12
#define INFL 0x3f3f3f3f3f3f3f3fLL
#define mod     1000000007
#define ROUNDOFFINT(d) d = (int)((double)d + 0.5)
#define fi first
#define se second
inline bool isPowerOfTwo(int x){ return (x != 0 && (x&(x - 1)) == 0); }
typedef long long 		ll;
double pi = 3.141592653589793238462643;
typedef unsigned long long	ull;
int dx[8] = {1 , 0 , -1 , 0 , 1 , -1 , -1 , 1};    // last 4 diagonal
int dy[8] = {0 , 1 , 0 , -1 , 1 , 1 , -1 , -1};
inline int add(int a,int b, int m=mod){a+=b;if(a>=m)a-=m;return a;}
inline int mul(int a,int b, int m=mod){return (int)(((ll)a*(ll)b)%m);}
inline bool ispalin(string& str){ int n = str.length(); for (int i = 0; i < n / 2; i++) if (str[i] != str[n - i - 1]) return false; return true; }
ll expo(ll base,ll pow){
    ll ans = 1;
    while(pow!=0){
        if(pow&1==1){
            ans = ans*base;
            ans = ans%mod;
        }
        base *= base;
        base%=mod;
        pow/=2;
    }
    return ans;
}
void swapp(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
ll inv(ll x){
    return expo(x,mod-2);
}
int expFactor(int n, int p)
{
    int x = p;
    int exponent = 0;
    while ((n/x) > 0)
    {
        exponent += n/x;
        x *= p;
    }
    return exponent;
}
inline int countsetbit(int n)
{
    unsigned int count = 0;
    while (n)
    {
      n &= (n-1) ;
      count++;
    }
    return count;
}
inline int abs(int x){
	if(x<0)
	return -x;
	return x;
}
bool isPal(string ss){
    int len = ss.length();
    for(int i = 0 ; i<len/2 ; i++){
	int comp = len-i-1;
	if(ss[i]!=ss[comp])
		return false;
	}
    return true;
}
ll _sieve_size; 
bitset<10000010> bs; 
vector <int> primes; 
void sieve(ll upperbound) { 
	_sieve_size = upperbound + 1; 
	bs.set();
	bs[0] = bs[1] = 0;
	for (ll i = 2; i <= _sieve_size; i++) 
	if (bs[i]) {
		for (ll j = i * i; j <= _sieve_size; j += i) 
			bs[j] = 0;
		primes.push_back((int)i); 
	} 
} 
bool isPrime(ll N) {
if (N <= _sieve_size) return bs[N]; 
for (int i = 0; i < (int)primes.size(); i++)
if (N % primes[i] == 0) return false;
return true;
} 
//     AND NOW IT ENDS        //
int main(){
	//freopen("d.in", "r", stdin);
    //freopen("d.out", "w", stdout);
    int t;
    cin>>t;
    for(int c=1;c<=t;c++){
		ll n,d;
		cin>>d>>n;
		cout<<"Case #"<<c<<": ";
		int res=0,i,ts;
		ll k[n],s[n];
		double tm[n];
		for( i=0;i<(int)n;i++){
			cin>>k[i]>>s[i];
			tm[i]=(d-k[i])*1.0/s[i];
			if(tm[ts]<tm[i]){
				ts=i;
			}
		}
		printf("%.10f",d*1.0/tm[ts]);cout<<endl;
    }
}

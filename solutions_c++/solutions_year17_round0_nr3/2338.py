#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef vector < int > vi;
typedef vector < ll > vll;
typedef vector < string > vs;
typedef vector < vll > matrix;

#define DEBUG false
#define sz(a) int((a).size()) 
#define sl(a) int((a).length()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rall(c) (c).rbegin(),(c).rend() 
#define tr(con,it) for (__typeof((con).begin()) it = con.begin(); it != con.end(); it++) 
#define wl(x) (cout << (x) << endl)
#define w(x) (cout << (x))
#define r(x) (cin >> (x))
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define ROF(i,a,b) for (int i = (b-1); i >= (a); i--)
#define PP(x) tr(x,it) cout << it->first << " " << it->second << endl
#define mp(x,y) make_pair((x),(y))
#define reset(x) memset((x),0,sizeof((x)))
#define log(x) if (DEBUG) cout << #x << " = " << x << endl
#define log2(x,y) if (DEBUG) cout << #x << " = " << x << " " << #y << " = " << y << endl
#define log3(x,y,z) if (DEBUG) cout << #x << " = " << x << " " << #y << " = " << y << " " << #z << " = " << z << endl
#define log4(x,y,z,t) if (DEBUG) cout << #x << " = " << x << " " << #y << " = " << y << " " << #z << " = " << z << " " << #t << " = " << t << endl
#define log5(x,y,z,t,v) if (DEBUG) cout << #x << " = " << x << " " << #y << " = " << y << " " << #z << " = " << z << " " << #t << " = " << t << " " << #v << " = " << v << endl
#define MAXN 1000010
#define MAXK 105
#define MDL 1000000007
#define EPS 1e-10
#define IO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0);
string to_str(const int &n){ostringstream stm; stm << n;return stm.str();}
string to_str(const ll &n){ostringstream stm; stm << n;return stm.str();}
ll powmod(ll a,ll b) {ll res=1;a%=MDL;for(;b;b>>=1){if(b&1)res=res*a%MDL;a=a*a%MDL;}return res;}
ll gcd(ll a,ll b) {return b==0?a:gcd(b,a%b);}
ll lcm(ll a,ll b) {return a*(b/gcd(a,b));}
int T=1;

ll n,k;
vector < bool > x;
vector < pair < pair < ll, ll > , int > > LR;
ll lc,rc,res1,res2;

void solve()
{
ll left_s=0,right_s=1,diff,dist,temp;

 res1=res2=0;

 while((temp=2*left_s+1)<=n) left_s=temp;
 res2=left_s/2;
 while((temp=2*right_s)<=k) { right_s=temp; res2/=2; }
 if (left_s < right_s) return;

 diff=n-left_s;

 dist=(diff/(2*right_s));
 res2+=dist;
 res1=res2;
 diff-=(dist*2*right_s);

 dist=diff/right_s;
 res1+=dist;
 diff-=(dist*right_s);

 if (dist==0 && diff>0 && diff>=(1+k-right_s)) { res1++; diff=0; }

 dist=diff/right_s;
 res2+=dist;
 diff-=(dist*right_s);

 if (dist==0 && diff>0 && diff>=(1+k-right_s)) { res2++; diff=0; }
}

int main() {clock_t t1 = clock();IO
r(T);

 FOR(tt,0,T)
 {
  r(n);r(k);
  solve();
  
  cout << "Case #" << (tt+1) << ": " << res1 << " " << res2 << endl;
  cerr << "case " << (tt+1) << " " << 1.0 * (clock() - t1) / CLOCKS_PER_SEC << " ms" << endl;  
 }

 return 0;
}
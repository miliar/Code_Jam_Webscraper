#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef vector < int > vi;
typedef vector < ll > vll;
typedef vector < string > vs;
typedef vector < vll > matrix;
 
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
#define log(x) cout << #x << " = " << x << endl
#define log2(x,y) cout << #x << " = " << x << " " << #y << " = " << y << endl
#define log3(x,y,z) cout << #x << " = " << x << " " << #y << " = " << y << " " << #z << " = " << z << endl
#define log4(x,y,z,t) cout << #x << " = " << x << " " << #y << " = " << y << " " << #z << " = " << z << " " << #t << " = " << t << endl
#define log5(x,y,z,t,v) cout << #x << " = " << x << " " << #y << " = " << y << " " << #z << " = " << z << " " << #t << " = " << t << " " << #v << " = " << v << endl
#define MAXN 1010
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

string s;
int k;

void solve()
{
int res=0;
bool found=true;

 FOR(i,0,1+sz(s)-k)
 {
  if (s[i]=='-')
  {
   res++;
   FOR(j,0,k)
   {
    if (s[i+j]=='-') s[i+j]='+';
    else s[i+j]='-';
   }
  }
 }

 FOR(i,0,sz(s)) if (s[i]=='-') { found=false; break; }
 if (found) wl(res);
 else wl("IMPOSSIBLE");
}

int main() {clock_t t1 = clock();IO
r(T);

 FOR(tt,0,T)
 {
  r(s);r(k);

  cout << "Case #" << (tt+1) << ": ";
  solve();

  cerr << "case " << (tt+1) << " " << 1.0 * (clock() - t1) / CLOCKS_PER_SEC << " ms" << endl;  
 }
 
 return 0;
}
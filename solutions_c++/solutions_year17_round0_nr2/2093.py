//bcw0x1bd2 {{{
#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;
#define FZ(x) memset((x),0,sizeof(x))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
#define SZ(x) ((int)((x).size()))
#define ALL(x) begin(x),end(x)
#define REP(i,x) for (int i=0; i<(x); i++)
#define REP1(i,a,b) for (int i=(a); i<=(b); i++)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef long double ld;

#ifdef DARKHH
#define FILEIO(name)
#else
#define FILEIO(name) \
  freopen(name".in", "r", stdin); \
  freopen(name".out", "w", stdout);
#endif

#ifdef DARKHH
template<typename T>
void _dump( const char* s, T&& head ) { cerr<<s<<"="<<head<<endl; }

template<typename T, typename... Args>
void _dump( const char* s, T&& head, Args&&... tail ) {
  int c=0;
  while ( *s!=',' || c!=0 ) {
    if ( *s=='(' || *s=='[' || *s=='{' ) c++;
    if ( *s==')' || *s==']' || *s=='}' ) c--;
    cerr<<*s++;
  }
  cerr<<"="<<head<<", ";
  _dump(s+1,tail...);
}

#define dump(...) do { \
  fprintf(stderr, "%s:%d - ", __PRETTY_FUNCTION__, __LINE__); \
  _dump(#__VA_ARGS__, __VA_ARGS__); \
} while (0)

template<typename Iter>
ostream& _out( ostream &s, Iter b, Iter e ) {
  s<<"[";
  for ( auto it=b; it!=e; it++ ) s<<(it==b?"":" ")<<*it;
  s<<"]";
  return s;
}

template<typename A, typename B>
ostream& operator <<( ostream &s, const pair<A,B> &p ) { return s<<"("<<p.first<<","<<p.second<<")"; }
template<typename T>
ostream& operator <<( ostream &s, const vector<T> &c ) { return _out(s,ALL(c)); }
template<typename T, size_t N>
ostream& operator <<( ostream &s, const array<T,N> &c ) { return _out(s,ALL(c)); }
template<typename T>
ostream& operator <<( ostream &s, const set<T> &c ) { return _out(s,ALL(c)); }
template<typename A, typename B>
ostream& operator <<( ostream &s, const map<A,B> &c ) { return _out(s,ALL(c)); }
#else
#define dump(...)
#endif
// }}}
// Let's Fight! ~OAO~~

const int S = 20;

int ip[S],dp[S][10][2];

int go(int pos, int lst, int any) {
  if (pos < 0) return 1;
  int &res =dp[pos][lst][any];
  if (res != -1) return res;
  res = 0;
  REP1(i,lst,9) {
    if (!any and i > ip[pos]) break;
    if (go(pos-1, i, any || (i < ip[pos]))) {
      return res = 1;
    }
  }
  return res;
}
ll solve(ll x) {
  ll y = x;
  REP(i,S) {
    ip[i] = y % 10;
    y /= 10;
  }
  memset(dp,-1,sizeof(dp));
  ll res = 0;

  for (int i=S-1,lst=0,any=0; i>=0; i--) {
    for (int j=9; j>=lst; j--) {
      if (!any and j > ip[i]) continue;
      if (go(i-1, j, any || (j < ip[i]))) {
        res = res * 10 + j;
        lst = j;
        any |= j < ip[i];
        break;
      }
    }
  }
  return res;
}
int main() {
  IOS;
  int nT;
  cin>>nT;
  REP1(cas,1,nT) {
    ll n;
    cin>>n;
    ll res = solve(n);
    cout<<"Case #"<<cas<<": "<<res<<endl;
  }

  return 0;
}


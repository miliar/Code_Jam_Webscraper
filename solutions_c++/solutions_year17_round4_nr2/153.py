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

const int MAXN = 1024;

int N,C,M,cnt[MAXN];
pii ip[MAXN];

void input() {
  cin>>N>>C>>M;
  REP(i,M) {
    cin>>ip[i].F>>ip[i].S;
    ip[i].F--;
    ip[i].S--;
  }
}
bool check(int k) {
  int p = 0;
  int c = 0;
  REP(i,M) {
    if (p > ip[i].F) return false;
    if (p >= N) return false;
    c++;
    if (c == k) {
      c = 0;
      p++;
    }
  }
  
  return true;
}
void solve(int cas) {
  memset(cnt,0,sizeof(cnt));
  sort(ip,ip+M);
  REP(i,M) {
    cnt[ip[i].S]++;
  }
  int l = 0, r = M;
  REP(i,MAXN) {
    l = max(l, cnt[i]);
  }
  while (l < r) {
    int m = (l + r) / 2;
    if (check(m)) r = m;
    else l = m+1;
  }
  int K = l;
  memset(cnt,0,sizeof(cnt));
  REP(i,M) cnt[ip[i].F]++;
  int Z = 0;
  REP(i,N) {
    if (cnt[i] > K) Z += cnt[i] - K;
  }
  cout<<"Case #"<<cas<<": "<<K<<" "<<Z<<endl;
}
int main() {
  IOS;
  int nT;
  cin>>nT;
  REP1(cas,1,nT) {
    input();
    solve(cas);
  }

  return 0;
}


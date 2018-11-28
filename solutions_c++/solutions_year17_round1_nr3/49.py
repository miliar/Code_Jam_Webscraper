//a34021501 {{{
#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;
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

#ifdef HAO123
#define FILEIO(name)
#else
#define FILEIO(name) \
  freopen(name".in", "r", stdin); \
  freopen(name".out", "w", stdout);
#endif

#ifdef HAO123
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
// Let's Fight! !111111111!

const int MAXN = 105;

using State = array<int, 4>;

int Hd, Ad, Hk, Ak, B, D;

int calc()
{
  map<State, int> mp;

  State st = {Hd, Ad, Hk, Ak};
  mp[st] = 0;

  queue<State> q;
  q.push(st);

  int cnt = 0;
  while(!q.empty() and cnt < 20000000)
  {
    cnt++;
    State s = q.front();
    q.pop();

    int d = mp[s];

    if(s[2] <= 0) return d;
    if(s[0] <= 0) continue;

    State ns;
    ns = {Hd, s[1], s[2], s[3]};
    ns[0] -= ns[3];
    if(!mp.count(ns))
    {
      mp[ns] = d + 1;
      q.push(ns);
    }
    ns = {s[0], s[1], max(0, s[2]-s[1]), s[3]};
    ns[0] -= ns[3];
    if(!mp.count(ns))
    {
      mp[ns] = d + 1;
      q.push(ns);
    }
    ns = {s[0], s[1]+B, s[2], s[3]};
    ns[0] -= ns[3];
    if(!mp.count(ns))
    {
      mp[ns] = d + 1;
      q.push(ns);
    }
    ns = {s[0], s[1], s[2], max(0, s[3]-D)};
    ns[0] -= ns[3];
    if(!mp.count(ns))
    {
      mp[ns] = d + 1;
      q.push(ns);
    }
  }
  assert(cnt < 20000000);
  
  return -1;
}

int main() {
  IOS;

  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
    cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
    int ans = calc();
    cout<<"Case #"<<t<<": ";
    if(ans == -1) cout<<"IMPOSSIBLE";
    else cout<<ans;
    cout<<endl;
  }

  return 0;
}


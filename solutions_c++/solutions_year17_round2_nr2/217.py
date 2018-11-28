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

int N;
int ans[5555];
int mp[555];
int ip[6];
int cnt[6];

void input() {
  cin>>N;
  REP(i,6) {
    cin>>ip[i];
  }
}
string solve() {
  if (ip[4] + ip[1] == N and ip[4] == ip[1]) {
    string res;
    REP(i,N/2) res += "OB";
    return res;
  }
  if (ip[0] + ip[3] == N and ip[0] == ip[3]) {
    string res;
    REP(i,N/2) res += "GR";
    return res;
  }
  if (ip[2] + ip[5] == N and ip[2] == ip[5]) {
    string res;
    REP(i,N/2) res += "VY";
    return res;
  }
  if (ip[1] and ip[4] < ip[1]+1) return "IMPOSSIBLE";
  if (ip[3] and ip[0] < ip[3]+1) return "IMPOSSIBLE";
  if (ip[5] and ip[2] < ip[5]+1) return  "IMPOSSIBLE";

  mp['R'] = 1;
  mp['O'] = 5;
  mp['Y'] = 4;
  mp['G'] = 6;
  mp['B'] = 2;
  mp['V'] = 3;
  pair<int,string> arr[3];
  arr[0] = {ip[0]-ip[3],"R"};
  arr[1] = {ip[4]-ip[1],"B"};
  arr[2] = {ip[2]-ip[5],"Y"};

  sort(arr,arr+3);
  int rd = arr[0].F + arr[1].F + arr[2].F;

  //cout<<arr[0]<<endl;
  //cout<<arr[1]<<endl;
  //cout<<arr[2]<<endl;
  if (arr[2].F > arr[0].F + arr[1].F) return "IMPOSSIBLE";


  string res;
  res += arr[2].S;
  arr[2].F--;
  int prv = 2;
  REP(i,rd-1) {
    int j = 0;
    if (j == prv) j++;
    REP(k,3) if (k != prv and arr[j].F <= arr[k].F) j = k;
    res += arr[j].S;
    arr[j].F--;
    prv = j;
  }

  assert(SZ(res) == rd);
  REP(i,rd) assert(res[i] != res[(i+1)%rd]);

  string res2;
  int fst[3] = {0,0,0};
  for (auto c:res) {
    res2 += c;
    if (c == 'R' and !fst[0]) {
      REP(_,ip[3]) res2 += "GR";
      fst[0] = 1;
    }
    if (c == 'B' and !fst[1]) {
      REP(_,ip[1]) res2 += "OB";
      fst[1] = 1;
    }
    if (c == 'Y' and !fst[2]) {
      REP(_,ip[5]) res2 += "VY";
      fst[2] = 1;
    }
  }

  assert(SZ(res2) == N);
  REP(i,N) {
    assert((mp[(int)res2[i]] & mp[(int)res2[(i+1)%N]]) == 0);
  }

  memset(cnt,0,sizeof(cnt));
  for (auto i:res2) {
    if (i == 'R') cnt[0]++;
    if (i == 'O') cnt[1]++;
    if (i == 'Y') cnt[2]++;
    if (i == 'G') cnt[3]++;
    if (i == 'B') cnt[4]++;
    if (i == 'V') cnt[5]++;
  }

  REP(i,6) assert(cnt[i] == ip[i]);

  return res2;
}
int main() {
  IOS;
  int nT;
  cin>>nT;
  REP1(cas,1,nT) {
    input();
    string res = solve();
    cout<<"Case #"<<cas<<": "<<res<<endl;
  }
  
  return 0;
}


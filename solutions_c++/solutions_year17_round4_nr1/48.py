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

int num[4];
int N, P;

int calc2()
{
  int arr[N];
  int cnt = 0;
  for(int i=0; i<P; i++)
    for(int j=0; j<num[i]; j++)
      arr[cnt++] = i;

  int ans = 0;
  do
  {
    int cur = 0, val = 0;
    for(int i=0; i<N; i++)
    {
      if(cur % P == 0) val++;
      cur += arr[i];
    }
    ans = max(ans, val);
  } while(next_permutation(arr, arr+N));

  return ans;
}

int calc()
{
  int A = num[0], B = num[1], C = num[2], D = num[3];
  int tot = 0;
  for(int i=0; i<P; i++)
    tot += i * num[i];
  tot %= P;
  int ans = 0;

  if(P == 2)
  {
    ans = A + (B/2);
  }
  else if(P == 3)
  {
    int m = min(B, C);
    int l = max(B, C) - m;
    ans = A + m + (l / 3);
  }
  else if(P == 4)
  {
    int m13 = min(B, D);
    int l13 = max(B, D) - m13;
    ans = A + m13;
    ans += C / 2;
    C %= 2;
    if(C>=1 and l13>=2)
    {
      C--;
      l13 -= 2;
      ans++;
    }
    ans += l13 / 4;
  }

  if(tot != 0) ans++;
  return ans;
}

int main() {
  IOS;

  int T;
  cin>>T;
    srand(time(0));
  for(int t=1; t<=T; t++)
  {
    cin>>N>>P;
    for(int i=0; i<P; i++)
      num[i] = 0;
    for(int i=0; i<N; i++)
    {
      int g;
      cin>>g;
      num[g%P]++;
    }

    //P = rand()%3 + 2;
    //N = rand() % 15;
    //for(int i=0; i<P; i++)
      //num[i] = 0;
    //for(int i=0; i<N; i++)
      //num[rand()%P]++;

    int ans = calc();
    //assert(ans == calc2());
    cout<<"Case #"<<t<<": "<<ans<<endl;
  }

  return 0;
}


#ifndef __clang__
#pragma GCC optimize "-O3"
#pragma GCC target "tune=native"
#endif
#ifdef ONLINE_JUDGE
#define NDEBUG 1
#endif
#include <stdio.h>
#include <bits/stdc++.h>

#define DESTRUCT2(p, a, b)                      \
  auto a = get<0>(p);                           \
  auto b = get<1>(p);

#define DESTRUCT3(p, a, b, c)                   \
  auto a = get<0>(p);                           \
  auto b = get<1>(p);                           \
  auto c = get<2>(p);

#define DESTRUCT4(p, a, b, c, d)                \
  auto a = get<0>(p);                           \
  auto b = get<1>(p);                           \
  auto c = get<2>(p);                           \
  auto d = get<3>(p);

#define FOR(i, n)     for(lli i = 0; i < (lli)(n); ++i)
#define FORU(i, j, k) for(lli i = (j); i <= (lli)(k); ++i)
#define FORD(i, j, k) for(lli i = (j); i >= (lli)(k); --i)

#define SQ(x) ((x)*(x))

#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back

using namespace std;

template<typename... As>
struct tpl : public std::tuple<As...> {
  using std::tuple<As...>::tuple;

  template<typename T = tuple<As...> >
  typename tuple_element<0, T>::type const&
  x() const { return get<0>(*this); }
  template<typename T = tuple<As...> >
  typename tuple_element<0, T>::type&
  x() { return get<0>(*this); }

  template<typename T = tuple<As...> >
  typename tuple_element<1, T>::type const&
  y() const { return get<1>(*this); }
  template<typename T = tuple<As...> >
  typename tuple_element<1, T>::type&
  y() { return get<1>(*this); }

  template<typename T = tuple<As...> >
  typename tuple_element<2, T>::type const&
  z() const { return get<2>(*this); }
  template<typename T = tuple<As...> >
  typename tuple_element<2, T>::type&
  z() { return get<2>(*this); }

  template<typename T = tuple<As...> >
  typename tuple_element<3, T>::type const&
  w() const { return get<3>(*this); }
  template<typename T = tuple<As...> >
  typename tuple_element<3, T>::type&
  w() { return get<3>(*this); }
};

using lli   = long long int;
using llu   = long long unsigned;

using pii   = tpl<lli, lli>;
using piii  = tpl<lli, lli, lli>;
using piiii = tpl<lli, lli, lli, lli>;
using vi    = vector<lli>;
using vii   = vector<pii>;
using viii  = vector<piii>;
using vvi   = vector<vi>;
using vvii  = vector<vii>;
using vviii = vector<viii>;

template<class T>
using min_queue = priority_queue<T, vector<T>, greater<T> >;
template<class T>
using max_queue = priority_queue<T>;

template<size_t... I>
struct my_index_sequence {
  using type = my_index_sequence;
  static constexpr array<size_t, sizeof...(I)> value = { {I...} };
};

namespace my_index_sequence_detail {
  template<typename I, typename J> struct concat;
  template<size_t... I, size_t... J>
  struct concat<my_index_sequence<I...>, my_index_sequence<J...> > :
    my_index_sequence<I..., (sizeof...(I)+J)...> { };
  template<size_t N> struct make_index_sequence :
    concat<typename make_index_sequence<N/2>::type, typename make_index_sequence<N-N/2>::type>::type { };
  template <> struct make_index_sequence<0> : my_index_sequence<>{};
  template <> struct make_index_sequence<1> : my_index_sequence<0>{};
}

template<class... A>
using my_index_sequence_for = typename my_index_sequence_detail::make_index_sequence<sizeof...(A)>::type;

template<class T, size_t... I>
void print_tuple(ostream& s, T const& a, my_index_sequence<I...>){
  using swallow = int[];
  (void)swallow{0, (void(s << (I == 0? "" : ", ") << get<I>(a)), 0)...};
}

template<class T>
ostream& print_collection(ostream& s, T const& a);
template<class... A>
ostream& operator<<(ostream& s, tpl<A...> const& a);
template<class... A>
ostream& operator<<(ostream& s, tuple<A...> const& a);
template<class A, class B>
ostream& operator<<(ostream& s, pair<A, B> const& a);

template<class T, size_t I>
ostream& operator<<(ostream& s, array<T, I> const& a) { return print_collection(s, a); }
template<class T>
ostream& operator<<(ostream& s, vector<T> const& a) { return print_collection(s, a); }
template<class T, class U>
ostream& operator<<(ostream& s, multimap<T, U> const& a) { return print_collection(s, a); }
template<class T>
ostream& operator<<(ostream& s, multiset<T> const& a) { return print_collection(s, a); }
template<class T, class U>
ostream& operator<<(ostream& s, map<T, U> const& a) { return print_collection(s, a); }
template<class T>
ostream& operator<<(ostream& s, set<T> const& a) { return print_collection(s, a); }

template<class T>
ostream& print_collection(ostream& s, T const& a){
  s << '[';
  for(auto it = begin(a); it != end(a); ++it){
    s << *it;
    if(it != prev(end(a))) s << " ";
  }
  return s << ']';
}

template<class... A>
ostream& operator<<(ostream& s, tpl<A...> const& a){
  s << '(';
  print_tuple(s, a, my_index_sequence_for<A...>{});
  return s << ')';
}

template<class... A>
ostream& operator<<(ostream& s, tuple<A...> const& a){
  s << '(';
  print_tuple(s, a, my_index_sequence_for<A...>{});
  return s << ')';
}

template<class A, class B>
ostream& operator<<(ostream& s, pair<A, B> const& a){
  return s << "(" << get<0>(a) << ", " << get<1>(a) << ")";
}

namespace std {
  namespace {
    template <class T>
    inline void hash_combine(size_t& seed, T const& v) {
      seed ^= hash<T>()(v) + 0x9e3779b9 + (seed<<6) + (seed>>2);
    }
    template <class Tuple, size_t Index = tuple_size<Tuple>::value - 1>
    struct HashValueImpl {
      static void apply(size_t& seed, Tuple const& tuple) {
        HashValueImpl<Tuple, Index-1>::apply(seed, tuple);
        hash_combine(seed, get<Index>(tuple));
      }
    };
    template <class Tuple>
    struct HashValueImpl<Tuple, 0> {
      static void apply(size_t& seed, Tuple const& tuple) {
        hash_combine(seed, get<0>(tuple));
      }
    };
  }
  template <typename ... TT>
  struct hash<tuple<TT...>> {
    size_t operator()(tuple<TT...> const& tt) const {
      size_t seed = 0;
      HashValueImpl<tuple<TT...> >::apply(seed, tt);
      return seed;
    }
  };
  template <typename ... TT>
  struct hash<tpl<TT...>> {
    size_t operator()(tpl<TT...> const& tt) const {
      size_t seed = 0;
      HashValueImpl<tuple<TT...> >::apply(seed, tt);
      return seed;
    }
  };
}

//------------------------------------------------------------------------------

const int dx[4]={-1,1,0,0};
const int dy[4]={0,0,-1,1};



struct pb {
  unordered_map<lli,lli> seen;
  int c,r,m;
  char A[100][100];
  lli TLINE[100][100];
  vii S;
  vii T;

  int date=10;
  int E[100][100];

  int ans=0;
  int to;

  void iter4(int i, int j, function<void(int,int)> f) {
    FOR(d,4) {
      int x=i+dx[d];
      int y=j+dy[d];
      if(x>=0&&y>=0&&x<r&&y<c) f(x,y);
    }
  }

  void read(){
    cin>>c>>r>>m;
    FOR(i,r) FOR(j,c) cin>>A[i][j];
    FOR(i,r) FOR(j,c) {
      if(A[i][j]=='S') S.pb(mt(i,j));
      if(A[i][j]=='T') { T.pb(mt(i,j)); calcline(T.size()-1, i,j); }
    }
    ans=T.size()+1;
  }

  void calcline(int t,int i,int j){
    FOR(d,4) {
      int x=i, y=j;
      do {
        TLINE[x][y] |= (1<<t);
        x+=dx[d]; y+=dy[d];
      } while(x>=0&&y>=0&&x<r&&y<c&&A[x][y] != '#');
    }
  }

  void dfs(lli bsS, lli bsT, lli from) {
    int cur=__builtin_popcount(bsT);
    if(cur<ans){
      ans=cur;
      to=1024*bsS + bsT;
    }
    if(seen.count(1024*bsS + bsT)) return;
    seen[1024*bsS + bsT]=from;
    FOR(i,S.size()) if(bsS&(1<<i)) {
      date++;
      lli killable = 0;
      vector<pii> A0,B; A0.pb(S[i]);
      FOR(nm,m+1) {
        if(A0.empty()) break;
        B.clear();
        for(auto p:A0) {
          if(TLINE[p.x()][p.y()]&bsT) {
            killable |= TLINE[p.x()][p.y()]&bsT;
          }else{
            iter4(p.x(),p.y(),[&](int i, int j){
                if(E[i][j]==date) return;
                if(A[i][j]=='#') return;
                //if(TLINE[i][j]&bsT) { killable |= TLINE[i][j]&bsT; return;}
                E[i][j]=date;
                B.pb(mt(i,j));
              });
          }
        }
        swap(B,A0);
      }
      //cout << i << ": " << bitset<10>(killable) << endl;
      FOR(j,T.size()) if(killable&(1<<j)) {
        dfs(bsS^(1<<i),bsT^(1<<j),1024*bsS+bsT);
      }
    }
  }

  void solve(){
    dfs((1<<S.size())-1,(1<<T.size())-1,-1);
    cout << T.size()-ans << endl;
    vii AA;
    while(seen[to] != -1) {
      lli bsS = to/1024;
      lli bsT = to&1023;
      to=seen[to];
      lli bsS1 = to/1024;
      lli bsT1 = to&1023;
      int i,j;
      FOR(a,10) if((bsS1&(1<<a))&&!((bsS&(1<<a)))) i=a;
      FOR(a,10) if((bsT1&(1<<a))&&!((bsT&(1<<a)))) j=a;
      AA.pb(mt(i,j));
    }
    reverse(all(AA));
    for(auto p : AA) cout << p.x()+1 << ' ' << p.y()+1 << endl;
  }
};

int main(){
  ios::sync_with_stdio(0); cin.tie(0);
  int nt; cin>>nt;
  vector<pb> pbs(nt);
  FOR(t,nt) pbs[t].read();
  FOR(t,nt) {
    cout << "Case #" << 1+t << ": ";
    pbs[t].solve();
  }
  return 0;
}

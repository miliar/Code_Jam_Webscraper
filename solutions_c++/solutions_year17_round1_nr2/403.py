#include <iostream>
#include <vector>
#include <cstdio>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>
#include <functional>
#include <set>
#include <ctime>
#include <random>
#include <chrono>
#include <cassert>
#include <tuple>
#include <utility>
using namespace std;

namespace {
  using Integer = long long; //__int128;
  template<class T, class S> istream& operator >> (istream& is, pair<T,S>& p){return is >> p.first >> p.second;}
  template<class T> istream& operator >> (istream& is, vector<T>& vec){for(T& val: vec) is >> val; return is;}
  template<class T> istream& operator ,  (istream& is, T& val){ return is >> val;}
  template<class T, class S> ostream& operator << (ostream& os, const pair<T,S>& p){return os << p.first << " " << p.second;}
  template<class T> ostream& operator << (ostream& os, const vector<T>& vec){for(size_t i=0; i<vec.size(); i++) os << vec[i] << (i==vec.size()-1?"":" "); return os;}
  template<class T> ostream& operator ,  (ostream& os, const T& val){ return os << " " << val;}

  template<class H> void print(const H& head){ cout << head; }
  template<class H, class ... T> void print(const H& head, const T& ... tail){ cout << head << " "; print(tail...); }
  template<class ... T> void println(const T& ... values){ print(values...); cout << endl; }

  template<class H> void eprint(const H& head){ cerr << head; }
  template<class H, class ... T> void eprint(const H& head, const T& ... tail){ cerr << head << " "; eprint(tail...); }
  template<class ... T> void eprintln(const T& ... values){ eprint(values...); cerr << endl; }

  class range{ Integer start_, end_, step_; public: struct range_iterator{ Integer val, step_; range_iterator(Integer v, Integer step) : val(v), step_(step) {} Integer operator * (){return val;} void operator ++ (){val += step_;} bool operator != (range_iterator& x){return step_ > 0 ? val < x.val : val > x.val;} }; range(Integer len) : start_(0), end_(len), step_(1) {} range(Integer start, Integer end) : start_(start), end_(end), step_(1) {} range(Integer start, Integer end, Integer step) : start_(start), end_(end), step_(step) {} range_iterator begin(){ return range_iterator(start_, step_); } range_iterator   end(){ return range_iterator(  end_, step_); } };

  inline string operator "" _s (const char* str, size_t size){ return move(string(str)); }
  constexpr Integer my_pow(Integer x, Integer k, Integer z=1){return k==0 ? z : k==1 ? z*x : (k&1) ? my_pow(x*x,k>>1,z*x) : my_pow(x*x,k>>1,z);}
  constexpr Integer my_pow_mod(Integer x, Integer k, Integer M, Integer z=1){return k==0 ? z%M : k==1 ? z*x%M : (k&1) ? my_pow_mod(x*x%M,k>>1,M,z*x%M) : my_pow_mod(x*x%M,k>>1,M,z);}
  constexpr unsigned long long operator "" _ten (unsigned long long value){ return my_pow(10,value); }

  inline int k_bit(Integer x, int k){return (x>>k)&1;} //0-indexed

  mt19937 mt(chrono::duration_cast<chrono::nanoseconds>(chrono::steady_clock::now().time_since_epoch()).count());

  template<class T> string join(const vector<T>& v, const string& sep){ stringstream ss; for(size_t i=0; i<v.size(); i++){ if(i>0) ss << sep; ss << v[i]; } return ss.str(); }

  inline string operator * (string s, int k){ string ret; while(k){ if(k&1) ret += s; s += s; k >>= 1; } return ret; }
}
constexpr long long mod = 9_ten + 7;

int solve(){
  int n,p;
  cin >> n,p;
  vector<long long> r(n);
  cin >> r;
  vector<vector<long long>> q(n, vector<long long>(p));
  cin >> q;

  vector< priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> > pk_begin(n);
  vector< priority_queue<int, vector<int>, greater<int>> > pk_end(n);

  set<int> kk;

  for(int i=0; i<n; i++){
    for(int j=0; j<p; j++){

      long long lb = -1;
      long long ub = 1e6 + 10;
      while(ub-lb>1){
        long long mid = (lb+ub)/2;
        bool ok = 10*q[i][j] <= r[i] * 11 * mid ;
        (ok? ub : lb) = mid;
      }

      int k_min = ub;

      lb = -1;
      ub = 1e6+10;
      while(ub-lb>1){
        long long mid = (lb+ub)/2;
        bool ok = 10*q[i][j] >= r[i] * 9 * mid;
        (ok ? lb : ub) = mid;
      }

      int k_max = lb;

      if( k_min > k_max || k_max <= 0 || k_min > 1e6){
      }else{
        pk_begin[i].push( {k_min, k_max} );

        kk.insert(k_min);
        kk.insert(k_max);
      }

    }
  }

  int ans = 0;
  for(int k : kk){
    vector<int> cnt(n, 0);

    for(int i=0; i<n; i++){
      while( pk_end[i].size() && pk_end[i].top() < k ){
        pk_end[i].pop();
      }
      while( pk_begin[i].size() && pk_begin[i].top().first == k){
        pk_end[i].push( pk_begin[i].top().second );
        pk_begin[i].pop();
      }

      cnt[i] = pk_end[i].size();
    }

    int d = *min_element(cnt.begin(), cnt.end());
    if(d <= 0) continue;

    ans += d;
    for(int i=0; i<n; i++){
      for(int j=0; j<d; j++) pk_end[i].pop();
    }
  }

  return ans;
}


int main(){
  int t;
  cin >> t;
  for(int i : range(t) ){
    auto ans = solve();
    printf("Case #%d: ", i+1);
    cout << ans << endl;
  }

  return 0;
}

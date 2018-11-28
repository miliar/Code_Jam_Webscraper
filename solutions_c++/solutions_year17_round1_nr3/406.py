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
  int hd,ad, hk,ak, b,d;
  cin >> hd,ad, hk,ak, b,d;

  vector<int> dp(101*101*101, 0);
  dp[ad*101*101 + hk*101 + ak] = hd;

  for(int t=1; t<=220; t++){
    vector<int> dp_(101*101*101, 0);

    for(auto a : range(1,101) ){
      for(auto h : range(1,101) ){
        for(auto aa : range(0,101) ){
          int p = a*101*101 + h*101 + aa;

          if( dp[p] <= 0 ) continue;

          { // atack
            int a_ = a;
            int h_ = h - a;
            int aa_ = aa;

            if( h_ <= 0 ){
              return t;
            }
            int hh = dp[p] - aa_;

            if( hh>0 ){
              dp_[a_*101*101 + h_*101 + aa_] = max(dp_[a_*101*101 + h_*101 + aa_], hh);
            }
          }

          { // buff
            int a_ = a + b;
            int h_ = h;
            int aa_ = aa;

            if( h_ <= 0 ){
              return t;
            }
            int hh = dp[p] - aa_;

            if( hh>0 ){
              dp_[a_*101*101 + h_*101 + aa_] = max(dp_[a_*101*101 + h_*101 + aa_], hh);
            }
          }

          { // debuff
            int a_ = a;
            int h_ = h;
            int aa_ = max<int>(0, aa - d);

            if( h_ <= 0 ){
              return t;
            }
            int hh = dp[p] - aa_;

            if( hh>0 ){
              dp_[a_*101*101 + h_*101 + aa_] = max(dp_[a_*101*101 + h_*101 + aa_], hh);
            }
          }

          { // cure
            int a_ = a;
            int h_ = h;
            int aa_ = aa;

            if( h_ <= 0 ){
              return t;
            }
            int hh = hd - aa_;

            if( hh>0 ){
              dp_[a_*101*101 + h_*101 + aa_] = max(dp_[a_*101*101 + h_*101 + aa_], hh);
            }
          }

          
        }
      }
    }

    swap(dp, dp_);
  }

  return -1;
}


int main(){
  int t;
  cin >> t;
  for(int i : range(t) ){
    auto ans = solve();
    printf("Case #%d: ", i+1);
    if(ans == -1) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }

  return 0;
}

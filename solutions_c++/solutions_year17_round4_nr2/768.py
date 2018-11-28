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

template<class T>
class Min_Cost_Flow{
public:

  struct edge{
    int to;
    int cap;
    T cost;
    int rev;
  };

  const T INF;
  vector<vector<edge>> G;

  Min_Cost_Flow(int n, T inf) : G(n), INF(inf){

  }

  void add_edge(int from, int to, int cap, T cost){
    G[from].push_back((edge){to, cap, cost, (int)G[to].size()});
    G[to].push_back((edge){from, 0, -cost, (int)G[from].size()-1});
  }


  //min cost : s->t (flow:f)
  T min_cost_flow(int s, int t, int f){
    const int N = G.size();
    T cost = 0;
    vector<int> prev_v(N,-1);
    vector<int> prev_e(N,-1);
    vector<T> potantial(N, 0);

    
    while(f>0){
      //min distance(cost based) search with SPFA
      vector<T> dist(N, INF);
      
      vector<int> cnt(dist.size(), 0);
      dist[s] = 0;
      prev_v[s] = s;

      queue<int> Q;
      auto my_push = [&](int node){
        Q.push(node);
        cnt[node]++;
      };
      auto my_pop = [&]() -> int{
        int ret = Q.front();
        cnt[ret]--;
        Q.pop();
        return ret;
      };
      my_push(s);
      while(!Q.empty()){
        int pos = my_pop();
        for(int i=0; i<G[pos].size(); i++){
          edge& E = G[pos][i];
          T new_dist = dist[pos] + E.cost + potantial[E.to] - potantial[pos];
          if(dist[E.to] > new_dist && E.cap > 0){
            dist[E.to] = new_dist;
            prev_v[ E.to ] = pos;
            prev_e[ E.to ] = i;

            if(cnt[ E.to ] == 0){
              my_push( E.to );
            }
          }
        }
      }
      for(int i=0; i<N; i++){
        dist[i] = potantial[i] + dist[i];
      }

      //cannot achieved to "t" return -1
      if(dist[t]>=INF) return -1;

      //add cost of s->t with flow=d
      int pos=t;
      int d=f;
      while(pos!=s){
        int i=prev_v[pos];
        int j=prev_e[pos];
        pos = i;
        d = min(d, G[i][j].cap);
      }
      
      pos = t;
      //cout << t ;
      while(pos!=s){
        int i=prev_v[pos];
        int j=prev_e[pos];
        G[i][j].cap -= d;
        G[ G[i][j].to ][ G[i][j].rev ].cap += d;
        //cost += G[i][j].cost * d;
        pos = i;
        //cout << " <- " << pos;
      }
      //cout << endl;
      cost += d * dist[t];
      f -= d;

      //f==0 then end
    }
    return cost;
  }
};


pair<int,int> solve(){
  int n,m,c;
  cin >> n,c,m;

  if( c > 2 ) abort();

  vector<vector<int>> t(2);
  for(int i=0; i<m; i++){
    int p,b;
    cin >> p,b;
    p--; b--;
    t[b].push_back(p);
  }

  sort(t[0].rbegin(), t[0].rend());
  sort(t[1].rbegin(), t[1].rend());

  Min_Cost_Flow<int> f(t[0].size() + t[1].size() + 2, 1e6);
  int source = t[0].size() + t[1].size() + 0;
  int sink = t[0].size() + t[1].size() + 1;
  for(int j=0; j<t[1].size(); j++){
    f.add_edge(t[0].size()+j, sink, 1, 0);
  }
  for(int i=0; i<t[0].size(); i++){
    f.add_edge(source, i, 1, 0);
    for(int j=0; j<t[1].size(); j++){
      if( t[0][i] != t[1][j] ){
        f.add_edge(i, t[0].size()+j, 1, 0);
      }else{
        if( t[0][i] != 0 ){
          f.add_edge(i, t[0].size()+j, 1, 1);
        }
      }
    }
  }

  int match = 0;
  int cost = 0;
  while(true){
    int ff = f.min_cost_flow(source, sink, 1);
    if( ff == -1 ){
      break;
    }else{
      match++;
      cost += ff;
    }
  }

  int ans = m - match;

  return pair<int,int>{ans, cost};
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

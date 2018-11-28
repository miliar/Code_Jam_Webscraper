#include <bits/stdc++.h>
#include <sys/time.h>
#include <unistd.h>
using namespace std;
#define i64         int64_t
#define rep(i, n)   for(i64 i = 0; i < ((i64)(n)); ++i)
#define sz(v)       ((i64)((v).size()))
#define bit(n)      (((i64)1)<<((i64)(n)))
#define all(v)      (v).begin(), (v).end()

std::string dbgDelimiter(int &i){ return (i++ == 0 ? "" : ", "); }
#define dbgEmbrace(exp) { int i = 0; os << "{"; { exp; } os << "}"; return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::vector<T> v);
template <class T> std::ostream& operator<<(std::ostream &os, std::set<T> v);
template <class T> std::ostream& operator<<(std::ostream &os, std::queue<T> q);
template <class T> std::ostream& operator<<(std::ostream &os, std::priority_queue<T> q);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::pair<T, K> p);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::map<T, K> mp);
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::unordered_map<T, K> mp);
template <int INDEX, class TUPLE> void dbgDeploy(std::ostream &os, TUPLE tuple){}
template <int INDEX, class TUPLE, class H, class ...Ts> void dbgDeploy(std::ostream &os, TUPLE t){ os << (INDEX == 0 ? "" : ", ") << get<INDEX>(t); dbgDeploy<INDEX + 1, TUPLE, Ts...>(os, t); }
template <class T, class K> void dbgDeploy(std::ostream &os, std::pair<T, K> p, std::string delim){ os << "(" << p.first << delim << p.second << ")"; }
template <class ...Ts> std::ostream& operator<<(std::ostream &os, std::tuple<Ts...> t){ os << "("; dbgDeploy<0, std::tuple<Ts...>, Ts...>(os, t); os << ")"; return os; }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::pair<T, K> p){ dbgDeploy(os, p, ", "); return os; }
template <class T> std::ostream& operator<<(std::ostream &os, std::vector<T> v){ dbgEmbrace( for(T t: v){ os << dbgDelimiter(i) << t; }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::set<T> s){ dbgEmbrace( for(T t: s){ os << dbgDelimiter(i) << t; }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::queue<T> q){ dbgEmbrace( for(; q.size(); q.pop()){ os << dbgDelimiter(i) << q.front(); }); }
template <class T> std::ostream& operator<<(std::ostream &os, std::priority_queue<T> q){ dbgEmbrace( for(; q.size(); q.pop()){ os << dbgDelimiter(i) << (T) q.top();   }); }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::map<T, K> mp){ dbgEmbrace( for(auto p: mp){ os << dbgDelimiter(i); dbgDeploy(os, p, "->"); }); }
template <class T, class K> std::ostream& operator<<(std::ostream &os, std::unordered_map<T, K> mp){ dbgEmbrace( for(auto p: mp){ os << dbgDelimiter(i); dbgDeploy(os, p, "->"); }); }
#define DBG_OUT std::cerr
#define DBG_OVERLOAD(_1, _2, _3, _4, _5, _6, macro_name, ...) macro_name
#define DBG_LINE() { char s[99]; sprintf(s, "line:%3d | ", __LINE__); DBG_OUT << s; }
#define DBG_OUTPUT(v) { DBG_OUT << (#v) << "=" << (v); }
#define DBG1(v, ...) { DBG_OUTPUT(v); }
#define DBG2(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG1(__VA_ARGS__); }
#define DBG3(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG2(__VA_ARGS__); }
#define DBG4(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG3(__VA_ARGS__); }
#define DBG5(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG4(__VA_ARGS__); }
#define DBG6(v, ...) { DBG_OUTPUT(v); DBG_OUT << ", "; DBG5(__VA_ARGS__); }

#define DEBUG0() { DBG_LINE(); DBG_OUT << std::endl; }
#define DEBUG(...)                                                      \
  {                                                                     \
    DBG_LINE();                                                         \
    DBG_OVERLOAD(__VA_ARGS__, DBG6, DBG5, DBG4, DBG3, DBG2, DBG1)(__VA_ARGS__); \
    DBG_OUT << std::endl;                                               \
  }















i64 f(i64 a, i64 b)
{
  return a / b + (a % b ? 1 : 0);
}



i64 calcAttack(i64 h, i64 a, i64 up)
{
  i64 bef = bit(50);
  for(i64 i = 0; true; ++i){
    i64 cur = f(h, i * up + a) + i;
    if(bef < cur) return bef;
    bef = cur;
  }
}

i64 g(i64 max_h, i64 h, i64 a, i64 needed)
{
  if(a == 0) return 0;

  i64 bonus = (h - 1) / a;
  needed = needed - bonus;
  if(needed <= 1) return 0;

  i64 t = f(max_h, a) - 2;
  if(t <= 0) return bit(50);
  // DEBUG(needed, t);
  return 1 + (needed - 2) / t;
}


i64 def_ans;
void calcDefence(i64 max_h, i64 h, i64 a, i64 down, i64 needed, i64 cur)
{
  a = max((i64) 0, a);
  // DEBUG(max_h, h, a, down, needed, cur);
  if(def_ans <= cur) return;
  if(h <= 0) return;
  // DEBUG(g(max_h, h, a, needed), cur);
  def_ans = min(def_ans, g(max_h, h, a, needed) + cur);
  calcDefence(max_h, h - (a - down), a - down, down, needed, cur + 1);
  if(h - (a - down) <= 0){
    calcDefence(max_h, max_h - a, a, down, needed, cur + 1);
  }
}

int main()
{
  i64 test_n;
  cin >> test_n;
  rep(test_case, test_n){
    i64 h0, a0, h1, a1, b, d;
    cin >> h0 >> a0 >> h1 >> a1 >> b >> d;
    i64 needed = calcAttack(h1, a0, b);
    // DEBUG0();
    def_ans = 10000;
    calcDefence(h0, h0, a1, d, needed, 0);
    if(def_ans == 10000){
      cout << "Case #" << test_case + 1 << ": IMPOSSIBLE" << endl;
    }else{
      cout << "Case #" << test_case + 1 << ": " << def_ans + needed << endl;
    }
  }
}


























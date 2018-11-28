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

















class StronglyConnectedComponents
{
public:
  int getGroupId(int vertex);
  void update();
  void addEdge(int source, int target);

  StronglyConnectedComponents(int size);
private:
  void updateDfsForward(int vertex, std::vector<int>& q);
  void updateDfsBackward(int vertex, int id);

  vector<int> group_id;
  vector<vector<int>> reversed_edges;
  vector<vector<int>> edges;

  static const int INITIAL_ID;
  static const int NO_ID;
};
const int StronglyConnectedComponents::INITIAL_ID = -1;
const int StronglyConnectedComponents::NO_ID = -2;

inline int StronglyConnectedComponents::getGroupId(int vertex)
{
  return group_id[vertex];
}

void StronglyConnectedComponents::updateDfsForward(int vertex, std::vector<int>& q)
{
  group_id[vertex] = NO_ID;
  for(auto e: edges[vertex])if(group_id[e] == INITIAL_ID) updateDfsForward(e, q);
  q.push_back(vertex);
}

void StronglyConnectedComponents::updateDfsBackward(int vertex, int id)
{
  group_id[vertex] = id;
  for(auto e: reversed_edges[vertex])if(group_id[e] == NO_ID) updateDfsBackward(e, id);
}

void StronglyConnectedComponents::update()
{
  for(int v = 0; v < edges.size(); ++v) group_id[v] = INITIAL_ID;

  std::vector<int> q;
  for(int v = 0; v < edges.size(); ++v)if(group_id[v] == INITIAL_ID) updateDfsForward(v, q);

  std::reverse(q.begin(), q.end());
  for(auto v: q)if(group_id[v] == NO_ID) updateDfsBackward(v, v);
}

void StronglyConnectedComponents::addEdge(int source, int target)
{
  edges[source].push_back(target);
  reversed_edges[target].push_back(source);
}

StronglyConnectedComponents::StronglyConnectedComponents(int size)
{
  group_id = vector<int>(size);
  edges = vector<vector<int>>(size);
  reversed_edges = vector<vector<int>>(size);
}












const i64 dxs[] = {1, 0, -1, 0};
const i64 dys[] = {0, 1, 0, -1};
i64 n, m;
vector<string> mp;
i64 getIndex(i64 x, i64 y, i64 dir)
{
  return (x * m + y) * 2 + (dir % 2);
}

vector<vector<vector<i64>>> search_beam_memo;
i64 searchBeam(i64 x, i64 y, i64 dir)
{
  if(x < 0 || n <= x) return -1;
  if(y < 0 || m <= y) return -1;
  i64 &res = search_beam_memo[x][y][dir];
  if(res == -100) return -1;
  if(res != -2) return res;
  res = -100;

  if(mp[x][y] == '/' || mp[x][y] == '\\' || mp[x][y] == '.') {
    i64 next_dir = dir;
    if(mp[x][y] == '/') {
      const i64 next_dirs[] = {3, 2, 1, 0};
      next_dir = next_dirs[dir];
    }else if(mp[x][y] == '\\'){
      const i64 next_dirs[] = {1, 0, 3, 2};
      next_dir = next_dirs[dir];
    }
    i64 nx = x + dxs[next_dir];
    i64 ny = y + dys[next_dir];
    return res = searchBeam(nx, ny, next_dir);
  }else if(mp[x][y] == '-' || mp[x][y] == '|'){
    return res = getIndex(x, y, dir);
  }else if(mp[x][y] == '#'){
    return res = -1;
  }else{
    DEBUG0();
    return 1 / 0;
  }
}


bool run(vector<string> arg0, vector<vector<i64>> force)
{
  mp = arg0;
  n = sz(mp);
  m = sz(mp[0]);
  search_beam_memo = vector<vector<vector<i64>>>(n, vector<vector<i64>>(m, vector<i64>(4, -2)));
  StronglyConnectedComponents graph(n * m * 2);
  rep(x, n)rep(y, m)if(force[x][y] != -1) graph.addEdge(getIndex(x, y, force[x][y]), getIndex(x, y, 1 - force[x][y]));
  rep(x, n)rep(y, m) {
      if (mp[x][y] == '.') {
        vector<i64> beams;
        rep(i, 2) {
          i64 beam0 = searchBeam(x, y, i == 0 ? 0 : 1);
          i64 beam1 = searchBeam(x, y, i == 0 ? 2 : 3);
          // DEBUG(x, y, i, beam0, beam1);
          if (beam0 != -1 && beam1 != -1) {
            graph.addEdge(beam0, beam0 ^ 1);
            graph.addEdge(beam1, beam1 ^ 1);
            continue;
          }
          if (beam0 != -1) beams.push_back(beam0);
          if (beam1 != -1) beams.push_back(beam1);
        }
        // DEBUG(x, y, sz(beams));
        if (sz(beams) == 0) return false;
        if (sz(beams) == 1) {
          graph.addEdge(beams[0] ^ 1, beams[0]);
        } else if (sz(beams) == 2) {
          graph.addEdge(beams[1] ^ 1, beams[0]);
          graph.addEdge(beams[0] ^ 1, beams[1]);
        } else {
          DEBUG0();
          return 1 / 0;
        }
      }
      if (mp[x][y] == '-' || mp[x][y] == '|') {
        rep(i, 2){
          i64 dir0 = i == 0 ? 0 : 1;
          i64 dir1 = i == 0 ? 2 : 3;
          i64 beam0 = searchBeam(x + dxs[dir0], y + dys[dir0], dir0);
          i64 beam1 = searchBeam(x + dxs[dir1], y + dys[dir1], dir1);
          if(beam0 != -1) graph.addEdge(getIndex(x, y, i), getIndex(x, y, i) ^ 1);
          if(beam1 != -1) graph.addEdge(getIndex(x, y, i), getIndex(x, y, i) ^ 1);
        }
      }
    }
  graph.update();
  rep(x, n)rep(y, m){
      if(graph.getGroupId(getIndex(x, y, 0)) == graph.getGroupId(getIndex(x, y, 1))){
        return false;
      }
    }
  return true;
}

bool run(vector<string> arg0)
{
  vector<vector<i64>> force(sz(arg0), vector<i64>(sz(arg0[0]), -1));
  return run(arg0, force);
}

void debug()
{
  vector<string> mp0({
                         "/..-",
                         ".###",
                     });
  DEBUG(1 == run(mp0));
  vector<string> mp1({
                         "/..-",
                         ".#.#",
                     });
  DEBUG(0 == run(mp1));
  vector<string> mp2({
                         "/.--",
                         ".###",
                     });
  DEBUG(0 == run(mp2));
  vector<string> mp3({
                         "./.-",
                         "\\/##",
                     });
  DEBUG(1 == run(mp3));
  vector<string> mp4({
                         "./.-",
                         "./##",
                     });
  DEBUG(0 == run(mp4));
  vector<string> mp5({
                         "/\\",
                         ".|",
                         "\\/"
                     });
  DEBUG(1 == run(mp5));
  vector<string> mp6({
                         "/.",
                         "..",
                         ".|",
                         "\\/"
                     });
  DEBUG(1 == run(mp6));
  vector<string> mp7({
                         "/\\",
                         "..",
                         ".|",
                         "\\/"
                     });
  DEBUG(0 == run(mp7));
  vector<string> mp8({
                         ".-",
                         "|.",
                     });
  DEBUG(1 == run(mp8));
  vector<string> mp9({
                         ".-",
                         "#.",
                     });
  DEBUG(0 == run(mp9));
  vector<string> mp10({
                         "./-",
                         "...",
                         "-/.",
                     });
  DEBUG(0 == run(mp10));
  vector<string> mp11({
                          "--",
                          "--"
                      });
  DEBUG(0 == run(mp11));
  vector<string> mp12({
                          "--",
                          "\\/"
                      });
  DEBUG(0 == run(mp12));
  vector<string> mp13({
                          "./-",
                          "./.",
                          "-/.",
                      });
  DEBUG(1 == run(mp13));
}


int main()
{
  if(!true){
    debug();
  }

  i64 test_case_n;
  cin >> test_case_n;
  rep(test_case_i, test_case_n){
    i64 n, m;
    cin >> n >> m;
    vector<string> mp(n);
    rep(i, n) cin >> mp[i];
    if(!run(mp)){
      cout << "Case #" << test_case_i + 1 << ": IMPOSSIBLE" << endl;
      continue;
    }
    cout << "Case #" << test_case_i + 1 << ": POSSIBLE" << endl;
    vector<vector<i64>> force(n, vector<i64>(m, -1));
    rep(x, n)rep(y, m){
        if(mp[x][y] != '-' && mp[x][y] != '|') continue;
        force[x][y] = 0;
        force[x][y] = (run(mp, force)) ? 0 : 1;
        // DEBUG(x, y, run(mp, force));
      }
    rep(x, n)rep(y, m)if(force[x][y] != -1) mp[x][y] = force[x][y] == 1 ? '|' : '-';
    rep(x, n) cout << mp[x] << endl;
  }
}








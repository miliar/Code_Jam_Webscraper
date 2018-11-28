#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <cassert>
#include <cstring>
#include <cstddef>
#include <climits>
#include <iomanip>
#define _USE_MATH_DEFINES // for C++
#include <cmath>
#include <future>

using namespace std;

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args);cerr << "\n"; }

vector<string> split(const string& s, char c) {
  vector<string> v;
  stringstream ss(s);
  string x;
  while (getline(ss, x, c))
    v.emplace_back(x);
  return move(v);
}

void err(vector<string>::iterator it) {}
template<typename T, typename... Args>
void err(vector<string>::iterator it, T a, Args... args) {
  cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\t';
  err(++it, args...);
}

const long long mod = 1000000007;
const long long inf = 1000000000;
long long powmod(long long a,long long b) {long long res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}

typedef vector<int> VI;
typedef vector<VI> VVI;

const int INF = 1000000000;

struct MaxFlow {
  int N;
  VVI cap, flow;
  VI dad, Q;

  MaxFlow(int N) :
    N(N), cap(N, VI(N)), flow(N, VI(N)), dad(N), Q(N) {}

  void AddEdge(int from, int to, int cap) {
    this->cap[from][to] += cap;
  }

  int BlockingFlow(int s, int t) {
    fill(dad.begin(), dad.end(), -1);
    dad[s] = -2;

    int head = 0, tail = 0;
    Q[tail++] = s;
    while (head < tail) {
      int x = Q[head++];
      for (int i = 0; i < N; i++) {
        if (dad[i] == -1 && cap[x][i] - flow[x][i] > 0) {
          dad[i] = x;
          Q[tail++] = i;
        }
      }
    }

    if (dad[t] == -1) return 0;

    int totflow = 0;
    for (int i = 0; i < N; i++) {
      if (dad[i] == -1) continue;
      int amt = cap[i][t] - flow[i][t];
      for (int j = i; amt && j != s; j = dad[j])
        amt = min(amt, cap[dad[j]][j] - flow[dad[j]][j]);
      if (amt == 0) continue;
      flow[i][t] += amt;
      flow[t][i] -= amt;
      for (int j = i; j != s; j = dad[j]) {
        flow[dad[j]][j] += amt;
        flow[j][dad[j]] -= amt;
      }
      totflow += amt;
    }

    return totflow;
  }

  int GetMaxFlow(int source, int sink) {
    int totflow = 0;
    while (int flow = BlockingFlow(source, sink))
      totflow += flow;
    return totflow;
  }
};
class Task{

  public:
    static const int maxn = 1003;

    int test_case;
    int N, C, M;
    vector<int> Tick[maxn];

    Task(int test_case);

    void read() {
      cin >> N >> C >> M;
      for(int i = 0; i < M; i++){
        int p, b;
        cin >> p >> b;
        Tick[b].push_back(p);
      }
    }

    void dummyCase() {
    }

    void prepare(){
    }

    string solve(){
      prepare();

      sort(Tick[1].begin(), Tick[1].end());
      sort(Tick[2].begin(), Tick[2].end());

      MaxFlow mf(M + 2);
      for(int i = 0; i < Tick[1].size(); i++){
        mf.AddEdge(0, 1 + i, 1);
      }

      for(int j = 0; j < Tick[2].size(); j++){
        mf.AddEdge(1 + Tick[1].size() + j, M + 1, 1);
      }

      for(int i = 0; i < Tick[1].size(); i++){
        for(int j = 0; j < Tick[2].size(); j++){
          if(Tick[1][i] != Tick[2][j]){
            mf.AddEdge(1 + i, 1 + Tick[1].size() + j, 1);
          }
        }
      }

      int match = mf.GetMaxFlow(0, M + 1);
      error(match);

      int x = match;
      int y = 0;

      map<int, int> qwe;
      for(int i = 0; i < Tick[1].size(); i++){
        qwe[ Tick[1][i] ]++;
      }
      for(int j = 0; j < Tick[2].size(); j++){
        qwe[ Tick[2][j] ]++;
      }

      int hot = -1;
      int hotTime = 0;
      for(auto au : qwe){
        if(hotTime < au.second){
          hot = au.first;
          hotTime = au.second;
        }
      }
      error(hot);

      int a = Tick[1].size() - match;
      int b = Tick[2].size() - match;

      if(a > 0 && b > 0){
        if(hot == 1){
          x += 2 * min(a, b);
        }else{
          x += min(a, b);
          y += min(a, b);
        }
      }

      x += (a - min(a, b)) + (b - min(a, b));
      /* for(int i = 0; i < Tick[1].size(); i++){ */
      /*   if(Tick[1][i] != 0){ */
      /*     for(int j = 0; j < Tick[2].size(); j++){ */
      /*       if(Tick[2][j] != 0){ */
      /*         assert(Tick[1][i] == Tick[2][j]); */
      /*         if(Tick[1][i] == 1){ */
      /*           x += 2; */
      /*         }else{ */
      /*           x += 1; */
      /*           y += 1; */
      /*         } */
      /*         Tick[1][i] = 0; */
      /*         Tick[2][j] = 0; */
      /*         break; */
      /*       } */
      /*     } */
      /*   } */
      /* } */

      /* for(int i = 0; i < Tick[1].size(); i++){ */
      /*   if(Tick[1][i] != 0){ */
      /*     x++; */
      /*     /1* error(x); *1/ */
      /*   } */
      /* } */

      /* for(int j = 0; j < Tick[2].size(); j++){ */
      /*   if(Tick[2][j] != 0){ */
      /*     x++; */
      /*   } */
      /* } */

      stringstream sst;
      sst << "Case #" << test_case << ": " << x << " " << y << endl;

      /* cerr << "test_case: " << test_case << " finished" << endl; */
      return sst.str();
    }
};

Task::Task(int test_case){
  this->test_case = test_case;
}

int main(){
  cout.precision(10);
  cout << fixed;

#ifdef LOCAL_DEFINE
  string problem = "B";

  /* string filename = problem; */
  /* string filename = problem + "-small-practice"; */
  /* string filename = problem + "-large-practice"; */
  /* string filename = problem + "-small-attempt0"; */
  /* string filename = problem + "-small-attempt1"; */
  /* string filename = problem + "-small-attempt2"; */
  string filename = problem + "-small-attempt3";
  /* string filename = problem + "-large"; */

  string input_filename = filename + ".in";
  string output_filename = filename + ".out";

  FILE *fin = freopen(input_filename.c_str(), "r", stdin);
  FILE *fout = freopen(output_filename.c_str(), "w", stdout);

  assert(fin != NULL);
  /* cout << setfill('0') << setw(5) << 25; */

  struct timespec start, finish;
  double elapsed;
  clock_gettime(CLOCK_MONOTONIC, &start);
#endif

  int _T;
  cin >> _T;

  bool multi_thread = false;
  future<string> futures[_T];

  for(int test_case = 1; test_case <= _T; test_case++){
    Task task(test_case);
    task.read();
    /* task.dummyCase(); */

    futures[test_case - 1] = async(std::launch::async, &Task::solve, task);
    if(!multi_thread){
      string ans = futures[test_case - 1].get();
      cout << ans;
    }
  }

  if(multi_thread){
    for(int test_case = 1; test_case <= _T; test_case++){
      string ans = futures[test_case - 1].get();
      cout << ans;
    }
  }

#ifdef LOCAL_DEFINE
  clock_gettime(CLOCK_MONOTONIC, &finish);
  elapsed = (finish.tv_sec - start.tv_sec);
  elapsed += (finish.tv_nsec - start.tv_nsec) / 1000000000.0;
  cerr << "Time elapsed: " << 1.0 * elapsed << " s.\n";
#endif
}


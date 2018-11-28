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

class Task{

  public:
    static const int maxn = 102;

    int test_case;
    int N, P;
    int G[maxn];

    Task(int test_case);

    void read() {
      cin >> N >> P;
      for(int i = 0; i < N; i++){
        cin >> G[i];
      }
    }

    void dummyCase() {
    }

    void prepare(){
    }

    string solve(){
      prepare();

      int ans = 0;
      if(P == 2){
        int cnt = 0;
        for(int i = 0; i < N; i++){
          if(G[i] % 2 == 0){
            cnt++;
          }
        }

        ans = cnt + (N -cnt + 1) / 2;
      }else if(P == 3){
        int cnt = 0;
        int x = 0;
        int y = 0;
        int z;
        for(int i = 0; i < N; i++){
          if(G[i] % 3 == 0){
            cnt++;
          }else if(G[i] % 3 == 1){
            x++;
          }else if(G[i] % 3 == 2){
            y++;
          }
        }

        z = min(x, y);
        ans = cnt + z + (x - z + 2) / 3 + (y - z + 2) / 3;
      }else if(P == 4){
        int cnt = 0;
        int x = 0;
        int y = 0;
        int z = 0;
        int m = 0;
        for(int i = 0; i < N; i++){
          if(G[i] % 4 == 0){
            cnt++;
          }else if(G[i] % 4 == 1){
            x++;
          }else if(G[i] % 4 == 2){
            y++;
          }else if(G[i] % 4 == 3){
            z++;
          }
        }

        m = min(x, z);
        ans = cnt + y / 2 + m + (x - m) / 4 + (z - m) / 4;
        if(y % 2 == 1){
          if((x - m) % 4 == 3 || (z - m) % 4 == 3){
            ans += 2;
          }else{
            ans += 1;
          }
        }else{
          if((x - m) % 4 > 0 || (z - m) % 4 > 0){
            ans += 1;
          }
        }
      }

      stringstream sst;
      sst << "Case #" << test_case << ": " << ans << endl;

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
  string problem = "A";

  /* string filename = problem; */
  /* string filename = problem + "-small-practice"; */
  /* string filename = problem + "-large-practice"; */
  /* string filename = problem + "-small-attempt0"; */
  /* string filename = problem + "-small-attempt1"; */
  /* string filename = problem + "-small-attempt2"; */
  string filename = problem + "-large";

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


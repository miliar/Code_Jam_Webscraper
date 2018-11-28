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

using namespace std;

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }

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
  cerr << it -> substr((*it)[0] == ' ', it -> length()) << " = " << a << '\n';
  err(++it, args...);
}

const long long mod = 1000000007;
long long powmod(long long a,long long b) {long long res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}

int N, K;
long double U;
long double P[51];

int main(){
  cout.precision(10);
  cout << fixed;

#ifdef LOCAL_DEFINE
  FILE *fin = freopen("C.in", "r", stdin);
  assert(fin != NULL);
  FILE *fout = freopen("C.ans", "w", stdout);
  /* cout << setfill('0') << setw(5) << 25; */
#endif

  int T;
  cin >> T;

  for(int testcase = 1; testcase <= T; testcase++){
    cin >> N >> K;

    cin >> U;

    for(int i = 0; i < N; i++){
      cin >> P[i];
    }

    long double ans = 1;
    if(N == 1){
      ans = U + P[0];
    }else{
      multiset<long double> ss;
      for(int i = 0; i < N; i++){
        ss.insert(P[i]);
      }

      while(U > 0){
        int cnt = 0;
        auto a = *ss.begin();

        while(!ss.empty() && (a == *ss.begin())){
          ss.erase(ss.begin());
          cnt++;
        }

        if(ss.empty() || (U <= (*ss.begin() - a) * cnt)){
          /* cerr<< "U = " << U << " cnt = " << cnt << endl; */
          a = a + U / cnt;
          U = 0;
          for(int i = 0; i < cnt; i++){
            ss.insert(a);
          }
          break;
        }else{
          /* cerr<< "U = " << U << " cnt = " << cnt << endl; */
          U -= (*ss.begin() - a) * cnt;
          a = *ss.begin();
          for(int i = 0; i < cnt; i++){
            ss.insert(a);
          }
        }
      }

      for(auto a : ss){
        ans *= a;
      }
    }

    cout << "Case #" << testcase << ": " << ans << endl;
  }


#ifdef LOCAL_DEFINE
  cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
}


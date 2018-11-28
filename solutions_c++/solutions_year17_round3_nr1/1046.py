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

long double dp[1003];
long double R[1003];
long double H[1003];

int main(){
  cout.precision(10);
  cout << fixed;

#ifdef LOCAL_DEFINE
  FILE *fin = freopen("A.in", "r", stdin);
  assert(fin != NULL);
  FILE *fout = freopen("A.ans", "w", stdout);
  /* cout << setfill('0') << setw(5) << 25; */
#endif

  int T;
  cin >> T;

  for(int testcase = 1; testcase <= T; testcase++){
    int N, K;
    cin >> N >> K;

    memset(R, 0, sizeof R);
    memset(H, 0, sizeof H);
    vector< pair<long double, int> > dp;
    for(int i = 0; i < N; i++){
      cin >> R[i] >> H[i];
      dp.push_back({R[i] * H[i], i});
    }

    sort(dp.begin(), dp.end());
    reverse(dp.begin(), dp.end());

    long double ans = 0;
    for(int k = 0; k < N; k++){
      long double temp = 2 * M_PI * R[k] * H[k];
      int cnt = 1;
      if(cnt < K){
        for(int i = 0; i < N; i++){
          if(k != dp[i].second){
            if(R[ dp[i].second ] <= R[k]){
              cnt++;
              temp += 2 * M_PI * dp[i].first;

              if(cnt == K){
                break;
              }
            }
          }
        }
      }

      if(cnt == K){
        temp += M_PI * R[k] * R[k];
        if(temp > ans){
          ans = temp;
          /* cerr << "k = " << k << endl; */
        }
      }
    }

    cout << "Case #" << testcase << ": " << ans << endl;
  }


#ifdef LOCAL_DEFINE
  cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
}


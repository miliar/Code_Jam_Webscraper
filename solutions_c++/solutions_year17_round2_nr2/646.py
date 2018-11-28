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

vector<char> ans;
int N, R, O, Y, G, B, V;

void f(char ca, int ia, char cb, int ib, char cc, int ic){
  for(int i = 0; i <= 2 * (ia - 1); i+=2){
    ans[i] = ca;
  }

  for(int i = 1; i < 2 * (ia - 1); i+=2){
    if(ib > ic){
      ans[i] = cb;
      ib--;
    }else{
      ans[i] = cc;
      ic--;
    }
  }

  for(int i = 2 * ia - 1; i < N; i++){
    if(ib > ic){
      ans[i] = cb;
      ib--;
    }else{
      ans[i] = cc;
      ic--;
    }
  }
}

int main(){
  cout.precision(10);
  cout << fixed;

#ifdef LOCAL_DEFINE
  FILE *fin = freopen("B.in", "r", stdin);
  assert(fin != NULL);
  FILE *fout = freopen("B.ans", "w", stdout);
  /* cout << setfill('0') << setw(5) << 25; */
#endif

  int T;
  cin >> T;

  for(int testcase = 1; testcase <= T; testcase++){
    cin >> N >> R >> O >> Y >> G >> B >> V;

    char ca = 'R', cb = 'Y', cc = 'B';
    int ia = R, ib = Y,ic = B;

    if(ia < ib){
      swap(ia, ib);
      swap(ca, cb);
    }

    if(ia < ic){
      swap(ia, ic);
      swap(ca, cc);
    }

    if(ib < ic){
      swap(ib, ic);
      swap(cb, cc);
    }

    if(ia > N / 2){
      cout << "Case #" << testcase << ": IMPOSSIBLE" << endl;
    }else{
      ans.resize(N);
      f(ca, ia, cb, ib, cc, ic);

      cout << "Case #" << testcase << ": ";
      for(char ch : ans){
        cout << ch;
      }
      cout << endl;
    }
  }


#ifdef LOCAL_DEFINE
  cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
}


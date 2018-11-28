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

int E[102], S[102];
long double R[102];
long double D[102][102];
long double Vis[102][102];
int U[102], V[102];
long double Time[120];

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
    int N, Q;
    cin >> N >> Q;

    for(int i = 0; i < N; i++){
      cin >> E[i] >> S[i];
    }

    for(int i = 0; i < N; i++){
      for(int j = 0; j < N; j++){
        cin >> D[i][j];
      }
    }

    /* if(testcase == 69){ */
    /*   cerr << "debug" << endl; */
    /* } */
    /* for(int k = 2; k < N; k++){ */
    /*   for(int i = 0; i < N - k; i++){ */
    /*     if(D[i][i + k - 1] > 0 && D[i + k - 1][i + k] > 0){ */
    /*       D[i][i + k] = D[i][i + k - 1] + D[i + k - 1][i + k]; */
    /*     } */
    /*   } */
    /* } */

    for(int i = 0; i < Q; i++){
      cin >> U[i] >> V[i];
    }

    cout << "Case #" << testcase << ":";
    for(int i = 0; i < Q; i++){
      int u = U[i];
      int v = V[i];

      u--;
      v--;

      long double ans = 1e18;
      set< pair<long double, tuple<int, int, int> > > ss;
      ss.insert( {0, {u, E[u], S[u]} });
      for(int i = 0; i < N; i++){
        R[i] = 1e18;
      }
      while(!ss.empty()){
        long double tt = ss.begin()->first;
        int uu = get<0>(ss.begin()->second);
        int ee = get<1>(ss.begin()->second);
        int sp = get<2>(ss.begin()->second);

        ss.erase(ss.begin());
        /* if(testcase == 70){ */
        /*   cerr << tt << endl; */
        /* } */

        if(tt >= ans){
          break;
        }

        if(uu == v){
          ans = min(ans, tt);
        }
        for(int j = 0; j < N; j++){
          if(D[uu][j] > 0 && ee >= D[uu][j]){
            ss.insert( {tt + D[uu][j] / sp, {j, ee - D[uu][j], sp}} );
            /* if(ss.find( {tt + D[uu][j] / sp, {j, ee - D[uu][j], sp}} ) == ss.end()){ */
            /* } */
            if(tt + D[uu][j] / sp < R[j]){
              ss.erase( {R[j], {j, E[j], S[j]}} );
              R[j] = tt + D[uu][j] / sp;
              ss.insert( {R[j], {j, E[j], S[j]}} );
            }
            /* if(ss.find( {tt + D[uu][j] / sp, {j, E[j], S[j]}} ) == ss.end()){ */
            /*   ss.insert( {tt + D[uu][j] / sp, {j, E[j], S[j]}} ); */
            /*   if(testcase == 70){ */
            /*     cerr << tt << endl; */
            /*     cerr << "sp = " << sp << endl; */
            /*     cerr << "uu = " << uu << " j = " <<  j << endl; */
            /*   } */
            /* } */
          }
        }
      }

      cout << " " << ans;
    }
    cout << endl;
  }


#ifdef LOCAL_DEFINE
  cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
}


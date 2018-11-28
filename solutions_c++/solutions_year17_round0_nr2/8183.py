#include <iostream>
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
#define _USE_MATH_DEFINES // for C++
#include <cmath>

using namespace std;

const long long mod = 1000000007;
long long powmod(long long a,long long b) {long long res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}


int main(){
  cout.precision(10);
  cout << fixed;

#ifdef LOCAL_DEFINE
  FILE *fin = freopen("B.in", "r", stdin);
  assert(fin != NULL);
  FILE *fout = freopen("B.ans", "w", stdout);
#endif

  int T;
  cin >> T;

  for(int testcase = 1; testcase <= T; testcase++){
    string s;
    cin >> s;

    int n = s.size();

    int p = 1;
    while(p < n){
      if(s[p] < s[p - 1]){
        s[p - 1]--;
        break;
      }
      p++;
    }

    if(p == n){
      cout << "Case #" << testcase << ": " << s << endl;
    }else{
      for(int i = p; i < n; i++){
        s[i] = '9';
      }

      p--;
      while(p > 0){
        if(s[p - 1] > s[p]){
          s[p] = '9';
          s[p - 1]--;
          p--;
        }else{
          break;
        }
      }

      cout << "Case #" << testcase << ": ";
      for(char ch : s){
        if(ch != '0'){
          cout << ch;
        }
      }
      cout << endl;
    }

    int ans = 0;
  }


#ifdef LOCAL_DEFINE
  cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
}


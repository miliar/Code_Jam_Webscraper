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
  FILE *fin = freopen("C.in", "r", stdin);
  assert(fin != NULL);
  FILE *fout = freopen("C.ans", "w", stdout);
#endif

  int T;
  cin >> T;

  for(int testcase = 1; testcase <= T; testcase++){
    long long n, k;
    cin >> n >> k;

    while(k > 1){
      if(k & 1){
        if(n & 1){
          n = n / 2;
        }else{
          n = n / 2 - 1;
        }
      }else{
        n = n / 2;
      }
      k = k / 2;
      /* cerr << n << " " << k << endl; */
    }

    multiset<long long> ss;
    ss.insert(-n);

    while(k--){
      long long l = -(*ss.begin());
      ss.erase(ss.begin());
      /* cout << "l = " << l << endl; */

      long long a, b;
      if(l & 1){
        a = l / 2;
        b = l / 2;
      }else{
        a = l / 2;
        b = l / 2 - 1;
      }

      if(k == 0){
        cout << "Case #" << testcase << ": " << a << " " << b << endl;
      }
      ss.insert(-a);
      ss.insert(-b);
    }
  }


#ifdef LOCAL_DEFINE
  cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
}


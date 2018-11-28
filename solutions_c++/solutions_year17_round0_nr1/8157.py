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

const int N = 1003;
bool a[N];

void flit(int p, int k){
  for(int i = p; i < p + k; i++){
    a[i] = !a[i];
  }
}

int main(){
  cout.precision(10);
  cout << fixed;

#ifdef LOCAL_DEFINE
  FILE *fin = freopen("A.in", "r", stdin);
  assert(fin != NULL);
  FILE *fout = freopen("A.ans", "w", stdout);
#endif

  int T;
  cin >> T;

  for(int testcase = 1; testcase <= T; testcase++){
    string s;
    int k;
    cin >> s >> k;

    int n = s.size();
    for(int i = 0; i < n; i++){
      if(s[i] == '+'){
        a[i] = true;
      }else{
        a[i] = false;
      }
    }

    int ans = 0;
    for(int i = 0; i <= n - k; i++){
      if(a[i]){
        continue;
      }else{
        ans++;
        flit(i, k);
      }
    }

    for(int i = n - k + 1; i < n; i++){
      if(a[i] == 0){
        ans = -1;
        break;
      }
    }

    if(ans == -1){
      cout << "Case #" << testcase << ": " << "IMPOSSIBLE" << endl;
    }else{
      cout << "Case #" << testcase << ": " << ans << endl;
    }
  }


#ifdef LOCAL_DEFINE
  cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
#endif
}


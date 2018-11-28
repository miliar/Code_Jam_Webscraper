#include <iostream>
#include <cassert>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)

int N, P;
int A[128];

// mod_0 is calculated using N
// mod_3, mod_2, mod_1, left
int dp[100][100][100][100];

int adj(int x) {
  return (P+P+P+x)%P;
}

int fun(int mod_3, int mod_2, int mod_1, int left) {
  // cout << mod_1 << " " << mod_2 << " " << mod_3 << " " << left << endl;
  assert(mod_1 >= 0);
  assert(mod_2 >= 0);
  assert(mod_3 >= 0);
  assert(left >= 0 && left < P);
  int &res = dp[mod_3][mod_2][mod_1][left];
  if (res != -1) return res;
  if (mod_1 == 0 && mod_2 == 0 && mod_3 == 0) {
    return res = 0;
  }
  res = 0;
  if (left == 0) {
    if (mod_3 > 0) res = max(res,1+fun(mod_3-1,mod_2,mod_1,P-3));
    if (mod_2 > 0) res = max(res,1+fun(mod_3,mod_2-1,mod_1,P-2));
    if (mod_1 > 0) res = max(res,1+fun(mod_3,mod_2,mod_1-1,P-1));
  } else {
    if (mod_3 > 0) res = max(res,fun(mod_3-1,mod_2,mod_1,adj(left-3)));
    if (mod_2 > 0) res = max(res,fun(mod_3,mod_2-1,mod_1,adj(left-2)));
    if (mod_1 > 0) res = max(res,fun(mod_3,mod_2,mod_1-1,adj(left-1)));
  }
  return res;
}

void do_case(int cn) {
  cin >> N >> P;
  FOR(i,0,N) cin >> A[i];
  memset(dp,-1,sizeof(dp));
  int mod_0 = 0;
  int mod_1 = 0;
  int mod_2 = 0;
  int mod_3 = 0;
  FOR(i,0,N) {
    if (A[i] % P == 0) mod_0++;
    if (A[i] % P == 1) mod_1++;
    if (A[i] % P == 2) mod_2++;
    if (A[i] % P == 3) mod_3++;
  }
  assert(N == mod_0 + mod_1 + mod_2 + mod_3);
  cout << "Case #" << cn << ": " << (mod_0 + fun(mod_3, mod_2, mod_1, 0)) << endl;
}

int main() {
  int T;
  cin >> T;
  FORE(te,1,T) do_case(te);
  return 0;
}
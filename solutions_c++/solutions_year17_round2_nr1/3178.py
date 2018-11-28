#include <algorithm>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> VI;
typedef pair<int, int> ipair;
typedef tuple<int, int, int> ituple;

const int INF = (int)2e9;
// const int MOD = (int)1e9 + 7;
// const double EPS = 1e-10;

#define MAX_N 10000 + 2

void exec(int c){
  ll d, n, k[MAX_N], s[MAX_N];
  long double ans = -1;
  cin >> d >> n;
  for (int i = 0; i < n; i++){
    scanf("%lld%lld", &k[i], &s[i]);
    if (ans == -1){
      ans = (long double)s[i] * d / (d - k[i]);
    }
    else{
      ans = min(ans, (long double)s[i] * d / (d - k[i]));
    }
  }

  printf("Case #%d: %.9Lf\n", c, ans);


}

void solve(){
  int t = 1;
  scanf("%d", &t);
  for (int i = 0; i < t; i++){
    exec(i + 1);
  }
}

int main(){
  solve();
  return 0;
}

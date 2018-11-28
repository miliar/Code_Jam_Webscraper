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

// const int INF = (int)2e9;
// const int MOD = (int)1e9 + 7;
// const double EPS = 1e-10;

#define MAX_N 100 + 2
string s;
int ns[20];

bool decrement(int pos){
  if (pos == s.length()){
    return false;
  }
  if (ns[pos] == 0){
    bool result = decrement(pos + 1);
    if (result){
      ns[pos] = 9;
    }
    return result;
  }
  ns[pos]--;
  return true;
}

void exec(int t){
  cin >> s;
  for (int i = 0; i < s.length(); i++){
    ns[i] = s[s.length() - i - 1] - '0';
  }

  for (int i = 0; i < s.length() - 1; i++){
    int digit = ns[i];
    for (int j = i + 1; j < s.length(); j++){
      if (ns[j] > digit){
        ns[i] = 9;
        decrement(i + 1);
        break;
      }
      digit = ns[j];
    }
  }

  ll ans = 0;
  ll fact = 1;

  for (int i = 0; i < s.length(); i++){
    ans += ns[i] * fact;
    fact *= 10;
  }


  printf("Case #%d: %lld\n", t + 1, ans);

}

void solve(){
  int t = 1;
  scanf("%d", &t);
  for (int i = 0; i < t; i++){
    exec(i);
  }
}

int main(){
  solve();
  return 0;
}

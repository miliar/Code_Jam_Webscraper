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

void exec(int t){
  string s;
  int k;
  cin >> s >> k;
  int flip = 0;

  for (int i = 0; i < s.length() - k + 1; i++){
    if (s[i] == '-'){
    flip++;
    for (int j = 0; j < k; j++){
      if (s[i + j] == '-'){
        s[i + j] = '+';
      }
      else if (s[i + j] == '+'){
        s[i + j] = '-';
      }
    }

    }
  }

  bool isOk = true;
  for (int i = 0; i < s.length(); i++){
    if (s[i] == '-'){
      isOk = false;
      break;
    }
  }

if (isOk){
  printf("Case #%d: %d\n", t + 1, flip);

}
else{
  printf("Case #%d: IMPOSSIBLE\n", t + 1);

}

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

#include<iostream>
#include<algorithm>
#include<map>

using namespace std;
typedef long long Int;

void solve(){
  Int n, k;
  cin >> n >> k;
  map<Int, Int> dp;
  dp[n] = 1;
  while(true){
    map<Int, Int>::reverse_iterator it = dp.rbegin();
    Int num = it->first;
    Int cnt = it->second;
    Int lhalf = num / 2;
    Int rhalf = num - lhalf - 1;
    dp[lhalf] += cnt;
    dp[rhalf] += cnt;
    k -= cnt;
    if(k <= 0){
      cout << lhalf << " " << rhalf << endl;
      return;
    }
    dp.erase(num);
  }
}

int main(){
  Int t;
  cin >> t;
  for(Int i = 1;i <= t;i++){
    cout << "Case #" << i << ": ";
    solve();
  }
  return 0;
}

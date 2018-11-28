//  @author TimeDragon

#include <bits/stdc++.h>
using namespace std;


int main(){

  int Test;
  cin >> Test;
  for(int test = 1; test <= Test; ++test){

    int n, p;
    cin >> n >> p;
    int arr[p];
    int arn[n];

    for(int i = 0; i < p; ++i) {
      arr[i] = 0;
    }

    for(int i = 0; i < n; ++i) {
      cin >> arn[i];
      arr[arn[i] % p]++;
    }

    int ans = arr[0];

    if(p == 2) {
      ans += (arr[1] + 1) / 2;
    }
    else if(p == 3) {
      ans += min(arr[1], arr[2]);
      int dif = max(arr[1], arr[2]) - min(arr[1], arr[2]);
      ans += (dif + 2) / 3;
    }
    cout << "Case #" << test <<": " << ans << endl;
  }
  return 0;
}
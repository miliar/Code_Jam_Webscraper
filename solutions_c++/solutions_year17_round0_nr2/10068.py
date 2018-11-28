#include<iostream>
#include<vector>
#include <algorithm>
#include <string>
using namespace std;

bool satisfy(int i){
  vector<int> digits;
  while(i > 0){
    digits.insert(digits.begin(),i%10);
    //cout << (i%10)<<endl;
    i /= 10;

  }
  return is_sorted(digits.begin(), digits.end());
}
int solve(int K){
  int ans;
  for(int i = K; i >= 0; i --){
    if(satisfy(i)){
      return i;
    }
  }
}
int main (){
    int T,ans;
    string s;
    int N;
    cin >> T;
    for(int i = 1; i <= T; i++){
      cin >> N;
      ans = solve(N);
      cout << "Case #"<<i<<": "<<ans<<endl;

    }
}

#include<bits/stdc++.h>


using namespace std;


bool isTidyNumber(int n){
  string str = to_string(n);
  for(int i = 0; i < str.size() - 1; i++){
    if(str[i] > str[i + 1]){
      return false;
    }
  }
  return true;
}

int main(){
  cin.tie(0);
  ios::sync_with_stdio(0);
  int t;
  cin >> t;
  for(int now = 1; now <= t; now++){
    cout << "Case #" << now << ": ";
    int n;
    cin >> n;
    int ans = 1;
    for(int i = n; i > 0; i--){
      if(isTidyNumber(i)){
        cout << i << "\n";
        break;
      }
    }
  }
}
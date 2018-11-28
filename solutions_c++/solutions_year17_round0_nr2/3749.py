#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int main(){
  long long x;
  int N;
  cin >> N;
  for(int i = 1; i <= N; i++){
    vector<long long> dig;
    cin >> x;
    while(x){
      dig.push_back(x%10);
      x /= 10;
    }
    for(int j = 0; j < dig.size()-1; j++){
      if(dig[j] < dig[j+1]){
        for(int k = j; k > -1; k--)
          dig[k] = 9;
        dig[j+1]--;
      }
    }
    int lead = 0;
    for(int j = dig.size()-1; j > -1; j--){
      if(dig[j]) break;
      lead++;
    }
    cout << "Case #" << i << ": ";
    for(int j = dig.size()-1-lead; j > -1; j--){
      cout << dig[j];
    }
    cout << endl;
  }
  return 0;
}

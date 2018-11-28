#include <iostream>
#include <vector>
#include <string>

using namespace std;

string recS(string num){
  int ind = 0;
  for(int i = 1; i < num.size(); i++){
    int last = (int)num[i-1] - 48;
    int curr = (int)num[i] - 48;
    if(curr < last){
      last--;
      num[i-1] = '0' + last;
      int nine = 9;
      for(int j = i; j < num.size(); j++){
        num[j] = '0'+nine;
      }
      break;
    }
    ind = i;
  }
  if(ind != num.size()-1){
    num = recS(num);
  }
  return num;
}

void solve(string num){
  if(num.size()==1){
    cout << num << endl;
    return;
  }
  string fix = recS(num);
  // remove leading zeroes
  fix.erase(0, fix.find_first_not_of('0'));
  cout << fix << endl;
}

int main(){
  int T;
  cin >> T;
  string num;
  for(int i = 0; i < T; i++){
    cin >> num;
    cout << "Case #" << i+1 << ": ";
    solve(num);
  }
  return 0;
}

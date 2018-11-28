#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

void print_case(int T){
  cout << "Case #" << T << ": ";
}

int main(){
  int T;  cin >> T;
  for(int ii = 1; ii <= T; ii++){
    string s; cin >> s;
    int len = s.length();
    int i = 0;
    string prior_s = "";
    while(prior_s != s){
      prior_s = s;
      for(i = 0; i < len-1; i++){
        if(s[i] > s[i+1]){
          s[i] = s[i]-1;
          break;
        }
      }
      for(i = i+1; i < len; i++){
        s[i] = '9';
      }
    }
    print_case(ii);
    if(s[0] == '0'){
      for(int j = 1; j < len; j++)  cout << s[j];
      cout << endl;
    }
    else{
      cout << s << endl;
    }
  }

  return 0;
}

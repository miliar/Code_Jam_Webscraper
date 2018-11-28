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
    int k;  cin >> k;
    int len = s.length();
    int count = 0;
    for(int i = 0; i <= len-k; i++){
      if(s[i] == '-'){
        for(int j = 0; j < k; j++){
          if(s[i+j] == '+')  s[i+j] = '-';
          else s[i+j] = '+';
        }
        //cout << s << endl;
        count++;
      }
    }
    int result = 1;
    for(int i = len-k+1; i < len; i++){
      if(s[i] == '-'){
        result = 0;
        break;
      }
    }
    print_case(ii);
    if(result == 1) cout << count << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}

#include <cstdio>
#include <iostream>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++){
    string s;
    int k;
    cin >> s >> k;
    string res = "";
    for(int j = 0; j < s.size(); j++)
      res += '+';
    int count = 0;

    for(int j = 0; j <= s.size() - k; j++){
      if(s[j] == '-'){
        for(int l = j; l <= j + k - 1; l++){
          if(s[l] == '-')
            s[l] = '+';
          else
            s[l] = '-';
        }
        count++;
      }
    }

    cout << "Case #" << i << ": ";
    if(s == res)
      cout << count << endl;
    else
      cout << "IMPOSSIBLE" << endl;

  }
  return 0;
}

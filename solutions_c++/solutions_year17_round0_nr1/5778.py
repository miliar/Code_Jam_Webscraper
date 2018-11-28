#include <vector>
#include <iostream>

using namespace std;

int main(){
  int t;
  cin >> t;
  for(int i = 0;i<t;i++){
    string s;
    int k;
    cin >> s >> k;
    int c=0;
    bool b = true;
    for(int j = 0;j<s.size();j++){
      if(s[j] == '-'){
        if(j<=s.size()-k){
          c++;
          for(int x = 0; x<k;x++){
            if(s[j+x] == '+')
              s[j+x] = '-';
            else
              s[j+x] = '+';
          }
        }
        else
          b = false;
      }
    }
    cout << "Case #" << i+1 << ": ";
    if(b)
      cout << c << endl;
    else
      cout << "IMPOSSIBLE" << endl;
  }
  return 0;
}

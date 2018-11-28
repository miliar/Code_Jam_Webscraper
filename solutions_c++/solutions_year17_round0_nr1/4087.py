#include <iostream>
#include <string>
using namespace std;

int main()
{
  int n, k;
  string s;
  cin >> n;
  for(int i = 0; i < n; i++){
    int count = 0;
    cin >> s >> k;
    for(int j = 0; j < s.length() - (k - 1) ; j++){
      if(s[j] == '-'){
        for(int l = 0; l < k; l++){
          if(s[j + l] == '+'){
            s[j + l] = '-';
          }else{
            s[j + l] = '+';
          } 
        }
        count++;
      }

    }
    if((int) s.find('-') != -1){
      cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
    }else{
      cout << "Case #" << i + 1 << ": " << count << endl;
    }
  }
  return 0;
}
#include <iostream>

using namespace std;

int main(){
  int t; 
  cin >> t;
  for (int c = 1; c <= t; c++){
    string pan;
    int s;
    cin >> pan >> s;
    int result = 0;
    for (int i = 0; i <= pan.size() - s; i++){
      if (pan[i] == '-'){
        for(int j = i; j < i + s; j++){
          pan[j] = pan[j] == '-' ? '+' : '-';
        }
        result++;
      }
    }

    bool possible = true;
    for (auto p: pan){
      if (p == '-'){
        possible = false;
        break;
      }
    }
    if (possible)
      cout << "Case #" << c << ": " << result << endl;
    else
      cout << "Case #" << c << ": IMPOSSIBLE" << endl;
  }
  return 0;
}
#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(){
  int t, k, n, moves;
  char pancakes[1001], *flipper;
  cin >> t;
  for(int _t=0; _t < t; _t++){
    cin >> pancakes >> k;
    n = strlen(pancakes);
    moves = 0;
    cout << "Case #" << _t+1 << ": ";
    for(int i=0; i < n; i++){
      if(pancakes[i] == '+'){
        continue;
      }else{
          moves += 1;
          for(int j=i; j <= n && j < i + k; j++){
            if(j == n){
              cout << "IMPOSSIBLE";
              goto next_test;
            }
            if(pancakes[j] == '-'){
              pancakes[j] = '+';
            }else{
              pancakes[j] = '-';
            }
          }
      }
    }
    cout << moves;
    next_test:
    cout << "\n";
  }
}

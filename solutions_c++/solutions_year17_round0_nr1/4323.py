#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
  int t, no = 1;
  cin >> t;
  while(t--){
    string answ;
    string pancakes;
    int k, counter = 0;
    cin >> pancakes >> k;
    int i = 0;
    while(i < pancakes.size() - k + 1){
      // cout << i << "\t" << pancakes[i] << "\t" << pancakes << endl;
      if(pancakes[i]=='+'){
        i++;
      } else {
        for(int j = i; j < i + k; j++){
          if(pancakes[j] == '-'){
            pancakes[j] = '+';
          } else {
            pancakes[j] = '-';
          }
        }
        counter++;
        i++;
      }
    }
    bool all_happy = true;
    while(i < pancakes.size()){
      if(pancakes[i]=='-'){
        all_happy = false;
      }
      i++;
    }
    cout << "Case #" << no << ": ";
    if(all_happy){
      cout << counter;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
    no++;
  }

  return 0;
}

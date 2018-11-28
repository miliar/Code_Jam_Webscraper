#include <iostream>
#include <string>
using namespace std;

#define ull unsigned long long

int main(){
  int t;
  cin >> t;
  string pancake;
  int flipper_size;
  ull flip_count=0;
  bool possible=true;

  //forall test cases
  for(int i(0); i<t; ++i){
    cin >> pancake;
    cin >> flipper_size;
    flip_count=0;
    possible=true;

    //forall pancake characters
    for(int j(0); j<pancake.size(); ++j){
      //flip is encountered down pancake and in bound
      if(pancake[j]=='-' and j+flipper_size-1<pancake.size()){
        //flip
        for(int f(j); f<flipper_size+j; ++f){
          if(pancake[f]=='-'){
            pancake[f]='+';
          } else{
            pancake[f]='-';
          }
        }
        ++flip_count;
      }
    }

    for(int j(0); j<pancake.size(); ++j){
      if(pancake[j]=='-'){
        possible=false;
        break;
      }
    }
    if(possible){
      cout << "Case #" << i+1 << ": " << flip_count << endl;
    } else{
      cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}

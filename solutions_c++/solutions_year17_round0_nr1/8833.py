/**
* Author: Christos Christou (christosnc)
* Date  : 07/04/2017
**/

#include <iostream>
#include <fstream>
using namespace std;

char flip(char a){
  if(a == '+') return '-';
  else return '+';
}

int main(){
  ifstream input;
  ofstream output;
  input.open("A-large.in");
  output.open("output.txt");

  int t;
  input >> t;
  int k;
  string pan;
  string *res = new string[t];

  for(int i = 0; i < t; i++){
    input >> pan >> k;
    int x = 0;
    for(int j = 0; j < pan.length(); j++){
      if(pan[j] == '+') x++;
    }
    if(x == pan.length()){
      res[i] = "0";
      continue;
    }

    x = 0;
    for(int j = 0; j < pan.length(); j++){
      if(pan[j] == '-'){
        if(pan.length() - j < k){
          res[i] = "IMPOSSIBLE";
          break;
        } else{
          for(int m = 0; m < k; m++) pan[j + m] = flip(pan[j + m]);
          x++;
        }
      }
    }
    if(res[i] != "IMPOSSIBLE") res[i] = to_string(x);
  }

  for(int i = 1; i <= t; i++){
    output << "Case #" << i << ": " << res[i - 1] << "\n";
  }

  input.close();
  output.close();
  return 0;
}

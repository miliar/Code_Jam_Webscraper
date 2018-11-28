/**
* Author: Christos Christou (christosnc)
* Date  : 07/04/2017
**/

#include <iostream>
#include <fstream>
using namespace std;

string thething(string s, int p){
  if(p == 0) return s;
  string a = s;
  a[p] = '9';
  for(int i = p + 1; i < s.length(); i++) a[i] = '9';
  if(s[p - 1] == '0'){
    return thething(a, p - 1);
  }
  a[p - 1] -= 1;
  return a;
}

int main(){
  ifstream input;
  ofstream output;
  input.open("B-small-attempt2.in");
  output.open("output.txt");

  int t;
  input >> t;
  string *cap = new string[t];

  for(int i = 0; i < t; i++){
    long long int n;
    input >> n;
    string o = to_string(n);
    while(1){
      int x = 0;
      for(int j = o.length() - 1; j > 0; j--){
        for(int k = o.length() - 2; k >= 0; k--){
          if(o[k] > o[j]) x = 1;
        }
      }
      if(x == 0) break;

      for(int j = o.length() - 1; j > 0; j--){
        for(int k = o.length() - 2; k >= 0; k--){
          if(o[k] > o[j]){
            o = thething(o, j);
          }
        }
      }
    }
    string a = "";
    int p = 0;
    for(int j = 0; j < o.length(); j++){
      if(o[j] != '0') p = 1;
      if(p == 0 && o[j] == '0');
      else a += o[j];
    }
    cap[i] = a;
  }

  for(int i = 0; i < t; i++){
    output << "Case #" << i + 1 << ": " << cap[i] << "\n";
  }

  input.close();
  output.close();
  return 0;
}

#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

string num;
string initial;

bool check(){
    for(int i = 1; i <num.size(); i++){
      if(!(num[i] >= num[i - 1]))
        return false;
    }
    return true;
}

bool checksize(){
  for(int i = 0; i <num.size(); i++){
    if(num[i] < initial[i])
      return true;
    if(num[i] > initial[i])
      return false;
  }
  return true;
}

char change(char a){
  if(a == '0')
    return '9';
  return a - 1;
}

string checkzero(){
  if(num[0] == '0')
    num.erase(0,1);
}



int main(){
  int T;
  cin >> T;
  for(int i = 1; i <= T; i++){
    cin >> num;
    initial = num;
    int len = num.size();
    for(int i = num.size() - 1; i >= 1; i--){
      if(check() && checksize())
        break;
      num[i] = '9';
      num[i - 1] = change(num[i - 1]);
    }
    checkzero();
    printf("Case #%d: %s\n", i, num.c_str());
  }


  return 0;
}

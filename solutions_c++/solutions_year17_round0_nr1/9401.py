#include <iostream>

using namespace std;

char flip(char simbol){
  if(simbol == '+'){
    return '-';
  }else{
    return '+';
  }
}

int isdone(string str){
  for(int i = 0; i < str.length(); i++){
    if(str[i] == '-'){
      return 0;
    }
  }
  return 1;
}

int main(){

  int count = 0, times = 0, numtests = 0;
  cin >> numtests;
  string str[numtests];
  int resp[numtests];

  for(int i = 0; i < numtests; i++){
    cin >> str[i];
    cin >> times;
    if(isdone(str[i])){
      resp[i] = 0;
    }else{
      for(int j = 0; j <= (str[i].length() - times); j++){
        if(str[i][j] == '-'){
          for(int k = 0; k < times; k++){
            str[i][j+k] = flip(str[i][j+k]);
          }
          resp[i] = ++count;
        }
      }
      count = 0;
    }
  }
  for(int i = 0; i < numtests; i++){
    if(isdone(str[i]))
      cout << "Case #" << i+1 << ": " << resp[i] << endl;
    else
      cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
  }

  return 0;
}

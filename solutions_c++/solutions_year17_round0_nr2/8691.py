#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int main(){
  int T; scanf("%d", &T);
  for(int cs = 1; cs <= T; cs++){
    printf("Case #%d: ", cs);
    bool ans = true;
    char number[20]; int size;
    scanf("%s", number);
    size = (int) strlen(number);
    for(int i = 0; i < size - 1; i++){
      if(number[i] > number[i + 1]) ans = false;
    }
    if(ans){
      cout << number << endl;
      continue;
    }else{
       for(int i = size - 1; i > 0; i--){
        if(number[i - 1] > number[i]){
          number[i] = '9';
          number[i - 1] -= 1;
        }
      }
       //cout << "parcial " << number << endl;
      for(int i = 0; i < size - 1; i++){
        if(number[i] > number[i + 1]){
          if(number[i] == '9' && number[i + 1] == '0'){
            number[i + 1] = '9';
          }else{
            number[i + 1] = '9';
            //number[i] -= 1;
          }
        }
      }
    }
    int start = 0;
    while(number[start] == '0') start++;
    for(int i = start; i < size; i++) printf("%c", number[i]);
    puts("");
  }
  return 0;
}

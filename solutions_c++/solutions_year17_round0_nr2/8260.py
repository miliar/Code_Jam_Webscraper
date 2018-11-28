#include <string>
#include <iostream>
using namespace std;

int main(){
  int t;
  cin >> t;
  
  string input;
  int firstNonZero=0; 
  for(int i(0); i<t; ++i){
    cin >> input;

    //size 1 are trivally true
    if (input.size()==1){
      cout << "Case #" << i+1 << ": " << input << endl;
    } else{
      //process test case
      for (int j(input.size()-1); j>0; --j){
        if (input[j] < input[j-1] or input[j-1]=='0'){

          input[j]='9';
          for(int h(j); h<input.size(); ++h){
            input[h]='9';
          }
          if (input[j-1] != '0'){
            switch (input[j-1]){
              case '1': input[j-1]='0'; break;
              case '2': input[j-1]='1'; break;
              case '3': input[j-1]='2'; break;
              case '4': input[j-1]='3'; break;
              case '5': input[j-1]='4'; break;
              case '6': input[j-1]='5'; break;
              case '7': input[j-1]='6'; break;
              case '8': input[j-1]='7'; break;
              case '9': input[j-1]='8';
            }
          }
        }
      }
        //cleanup front zeros
        for(firstNonZero=0; 
            firstNonZero<input.size() and input[firstNonZero]=='0';
            ++firstNonZero);
        input.erase(0,firstNonZero);
        cout << "Case #" << i+1 << ": " << input << endl;
    }
  }

  return 0;
}

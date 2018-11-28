#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

int main(){

  int numberOfTrials;
  string TEMP;
  int TEMPOR;
  cin >> numberOfTrials;
  vector<string> INPUTS;
  vector<int> SizeInputs;
  for(int t = 0; t < numberOfTrials; t++){
    cin >> TEMP;
    INPUTS.push_back(TEMP);
    cin >> TEMPOR;
    SizeInputs.push_back(TEMPOR);
  }

  for(int i = 0; i < numberOfTrials; i++){
    vector<char> pancakes;
    char temp;
    TEMP = INPUTS[i];
    int size = SizeInputs[i];
    int flipCount = 0;
    int plusCount = 0;

    for(int p = 0; p < TEMP.size(); p++){
      temp = TEMP[p];
      pancakes.push_back(temp);
    }

    for(int q = pancakes.size()-1; q >= 0; q--){
      if(q >= size-1){
        if(pancakes[q] == '-'){
          pancakes[q] = '+';
          flipCount++;
          for(int subtract = 1; subtract < size; subtract++){
            if(pancakes[q-subtract] == '-'){
              pancakes[q-subtract] = '+';
            }
            else{
              pancakes[q-subtract] = '-';
            }
          }
        }
      }
    }
    for(int g = 0; g < pancakes.size(); g++){
      if(pancakes[g] == '+'){
        plusCount++;
      }
    }
    if(plusCount == pancakes.size()){
      cout << "Case #" << i+1 << ": " << flipCount << endl;
    }
    else{
      cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
    }
  }

  return 0;
}

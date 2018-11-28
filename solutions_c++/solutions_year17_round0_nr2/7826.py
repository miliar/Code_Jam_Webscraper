#include <iostream>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <string>
#include <vector>
#include <iterator>

using namespace std;

int main(){

  int numberOfTrials;
  long long TEMP;
  cin >> numberOfTrials;
  vector<long long> INPUTS;
  for(int t = 0; t < numberOfTrials; t++){
    cin >> TEMP;
    INPUTS.push_back(TEMP);
  }

  for(int i = 0; i < numberOfTrials; i++){
    long long N = INPUTS[i];
    long long BACKUP = N;

    for(long long subtract = 0; subtract < N; subtract++){
      vector<int> digits;
      long long temporary = 0;
      long long testing = N-subtract;
      long long placeholder = testing;
      long long division = placeholder;
      long long counter = 0;

      while(placeholder != 0){
        division = placeholder%10;
        digits.push_back(division);
        placeholder = placeholder/10;
      }

      reverse(digits.begin(), digits.end());

      for(int q = digits.size()-1; q >= 0; q--){
        if(digits[q] >= digits[q-1] && q-1 >= 0){
          counter++;
          //cout << "counter: " << counter << endl;
        }
        else{
          if(q-1 >= 0){
            digits[q-1] = digits[q-1]-1;
            fill(digits.begin()+q, digits.end(), 9);
            N=0;
            for(int t = digits.size()-1; t >= 0; t--){
              N = N * (digits[t]*(pow(10,t)));
            }
            //cout << "DONE" << endl;
            subtract = 0;
            q=digits.size()-1;
          }
        }
      }

      cout << "Case #" << i+1 << ": ";

      for(int p = 0; p < digits.size(); p++){
        if(digits[p] != 0){
          cout << digits[p];
        }
      }
      cout << endl;
      break;
      /*if(counter == digits.size()-1){
        cout << "Case #" << i+1 << ": " << N << endl;
        break;
      }*/
    }
  }
  return 0;
}

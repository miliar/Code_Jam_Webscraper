#include <bits/stdc++.h>
#include <cstdlib>
using namespace std;

bool bad_pattern (string x){
     if (x.find("10") == string::npos){
          return false;
     }

     for (unsigned int iter = 0; iter != x.find("10"); iter++){
          if (x[iter] != '1'){
               return false;
          }
     }

     return true;
}


string set_digits (string q, int j, char c){
     for (int i = j; i < q.size(); i++){
          q[i] = c;
     }
     return q;
}

string answer_generator(string a){
     unsigned index;
     string answer;
     unsigned count = a.size();

     if (a.size() == 1){
          return a;
     }

     if (bad_pattern(a)){
          for (size_t i = 0; i < a.size() - 1; i++){
               answer.push_back('9');
          }

          return answer;
     }

     for (size_t i = 0; i < a.size(); i++) {
          answer.push_back('9');
     }

     char min_digit;

     if (a[0] != '1'){
          min_digit = a[0] - 1;
     }
     else
          min_digit = '1';

     for (size_t i = 0; i < a.size(); i++) {
          for (char c = min_digit; c <= '9'; c++){
               if (set_digits (answer, i, c) > a){
                    answer[i] = c - 1;
                    min_digit = c - 1;
                    break;
               }
          }
     }

     return answer;

}

int main(){

     unsigned int test_cases;
     cin >> test_cases;

     vector<string> input;

     for (size_t i = 0; i < test_cases; i++) {

          string number;
          cin >> number;
          input.push_back(number);
     }

     vector<string> output;

     for (size_t i = 0; i < test_cases; i++){
           output.push_back(answer_generator(input[i]));
     }

     for (size_t i = 0; i < test_cases; i++) {
          cout << "Case #" << i+1 << ":" << " " << output[i] << endl;
     }

     return 0;
}

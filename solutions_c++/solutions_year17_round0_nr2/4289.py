#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>
#include <cmath>

using namespace std;

bool is_nondecreasing(const string& num){
  for(int i = 0; i < num.size()-1; i++){
    if(num[i]>num[i+1]) return false;
  }
  return true;
}

int main(){
  unsigned long long int n;

  int t;
  cin >> t;

  int case_number = 1;

  while(t--){
    cin >> n;
    string number = to_string(n);
    string candidate(int(log10(n)),'9');
    string answ = number;

    bool have_to_fix = false;

    for(int i = 0; i < number.size()-1; i++){
      if(number[i]>number[i+1]){
        have_to_fix = true;
      }
    }

    if(have_to_fix){
      do{
        int j = 0;
        while(j < number.size() && number[j]<=number[j+1]){
          j++;
        }

        unsigned long long int tmp;
        stringstream strstream;


        strstream << number.substr(0,j+1);
        strstream >> tmp;
        tmp--;

        string new_string = (tmp!=0 ? to_string(tmp) : "");

        answ = new_string + candidate.substr(j);

        bool contains_zero = false;
        for(int i = 0; i < answ.size(); i++){
          if(answ[i] == '0'){
            contains_zero = true;
          }
        }
        if(contains_zero){
          answ = candidate;
        }
        number = answ;
      } while(!is_nondecreasing(answ));
    }
    cout << "Case #" << case_number << ": " << answ << endl;
    case_number++;
  }

  return 0;
}

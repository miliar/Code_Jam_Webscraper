#include "stove.h"
#include <iostream>
#include <string>

using namespace std;


int main(){
  int num_tests;
  string pcakes;
  int k;
  
  std::cin >> num_tests;

  for(int case_num = 1; case_num <= num_tests; case_num++){
    std::cin >> pcakes;
    std::cin >> k;

    Stove s(pcakes, k);
    int calc = s.Calculate();
    
    cout << "Case #" << case_num << ": ";
    if(calc == -1)
      cout << "IMPOSSIBLE";
    else
      cout << calc;
    cout << endl;
  
  }

  return 0;
}


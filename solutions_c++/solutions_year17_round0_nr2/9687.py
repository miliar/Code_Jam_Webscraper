#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>

int main() {
  std::string path("E:/nosave/codejam/");
  std::ifstream in (path + "B-small-attempt3.in" );
  std::ofstream out(path + "B-small-attempt3.out");
  unsigned int T = 0;
  in >> T;
  for (unsigned int test_case = 1; test_case <= T; test_case++) {
    //read
    unsigned long N = 0;
    in >> N;
    out << "Case #" << test_case << ": ";
    std::cout << "Case #" << test_case << std::endl;
    
    //main loop
    //for all digits from log(N) to 1 
    int maxDigit = (int)floor(log10(N));
 //   if(maxDigit) out << N << std::endl;
    std::vector<int> number(maxDigit+1);
    for (int i = maxDigit; i >= 0; --i) {
      number[i] = (int)floor(N / pow(10, i));
      N -= number[i] * pow(10, i);
    }

    for (int i = 0; i < maxDigit ;++i) {
      //look if there is a value bigger than
      bool needToChange = false;
      for (unsigned int j = i+1; j <= maxDigit ; ++j) {
        //look if there is a value bigger than 
        if (number[i] < number[j]) {
          needToChange = true;
          break;
        }
      }
      if (needToChange) {
        for (int k = 0; k <= i; k++) number[k] = 9;
        number[i + 1] -= 1;
      }
    }
    for (int i = number.size() - 1; i >= 0; --i) {
      N += number[i] * pow(10, i);
    }
    out << N << std::endl;
  }
  


  in.close();
  system("pause");
}
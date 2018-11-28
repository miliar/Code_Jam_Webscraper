#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

// #define NAT_DEBUG

// Function prototypes

int main(int argc, const char * argv[]){
  // Check flags
  if (argc<3){
    std::cout << "INPUT AND OUTPUT FLAGS REQUIRED!" << std::endl;
    exit(EXIT_FAILURE);
  }

  // Open in and out files
  std::ifstream fin(argv[1]);
  if(!fin.is_open()) {
    std::cout << "Unable to open input file: " << argv[1] << std::endl;
    exit(EXIT_FAILURE);
  }
  std::ofstream fout(argv[2]);

  // T tests
  int T;

  // temp string to read to
  std::string tempString;

  std::getline(fin, tempString);
  T = std::stoi(tempString);

  std::cout << T << " test cases following\n";

  for (int i = 0; i < T; i++){
    std::getline(fin, tempString);

    #ifdef NAT_DEBUG
    std::cout << "Case " << i << " is " << tempString << std::endl;
    #else
    std::cout << i << std::endl;
    #endif

    if (tempString.length() > 1) {
      int i;
      bool n_tidy = false;
      for(i = 0; i < tempString.length() - 1; i++) {
        if (tempString[i] > tempString[i+1]) {
          n_tidy = true;
          break;
        }
      }

      if (n_tidy) {
        if (tempString[i] > '1') {
          while (i > 0 && tempString[i] == tempString[i-1]) i--;
          tempString[i]--;
          for (int j = i+1; j < tempString.length(); j++) {
            tempString[j] = '9';
          }
        } else {
          tempString.erase(tempString.begin());
          for (int j = 0; j < tempString.length(); j++) {
            tempString[j] = '9';
          }
        }

      }

    }

    #ifdef NAT_DEBUG
    std::cout << "Case #" << i + 1 << ": " << tempString << std::endl;
    #endif

    fout << "Case #" << i + 1 << ": ";
    fout << tempString;
    // (C!=0)? fout << C*N : fout << "INSOMNIA";
    fout << std::endl;
  }

  // Cleanup
  fin.close();
  fout.close();

  return 0;
}

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>

// Function prototypes
void swap(std::string &s, int width, int index);

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
  int T,K;

  // temp string to read to
  std::string tempString;

  std::getline(fin, tempString);
  T = std::stoi(tempString);

  std::cout << T << " test cases following\n";

  for (int i = 0; i < T; i++){
    std::getline(fin, tempString);
    // N = std::stoi(tempString);
    std::cout << "Case " << i << " is " << tempString << std::endl;

    int j = 0;
    while (tempString[j++]!=' ');
    j--;
    K = std::stoi(tempString.substr(j, tempString.length()-1));
    tempString = tempString.substr(0,j);

    std::cout << K <<" "<<tempString<<std::endl;

    int count = 0;

    for (int a = 0; a <= tempString.length() - K; a++) {
      if (tempString[a] == '-') {
        swap(tempString, K, a);
        count++;
      }
    }

    bool all_ok = true;
    // check last K - 1
    for (int b = tempString.length() - K; b < tempString.length(); b++) {
      if (tempString[b] == '-') {
        all_ok = false;
        break;
      }
    }

    std::cout << tempString << '\n';


    fout << "Case #" << i + 1 << ": ";
    (all_ok)? fout << count : fout << "IMPOSSIBLE";
    fout << std::endl;
  }

  // Cleanup
  fin.close();
  fout.close();

  return 0;
}

void swap(std::string &s, int width, int index){
  for(int j = 0; j < width; j++) {
    if (s[index + j] == '+') s[index + j] = '-';
    else s[index + j] = '+';
  }
}

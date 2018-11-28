#include <iostream>
#include <fstream>
#include <set>
#include <string>
#include <vector>

int main() {
  std::string path("E:/nosave/codejam/");
  std::ifstream in (path + "A-large.in" );
  std::ofstream out(path + "A-large.out");
  unsigned int N = 0;
  in >> N;
  for (unsigned int test_case = 1; test_case <= N; test_case++) {
    //read
    std::string word;
    in >> word;
    unsigned int K = 0;
    in >> K;
    std::vector<bool> cakes(word.size());
    for (unsigned int i = 0; i < word.size(); ++i) {
      if (word[i] == '+') {
        cakes[i] = false;
      } else {
        cakes[i] = true;
      }
    }

    //main loop
    out << "Case #" << test_case << ": ";
    int result = 0;
    for (unsigned int i = 0; i <= cakes.size() - K;++i) {
      
      if (cakes[i] == false) {
        continue;
      }
      //flip bits from i to i+K
      result++;
      for (unsigned int j = i; j < i + K; ++j) {
        cakes[j] = cakes[j] ^ true;
      }
    }
    //check that all the bits from cakes.size() - K are 0
    for (unsigned int i = cakes.size() - K + 1; i < cakes.size(); ++i) {
      if (cakes[i]) {
        result = -1;
        break;
      }
    }

    if (result != -1) {
      out << result;
    } else {
      out << "IMPOSSIBLE";
    }
    out << std::endl;
  }
  


  in.close();
  system("pause");
}
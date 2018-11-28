#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <list>

using namespace std;

int main(int argc, char const *argv[]) {
  int T, k = 0;
  std::string N;

  std::cin >> T;
  getchar();

  for (int i = 0; i < T; i++) {

    getline(cin, N);

    k = N.size();
    for (std::string::iterator j = N.end()-1; j != N.begin(); j--) {

        if (N.size() == 1) {
          break;
        }
        if (*(j-1) > *j) {
          *(j-1) = *(j-1) - 1;
          for (std::string::iterator a = j; a != N.end(); a++) {
            *a = '9';
          }
        }
    }

    for (std::string::iterator j = N.begin(); j != N.end(); j--) {
      if (*j != '0') {
        break;
      }
      else{
        N.erase(j);
      }
    }

    std::cout << "Case #" << i+1 << ": "<< N << std::endl;

  }

  return 0;
}

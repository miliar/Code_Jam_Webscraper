#include <iostream>
#include <fstream>
#include <cassert>

int main(int argc, char *argv[]) {
  // std::ifstream ifs("a.txt");
  std::ifstream ifs(argv[1]);
  assert(ifs.is_open());
  int t;
  ifs >> t;
  std::string line;
  int size;
  int num=0;
  while (ifs >> line >> size) {
    num++;
    int ct=0;
    for (int i=0;i<line.length();i++) {
      // std::cout << i << ": " << line << "\n";
      if (line[i] == '-') {
        if (i + size > line.size()) {
          ct=-1;break;
        } else {
          ct++;
          for (int j=i;j<i+size;j++) {
            line[j] = line[j]=='+'?'-':'+';
          }
        }
      }
    }
    if (ct==-1) {
      std::cout << "Case #" << num << ": " << "IMPOSSIBLE"  << "\n";
    } else {
      std::cout << "Case #" << num << ": " << ct  << "\n";
    }
  }
}

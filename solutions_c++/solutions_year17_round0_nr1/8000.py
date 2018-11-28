#include <vector>
#include <fstream>
#include <iostream>
#include <cstdlib> // for exit()
#include <stdio.h>
#include <string>
#include <iterator>
#include <cassert>

int main()
{
  using namespace std;

  ifstream inf("A-large.in");
  ofstream outf("A-large.out");
  int T,S;
  inf >> T;
  std::string str;
  for (int i = 1; i <= T; ++i)
  {
    outf << "Case #" << i << ": ";

    inf >> str;
    inf >> S;

    int len = str.length();
    std::vector<bool> v(len);
    for (int j = 0; j < len; j++) {
      if (str[j] == '+') {
        v[j] = true;
      }
      cout << v[j];
    }
    cout << endl;

    int flips = 0;
    for (int j = 0; j < len-S+1; j++) {
      if (!v[j]) {
        flips++;
        for (int k = 0; k < S; k++) {
          v[j+k] = !v[j+k];
        }
      }
    }

    for (int j = 0; j < len; j++) {
      cout << v[j];
    }
    cout << endl;

    bool ispos = true;
    for (int j = len-S; j < len; j++) {
      if (!v[j]) {
        ispos = false;
      }
    }

    if (ispos) {
      outf << flips;
    } else {
      outf << "IMPOSSIBLE";
    }
    outf << endl;
  }
  return 0;
}

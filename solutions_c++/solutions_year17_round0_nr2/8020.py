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

  ifstream inf("B-large.in");
  ofstream outf("B-large.out");
  int T;

  inf >> T;
  std::string str;
  for (int i = 1; i <= T; ++i)
  {
    outf << "Case #" << i << ": ";

    inf >> str;

    int len = str.length();
    std::vector<int> v(len);
    for (int j = 0; j < len; j++) {
      v[j] = (int) str[j] - 48;
      //cout << v[j];
    }
    //cout << endl;

    int pos = -1;
    bool istidy = true;
    for (int j = 1; j < len; j++) {
      if(v[len-j-1] > v[len-j]) {
        istidy = false;
        pos = j;
        int k = j;
        v[len-j] = 9;
        v[len-j-1] -= 1;
        for (int k = 1; k < j; k++) {
          v[len-k] = 9;
        }
      }
    }
    //cout << istidy << " " << pos << endl;
    if (pos != len-1) {
      outf << v[0];
    } else {
      if (v[0] > 0)
      outf << v[0];
    }
    for (int j = 1; j < len; j++) {
      outf << v[j];
    }
    outf << endl;

    // for (int j = 0; j < len; j++) {
    //   cout << v[j];
    // }
    // cout << endl;
  }
  return 0;
}

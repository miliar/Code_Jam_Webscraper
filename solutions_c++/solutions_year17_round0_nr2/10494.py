#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

// need to only work with strings, and not ints for large data set...

bool tidyCheck(string number) {
  if (number.length() == 1) {
    return true;
  }
  for (int i=number.length()-1; i>0; --i) {
    if (number[i] - '0' < number[i-1] - '0') {
      return false;
    }
  }
  return true;
}

int main() {
  ifstream ifile("filename.txt");
  int cases;
  ifile >> cases;

  for (int i=0; i < cases; ++i) {
    int n;
    ifile >> n;
    int curr = n;
    while (curr > n/10) {
      if (tidyCheck(to_string(curr))) {
        cout << "Case #" << i+1 << ": " << curr << endl;
        break;
      } else {
        curr--;
      }
    }

  }

}

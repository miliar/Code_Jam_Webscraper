// Patrick Thompson
// Google Code Jam
// Tidy Numbers

#include <iostream>
#include <fstream>
using namespace std;

bool isTidy(long long num) {
  int last = num%10;
  num /= 10;
  while (num) {
    if (last < num%10)
      return false;
    last = num%10;
    num /= 10;
  }

  return true;
}

int main(void) {
  int num_cases, i, j;
  //char curr = '9';
  long long curr, max;
  string line;
  ifstream input;
  ofstream output;
  input.open("B-small-attempt0.in");
  output.open("out");
  input >> num_cases;
  //cout << num_cases << endl;

  for (i = 0; i < num_cases; i++) {
    input >> curr;
    //cout << curr << endl;
    for (j = 1; j <= curr; j++) {
      //cout << max << endl;
      if (isTidy(j))
        max = j;
    }
    output << "Case #" << (i+1) << ": " << max << endl;
  }

  input.close();
  output.close();
  return 0;
}

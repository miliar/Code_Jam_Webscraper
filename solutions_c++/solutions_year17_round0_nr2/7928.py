#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <map>
using namespace std;

bool isTidy( long number) {
  if (number < 10) return true;
  string nS = to_string(number);
  for (int j = 1; j < nS.size(); ++j) {
    if (nS[j] < nS[j-1]) return false;
  }
  return true;
}

size_t minDigitWhichCanBeDecremented(long number) {
  string nS = to_string(number);
  int digit;
  for (digit = 1; digit < nS.size(); ++digit) {
    if (nS[digit] < nS[digit-1]) {
      digit--;
      break;
    }
  }

  for (; digit > 0; --digit) {
    if (nS[digit] > nS[digit -1]) {
      return digit;
    }
  }
  return 0;
}

int main(int argc, char* argv[]) {
  string filename = argv[1];
  ifstream ifs(filename.c_str());
  string line,input;
  int k;
  getline(ifs,line);
  int numTests = atoi(line.c_str());
  for (int i=0;i<numTests;++i) {
    getline(ifs,line);
    long number;
    istringstream iss(line);
    iss >> number;
    if (isTidy(number)) {
      cout << "Case #" << i+1 << ": " << number << endl;
      continue;
    }
    size_t minDigit = minDigitWhichCanBeDecremented(number);
    string nS = to_string(number);
    size_t nsSize = nS.size();
    if (minDigit > 0 || (minDigit == 0 && nS[minDigit] != '1')) {
       int d = (int)(nS[minDigit]) - 1;
       nS[minDigit] = d;
       for (size_t digit = minDigit+1; digit < nS.size(); ++digit) {
         nS[digit] = '9';
       }
       cout << "Case #" << i+1 << ": " << nS << endl;
    } else {
      string nS = "";
      for (size_t digit = 0; digit < nsSize -1; ++digit) {
        nS += '9';
      }
      cout << "Case #" << i+1 << ": " << nS << endl;
    }
  }
}

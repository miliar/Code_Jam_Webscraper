#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <map>
using namespace std;

string solve(string input, int k) {
  if(input.find('-') == string::npos) {
    return "0";
  }
  int numTurns = 0;
  while (input.find('-') != string::npos) {

    size_t pos = input.find_first_of('-');
    if (pos > (input.size() - k)) {
      return "IMPOSSIBLE";
    }
    for (size_t i = pos; i < pos + k; ++i) {
      char c = input[i];
      char alternate = (c=='+')?'-':'+';
      input[i] = alternate;
    }
    numTurns++;
  }
  return to_string(numTurns);
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
    istringstream iss(line);
    iss >> input >> k;
    string result = solve(input, k);
    cout << "Case #" << i+1 << ": " << result << endl;
  }
}

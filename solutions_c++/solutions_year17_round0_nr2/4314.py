#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <limits>
#include <omp.h>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void help(void) { cout << "Need to pass file in argument" << endl; }

string process(string& caseLine);

int main(int argc, const char* argv[]) {
  if (argc != 2) {
    help();
    return 1;
  }

  ifstream dataFile;
  dataFile.open(argv[1]);

  int nbCase;
  dataFile >> nbCase;
  {
    string tmp;
    getline(dataFile, tmp); // finish line
  }

  // Vector that receive each line of the data file
  vector<string> lines;
  lines.reserve(nbCase);

  for (int i = 0; i < nbCase; i++) {
    string line;
    getline(dataFile, line);
    lines.emplace_back(line);
  }

  dataFile.close();

  // parallel process each case
  #pragma omp parallel for
  for (int i = 0; i < nbCase; i++) {
    lines[i] = process(lines[i]);
  }

  // print result
  for (int i = 0; i < nbCase; i++) {
    stringstream l(lines[i]);
    // remove leading 0
    long int val = stol(lines[i]) ;
    cout << "Case #" << i + 1 << ": " << val << endl;
  }

  return 0;
}

int digit(vector<char>& v, size_t i) { return (int)(v[i] - '0'); }
void decrement(vector<char>& v, size_t i) { v[i] = v[i] - 1; }

string process(string& caseLine) {
  vector<char> number(caseLine.begin(), caseLine.end());
  const auto numSize = number.size();

  int lastUp = 0;
  for (int i = 0; i < numSize - 1; i++) {
    int actualDig = digit(number, i);
    int nextDig = digit(number, i + 1);

    if (nextDig > actualDig) {
      lastUp = i+1;
    } else if (nextDig < actualDig) {
      decrement(number, lastUp);
      fill(number.begin() + lastUp + 1, number.end(), '9');
      break;
    }
  }

  string result(number.begin(), number.end());
  return result;
}

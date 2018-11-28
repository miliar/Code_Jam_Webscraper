#include <iostream>
#include <istream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cmath>
#include <iomanip>
using namespace std;

vector<string> inputarr;
int caseNumber;

vector<string> split(const string &s, const char* delim) {
  vector<string> itemarr;
  stringstream ss(s);
  string item;
  while (getline(ss, item, *delim)) {
    itemarr.push_back(item);
  }
  return itemarr;
}

vector<double> stringArrToDoubleArr(vector<string> stringarr) {
  vector<double> itemarr;
  vector<string>::iterator it = stringarr.begin();
  while (it != stringarr.end()) {
    itemarr.push_back(atof((*it).c_str()));
    it++;
  }
  return itemarr;
}

bool flip(string& s, int k, int i) {
  if (s.size() - i < k) {
    return false;
  }

  int maxIndex = i + k - 1;
  for (; i <= maxIndex; i++) {
      if (s[i] == '-')
        s[i] = '+';
      else
        s[i] = '-';
  }
  return true;
}

void solveProblem(ofstream& ofstream) {
  string s = inputarr[0];
  int k = atoi(inputarr[1].c_str());

  ofstream << "Case #" << caseNumber << ": ";

  int numFlip = 0;
  for (int i = 0; i < s.size(); i++) {
    if (s[i] == '-') {
      if (!flip(s, k, i)) {
        ofstream << "IMPOSSIBLE\n";
        return;
      }
      numFlip++;
    }
  }

  ofstream << numFlip << "\n";
}


int main () {
  ofstream resultfile;
  ifstream inputfile;
  inputfile.open ("input.txt");
  resultfile.open ("result.txt");

  string line;
  getline (inputfile, line);

  while (getline (inputfile, line)) {
    caseNumber++;
    inputarr = split(line, " ");
    
    solveProblem(resultfile);
    continue;
  }

  inputfile.close();
  resultfile.close();
  return 0;
}
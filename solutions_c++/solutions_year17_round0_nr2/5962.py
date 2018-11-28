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

void solveProblem(ofstream& ofstream) {
  string s = inputarr[0];

  ofstream << "Case #" << caseNumber << ": ";

  bool setRest = false;
  for (int i = 0; i < s.size(); i++) {
    if (setRest) {
      s[i] = '9';
    }
    else if (i < s.size() - 1) {
      int thisDig = s[i] - '0';
      int nextDig = s[i+1] - '0'; 
      if (thisDig > nextDig) {
        s[i] = to_string(thisDig - 1)[0];

        if (i > 0 && thisDig - 1 < s[i - 1] - '0')
          i -= 2;
        else
          setRest = true;
      }
    }
    //cout << "i " << i << ", s " << s << "\n";
  }

  ofstream << (s.size() > 1 && s[0] == '0' ? s.substr(1) : s) << "\n";
}

int main () {
  ofstream resultfile;
  ifstream inputfile;
  inputfile.open ("input.txt");
  resultfile.open ("result.txt");

  string line;
  getline (inputfile, line);
  while (getline (inputfile, line)) {
    inputarr = split(line, " ");
    caseNumber++;
    solveProblem(resultfile);
    continue;
  }

  inputfile.close();
  resultfile.close();
  return 0;
}
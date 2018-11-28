#include <iostream>
#include <fstream>
#include <list>
#include <string>

#include "stdlib.h"

using namespace std;

typedef struct {
  string pans;
  int flipperSize;
} Pan;

typedef struct {
  int T;
  list<Pan> pans;
} Data;

void read_data(char *fileName, Data &data) {
  ifstream stream(fileName);
  if(!stream.is_open()) {
    cerr << "error opening file" << endl;
    exit(1);
  }

  string str;
  getline(stream, str);
  data.T = stoi(str);

  Pan pan;
  for(int i=0; i<data.T; i++) {
    getline(stream, str);
    int spaceIdx = str.find(' ');
    string pans = str.substr(0, spaceIdx);
    string flipperSize = str.substr(spaceIdx+1);
    pan.pans = pans;
    pan.flipperSize = stoi(flipperSize);
    data.pans.push_back(pan);
  }
}

int main(int argc, char ** argv) {
  Data data;

  if(argc != 2) {
    cerr << "file path missing" << endl;
    exit (1);
  }

  // cout << "Reading file" << endl;
  read_data(argv[1], data);
  // cout << "File OK" << endl;

  unsigned int caseNr=1;

  for (list<Pan>::iterator itList=data.pans.begin(); itList != data.pans.end(); ++itList) {
    Pan &pan = *itList;
    int cur = pan.pans.size() - 1;
    bool res = true;
    int flipNr = 0;

    while (cur >= (pan.flipperSize-1)) {
      if (pan.pans[cur] == '-') {
        flipNr++;
        for (int j=0; j<pan.flipperSize; j++) {
          if (pan.pans[cur-j] == '-') {
            pan.pans[cur-j] = '+';
          } else {
            pan.pans[cur-j] = '-';
          }
        }
      }

      // cout <<  "--> " << pan.pans << endl;
      cur--;
    }

    for (; cur >=0; cur--) {
      if(pan.pans[cur] == '-') {
        res = false;
      }
    }

    if(! res) {
      cout <<  "Case #" << caseNr << ": IMPOSSIBLE" << endl;
    } else {
      cout <<  "Case #" << caseNr << ": " << flipNr << endl;
    }

    caseNr++;
  }

}


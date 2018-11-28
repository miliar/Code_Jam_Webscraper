#include <iostream>
#include <fstream>
#include <list>
#include <string>

#include "stdlib.h"

using namespace std;

typedef struct {
  int T;
  list<string> S;
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

  for(int i=0; i<data.T; i++) {
    getline(stream, str);
    data.S.push_back(str);
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

  for (list<string>::iterator itList=data.S.begin(); itList != data.S.end(); ++itList) {

    // cout << "Starting case " << caseNr << ": " << *itList << endl;
    unsigned int cur=1;
    while (cur < (*itList).size() && (*itList)[cur-1] <= (*itList)[cur]) {
      cur++;
    }

    // cout << "Stopping at " << cur << endl;

    if(cur < (*itList).size()) {
      // cout <<  "Going backward " << endl;
      while (cur>0 && (*itList)[cur-1] > (*itList)[cur]) {
        // cout <<  "cur is " << cur << endl;
        // (*itList)[cur-1] = (*itList)[cur];
        (*itList)[cur-1]--;
        cur--;
      }

      cur++;
      // cout <<  "Setting 9s from " << cur << endl;
      for (;cur < (*itList).size(); cur++) {
        (*itList)[cur] = '9';
      }

      // cout <<  "Removing leading 0s " << endl;
      while((*itList)[0] == '0') {
        (*itList).erase(0, 1);
      }
    }

    cout <<  "Case #" << caseNr << ": " << *itList << endl;
    caseNr++;
  }

}


#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#include <assert.h>
#include <queue>
#include <sstream>
#include <iomanip>
#include <algorithm>

using namespace std;

bool debug=false;

#define DEBUG if (debug) cout

//ostream& operator<<(ostream& o, const Omino& oo) {
//  for (int y=0; y<oo[0].size(); ++y) {
//    for (int x=0; x<oo.size(); ++x) {
//      o << oo[x][y] << " ";
//    }
//    o << endl;
//  }
//
//  return o;
//}

string N,P;

string int2string(long int i) 
{
  stringstream s;
  s << i;

  return s.str();
}

long int string2int(const string& s)
{
  assert(s.find("@") == string::npos);

  long int i;
  stringstream ss(s);
  ss >> i;

  assert(int2string(i) == s);

  return i;
}

string solve()
{
  string s = N;

  for (int i=s.size()-1; i>0; --i) {
    if (s[i] < s[i-1]) {
      if (s[i-1] == '0') return P;
      s[i-1] = s[i-1] - 1;
      for (int j=i; j<s.size(); ++j)
        s[j] = '9';
    }
  }

  while (s[0] == '0') s = s.substr(1);

  return s;
}


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;

  DEBUG << "  numCases: " << numCases << endl;
  
  for (int c=0; c<numCases; ++c) {
    i >> N;
    
    if (N.size() == 1) {
      cout << "Case #" << c+1 << ": " << N << endl;
      continue;
    }

    P.clear();
    for (int j=0; j<N.size()-1; ++j) P += "9";

    cout << "Case #" << c+1 << ": " << solve() << endl;
  }

  return true;
}



int main(int argv, char* argc[])
{
  if (argv < 2) {
    cout << "Usage " << argc[0] << " <inputFile>" << endl;
    exit(1);
  }

  ifstream filei(argc[1]);

  readFile(filei);

  return 0;
}

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
#include <bitset>

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

#define MaxSize 1000

bitset<MaxSize> a;

vector<bool> aa;

int K;
int N;

bool operator<(const std::bitset<MaxSize>& x, const std::bitset<MaxSize>& y)
{
    for (int i = N-1; i >= 0; i--) {
        if (x[i] ^ y[i]) return y[i];
    }
    return false;
    }

ostream& operator<<(ostream& o, const vector<bool>& b)
{
  for (bool bb: b) o << bb;
  return o;
}


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

int solve()
{
  //  set<bitset<MaxSize>> visited;
  set<vector<bool>> visited;

  //  typedef pair<int, bitset<MaxSize>> P;
  typedef pair<int, vector<bool>> P;
  queue<P> q;

  q.push(make_pair(0, aa));

  while (!q.empty()) {
    P p = q.front();
    q.pop();

    DEBUG << "EXPANDING " << p.first << " " << p.second << endl;

    bool done=true;
    for (int j=0; j<N; ++j) {
      if (!p.second[j]) { done = false; break; }
    }

    if (done) return p.first;

    if (visited.find(p.second) != visited.end()) continue;
    visited.insert(p.second);

    for (int k=0; k<=N-K; ++k) {
      //      bitset<MaxSize> b = p.second;
      vector<bool> b = p.second;

      for (int j=0; j<K; ++j)
        b[k+j] = !b[k+j];

      if (visited.find(b) == visited.end()) {
        q.push(make_pair(p.first+1, b));
        DEBUG << "OPENNING " << p.first+1 << " " << b << endl;
      }
    }
  }
  
  return -1;
}


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;

  DEBUG << "  numCases: " << numCases << endl;
  
  for (int c=0; c<numCases; ++c) {
    string s;
    i >> s >> K;
    N = s.size();

    aa.clear();

    for (int j=0; j<s.size(); ++j) {
      assert(s[j] == '-' || s[j] == '+');
      //      a[j] = (s[j] == '+');
      aa.push_back((s[j] == '+'));
    }
    //    for (int j=s.size(); j<MaxSize; ++j)
    //      a[j] = false;

    int m = solve();
    if (m==-1)
      cout << "Case #" << c+1 << ": IMPOSSIBLE" << endl;
    else
      cout << "Case #" << c+1 << ": " << m << endl;
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

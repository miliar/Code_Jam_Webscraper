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

long long int N,K;

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

pair<int,int> solve()
{
  typedef pair<int,int> P;
  queue<P> q;
  vector<P> tmp;

  DEBUG << "K=" << K << endl;

  q.push(make_pair(0, N-1));
  for (int k=0; k<K; ++k) {
    if (q.empty()) {
      sort(tmp.begin(), tmp.end(), [](const P& p1, const P& p2) { return (p1.second-p1.first) > (p2.second-p2.first);});
      for (const P& p: tmp) q.push(p);
      tmp.clear();
    }

    assert(!q.empty());
    P p = q.front();
    q.pop();
    
    assert(p.first <= p.second);
    if (p.first == p.second) continue;

    int center = (p.first+p.second)/2;

    DEBUG << "k: " << k << " c: " << center << endl;

    if (k<K-1) {
      if (center+1 <= p.second) tmp.push_back(make_pair(center+1, p.second));
      if (p.first <= center-1)  tmp.push_back(make_pair(p.first, center-1));
    } else {
      int left = center-p.first;
      int right = p.second-center;

      return make_pair(max(left,right),min(left,right));
    }
  }

  return make_pair(0,0);
}


bool readFile(ifstream& i)
{
  int numCases;
  i >> numCases;

  DEBUG << "  numCases: " << numCases << endl;
  
  for (int c=0; c<numCases; ++c) {
    i >> N >> K;
    
    auto p = solve();
    
    cout << "Case #" << c+1 << ": " << p.first << " " << p.second << endl;
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

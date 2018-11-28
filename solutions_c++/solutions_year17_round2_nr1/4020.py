#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>
using namespace std;

typedef unsigned char uc;
typedef unsigned int  ui;
typedef unsigned long ul;
typedef unsigned long long ull;

template <class T>
void print_out(int l, T ret) {
  cout.precision(10);
  cout << "Case #" << l << ": " << fixed << ret << endl;
}

double gett(pair<int,int>& p) {
  return (double(p.first)/p.second);
}

int main(void) {
  int T; cin >> T; cin.ignore();
  for (int l = 1; l <= T; ++l) {
    /* DO PROBLEM STUFF HERE --> */
    
    // D target pos [km]
    int D, N; cin >> D >> N; cin.ignore();
    vector<pair<int,int> > horses;
    for (int i = 0; i <N ; ++i) {
      // K initial horse position [km], S speed [kmh]
      int K, S; cin>>K>>S; cin.ignore();
      horses.push_back(make_pair((D-K),S));
    }
    sort(horses.begin(), horses.end());
    
    double totalhours = gett(horses[horses.size()-1]);
    
    if (horses.size() > 1) {
      for (int i = horses.size()-2; i >= 0; --i) {
        if (gett(horses[i]) <= gett(horses[i+1])) {
          //collision, they merge
        }
        else {
          totalhours = gett(horses[i]);
        }
      }
    
    }
    
    print_out(l, (double)(D/totalhours));
    
    /* <-- DO PROBLEM STUFF HERE */
  }
  return 0;
}




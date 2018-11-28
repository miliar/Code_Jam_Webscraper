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
  cout << "Case #" << l << ": " << ret << endl;
}

int main(void) {
  int T; cin >> T; cin.ignore();
  for (int l = 1; l <= T; ++l) {
    /* DO PROBLEM STUFF HERE --> */
    int Ac, Aj; cin >> Ac >> Aj;
    
    int Crem = 720;
    int Jrem = 720;

    set< pair<pair<int,int>, char> > ranges;
    
    for (int i = 0; i < Ac; ++i) {
      int C, D; cin >> C >> D;
      Jrem -= (D-C);
      ranges.insert(make_pair(make_pair(C,D), 'J'));//Jamie protects the baby
    }
    for (int i = 0; i < Aj; ++i) {
      int C, D; cin >> C >> D;
      Crem -= (D-C);
      ranges.insert(make_pair(make_pair(C,D), 'C'));
    }
    
    if ((Ac == 0 && Aj == 1) || (Ac == 1 && Aj == 0)) {
      print_out(l, 2);
    }
    else if ((Ac == 1 && Aj == 1)) {
      print_out(l, 2);
    }
    else if ((Ac == 2 && Aj == 0) || (Ac == 0 && Aj == 2)) {
      int b = ranges.begin()->first.first;
      int e = (++ranges.begin())->first.second;
      
      int e2 = ranges.begin()->first.second;
      int b2 = (++ranges.begin())->first.first;
      
      if ((e-b) <= 720 || (e2+1440-b2) <= 720) {
        print_out(l, 2);
      }
      else {
        print_out(l, 4);
      }
    }
    else {
      print_out(l, 0);
    }
    
    /* <-- DO PROBLEM STUFF HERE */
  }
  return 0;
}




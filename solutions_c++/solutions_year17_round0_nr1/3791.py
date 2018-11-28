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

template <class T>
void print_out(int l, T ret) {
  cout << "Case #" << l << ": " << ret << endl;
}

int main(void) {
  int T; cin >> T; cin.ignore();
  for (int l = 1; l <= T; ++l) {
    string S; int K;
    cin >> S >> K; cin.ignore();
    
    /* DO PROBLEM STUFF HERE --> */
    int ret = 0;
    for (ui i = 0; i <= S.size()-K; ++i) {
      if (S.at(i) == '-') {
        for (ui j = i; j < i+K; ++j) {
          if (S.at(j) == '+') {
            S.at(j) = '-';
          }
          else {
            S.at(j) = '+';
          }
        }
        ++ret;
      }
    }
    
    if (S != string(S.size(), '+')) {
      print_out(l, "IMPOSSIBLE");
    }
    else {
      print_out(l, ret);
    }
    
    /* <-- DO PROBLEM STUFF HERE */
  }
  return 0;
}




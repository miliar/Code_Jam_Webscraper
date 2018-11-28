#include <iostream>
#include <sstream>
#include <algorithm>
#include <bitset>
#include <complex>
#include <exception>
#include <initializer_list>
#include <locale>
#include <tuple>
#include <typeinfo>
#include <type_traits>
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

void output(int t, vector<string> res) {
  cout << "Case #" << t + 1<< ": " << endl;
  for (int i=0; i < res.size(); i++) {
    cout << res[i] << endl;
  }
}

void output(int t, unsigned long long res) {
  cout << "Case #" << t + 1<< ": " << res << endl;
}

int main() {
  int t;
  cin >> t;
  for (int tt = 0; tt < t; tt++) {
    int r, c;
    cin >> r >> c;
    vector<string> res;
    for (int rr = 0; rr < r; rr++) {
      string tmp;
      cin >> tmp;
      int i=0;
      while (i< tmp.length()) {
        int j = i;
        while(tmp[j] == '?' && j < tmp.length()) j++;
        if (j<tmp.length()) {
          for (int k=i; k<j; k++) {
            tmp[k] = tmp[j];
          }
        } else if (i != 0) {
          for (int k=i; k<j; k++) {
            tmp[k] = tmp[i-1];
          }
        }
        while(tmp[j] != '?' && j < tmp.length()) j++;
        i=j;
      }
      res.push_back(tmp);
    }
    int i = 0;
    while (i< res.size()) {
      int j = i;
      while(res[j][0] == '?' && j < res.size()) j++;
      if (j<res.size()) {
        for (int k=i; k<j; k++) {
          res[k] = res[j];
        }
      } else if (i != 0) {
        for (int k=i; k<j; k++) {
          res[k] = res[i-1];
        }
      }
      while(res[j][0] != '?' && j < res.size()) j++;
      i=j;
    }
    output(tt, res);
  }
  return 0;
}

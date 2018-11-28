#include <iostream>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <cstdlib>
#include <cassert>
#include <sstream>

using namespace std;

bool isCorrect(string n) {
  for(int i=0;i<n.length()-1;i++) {
    if(n[i]>n[i+1]) {
      return false;
    }
  }
  return true;
}

int solve(int n) {
  int m = 1;
  for(int i=1;i<=n;i++) {
    string si;
    stringstream ss;
    ss << i;
    ss >> si;
    if(isCorrect(si)) {
      m = i;
    }
  }
  return m;
}

int main() {
  int T;
  cin >> T;
  for(int t=1;t<=T;t++) {
    int n;
    cin >> n;
    int r = solve(n);
    cout << "Case #" << t << ": " << r << endl;
  }
  return 0;
}
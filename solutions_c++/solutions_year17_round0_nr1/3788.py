#include <iostream>
#include <string>
using namespace std;
string s;

bool flip(int j, int k) {
  bool a = true;
  for(int i = j; i<j+k; i++) {
    if(s[i] == '-') {
      s[i] = '+';
    }
    else {
      s[i] = '-';
      a = false;
    }
      
  }
  return a;
}


int main() {
  int t, k, n;
  bool ord;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    n=0;
    ord = true;
    cin >> s >> k;
    int size = s.size();
    for(int j = 0; j < size; j++) {
      if(s[j] == '-') {
        if(size-j >= k) {
          ord = flip(j,k);
          n++;
        }
        else {
          ord = false;
        }
      }
    }
    if(ord) {
      cout << "Case #" << i << ": " << n << endl; 
    }
    else {
      cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
#include <iostream>

using namespace std;


void test() {
  string n;
  cin >> n;
  
  // special case: 1(...)10gsgdadsfj
  {
    int i = 0;
    while(i < n.length() and n[i] == '1') i++;
    if(i < n.length() and n[i] == '0') {
      for(int j = 0; j < n.length() - 1; j++) {
        cout << '9';
      }
      cout << '\n';
      return;
    }
  }
  
  for(int i = 1; i < n.length(); i++) {
    if(n[i] < n[i-1]) {
      // fix prefix
      char t = n[i - 1];
      int j1 = i - 1, j0 = j1;
      while(j0 >= 0 and n[j0] == t) {
        j0--;
      }
      j0++;
      // j0..j1 is an equal range
      
      n[j0]--; // decrease it's first digit
      
      // put nines to others
      for(int j = j0 + 1; j < n.length(); j++) {
        n[j] = '9';
      }
      
      break;
    }
  }
  
  cout << n << '\n';
}


int main() {
  int t;
  cin >> t;
  
  for(int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    test();
  } 
  
  return 0;
}

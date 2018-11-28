#include <bits/stdc++.h>

using namespace std;

bool tidy(int x) {
  int last_digit = 9;
  while(x) {
    int d = x % 10;
    x /= 10;
    if(d > last_digit) {
      return false;
    } else {
      last_digit = d;
    }
  }
  return true;
}

int main(){
  int casos, n;
  cin >> casos;
  for(int caso = 1 ; caso <= casos; caso++) {
    cin >> n;
    while(!tidy(n)) {
      n--;
    }
    cout << "Case #" << caso << ": " << n << endl;
  }
  return 0;
}
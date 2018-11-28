#include <iostream>
using namespace std;

int main() {
  long long t, n, k, w, p;
  cin >> t;
  for(int nr = 1; nr <= t; nr ++) {
    cin >> n;
    k = 9;
    w = n % 10;
    n /= 10;
    p = 1;
    
    while(n) {
      if(n % 10 > w / p) {
        p *= 10;
        w = k + (n % 10 - 1) * p;
      } else {
        p *=10;
        w = w + (n % 10) * p;
      }
      k += 9 * p;
      n /= 10;
    }
    cout << "Case #" << nr <<": " << w << endl;
  }
  
}

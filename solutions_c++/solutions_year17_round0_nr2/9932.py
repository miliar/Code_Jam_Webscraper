#include <vector>
#include <iostream>
using namespace std;

typedef long long int LLI;


int istidy(LLI x) {
  LLI y;
  LLI r, lastr;

  lastr = 10;
  for (y = x; y > 0; y /= 10) {
    r = y % 10;
    if (r > lastr) {
      return 0;
    }
    lastr = r;
  }
  return 1;
}

LLI trytidy(LLI x, LLI pos) {
  x -= (x % pos);
  x -= 1;
  return x;
}


int main(void) {
  //  LLI x = 987654321;
  int T, t;
  LLI b, x;
  cin >> T;
  for (t = 1; t <= T; t++) {
    cin >> x;
    b = 10;
    while (!istidy(x)) {
      x = trytidy(x, b);
      b *= 10;
    }
    cout << "Case #" << t << ": " << x << endl;
  }
  return 0;
}

  
  

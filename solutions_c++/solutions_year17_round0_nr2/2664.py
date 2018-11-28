#include <iostream>
using namespace std;
int T;
long long N;

int main(int argc, char** argv) {
  cin >> T;
  cerr << sizeof(N) << endl;

  for (int t = 0; t < T; ++t) {
    cin >> N;
    char b[32];
    for (int i = 0; i < 32; ++i) b[i] = '0';

    for (int i = 0; N > 0; N /= 10) {
      b[i++] = '0' + N % 10;
    }

    for (int i = 0; i < 32; ++i) cerr << (char)b[i];
    cerr << endl;

    for (int j = 0; j < 31; ++j) {
      if (b[j] < b[j+1]) {
        b[j+1]--;
        for (int k = 0; k <= j; ++k)
          b[k] = '9';
      }
    }

    cout << "Case #" << (t + 1) << ": ";
    bool p = false;
    for (int i = 31; i >= 0; --i) {
      p = p || (b[i] != '0');
      if (p) cout << (char)b[i];
    }
    cout << endl;
  }
  return 0;
}

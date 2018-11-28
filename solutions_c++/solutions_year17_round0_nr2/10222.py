#include <iostream>
#include <vector>

using namespace std;

bool isTidy(long long n) {
  long long aux = n;
  int rem = aux % 10;
  while (aux > 0) {
    if (rem >= aux % 10) {
      rem = aux % 10;
      aux /= 10;
    }
    else
      return false;
  }
  return true;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    long long N;
    cin >> N;
    while (!isTidy(N)){
      N--;
    }
    cout << "Case #" << i+1 << ": " << N << endl;
  }
  return 0;
}

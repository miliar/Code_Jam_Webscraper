#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <numeric>
using namespace std;

bool check(int T) {
  int last = 9;
  while (T) {
    if (T%10 > last) return false;
    last = T % 10;
    T /= 10;
  }
  return true;
}
int main() {
    int caseN = 0;
    int last = 0;
    int valid[2000];
    for (int i = 0; i <= 1000; i ++) {
      if (check(i)) {
        last = i;
      }
      valid[i] = last;
    }
    cin >> caseN;
    for (int tcas = 1; tcas <= caseN; ++tcas) {
      int N;
      cin >> N;
      cout << "Case #" << tcas << ": " << valid[N] << endl;
    }

}

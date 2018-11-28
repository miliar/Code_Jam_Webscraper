#include <iostream>
#include <fstream>
using namespace std;

int T;
unsigned long long N, K, lefts, rights, num;
long long val, mins, maxs;

int main() {
  ifstream fin("C-large.in");
  ofstream fout("C-large.out");
  fin >> T;
  for (int t = 1 ; t <= T ; t++) {
    fin >> N >> K;
    lefts = 1;
    rights = 0;
    num = 1;
    val = N;
    while (num <= K / 2) {
      num *= 2;
      if (val % 2 == 1) {
        lefts = lefts * 2 + rights;
      } else {
        rights = lefts + rights * 2;
      }
      val = (val - 1) / 2;
    }

    if (K - num < rights) {
      maxs = (val + 1) / 2;
      mins = val / 2;
    } else {
      maxs = val / 2;
      mins = (val - 1) / 2;
    }

    fout << "Case #" << t << ": " << maxs << " " << mins << endl;
  }
  return 0;
}
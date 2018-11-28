#include <iostream>
#include <fstream>
using namespace std;

int T, K, flips, amount[1005], amnt;
bool possible;
string S;

int main() {
  ifstream fin("A-large.in");
  ofstream fout("A-large.out");
  fin >> T;
  for (int t = 1 ; t <= T ; t++) {
    fin >> S >> K;
    flips = amnt = 0;
    possible = true;
    for (int i = 0 ; i < S.length() ; i++) {
      amount[i] = 0;
    }
    for (int i = 0 ; i < S.length() && possible ; i++) {
      amnt += (S[i] == '-') ? 1 : 0;
      amnt += amount[i];
      if (amnt % 2 == 1) {
        if (i <= S.length() - K) {
          flips++;
          amnt++;
          amount[i+K] = -1;
        } else {
          possible = false;
        }
      }
      amnt -= (S[i] == '-') ? 1 : 0;
    }
    if (possible) {
      fout << "Case #" << t << ": " << flips << endl;
    } else {
      fout << "Case #" << t << ": IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
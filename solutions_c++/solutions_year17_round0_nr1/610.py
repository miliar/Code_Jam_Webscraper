#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define ll long long
#define pii pair<int,int>

int N,T,K;

ifstream fin("A.in");
ofstream fout("A.out");

int main() {
  fin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cout << "Working on Case #" << tt << "\n";
    string input;
    fin >> input >> K;
    N = input.length();
    int ans = 0;
    for (int i = 0; i <= N-K; i++) {
      if (input[i] == '-') {
        ans++;
        for (int j = 0; j < K; j++) {
          if (input[i+j] == '-') input[i+j] = '+';
          else input[i+j] = '-';
        }
      }
    }
    bool flag = true;
    for (int i = 0; i < N; i++) {
      if (input[i] == '-') flag = false;
    }
    fout << "Case #" << tt << ": ";
    if (flag) fout << ans << "\n";
    else fout << "IMPOSSIBLE\n";
  }
  return 0;
}
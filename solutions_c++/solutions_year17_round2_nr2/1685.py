#include <iostream>
#include <inttypes.h>

#include <string>
#include <vector>
#include <map>
#include <set>

#include <cmath>
#include <algorithm>

#include <cassert>

using namespace std;

bool Compare(const pair<char, int>& a, pair<char, int>& b) { return a.second >= b.second; }

bool ok(char a, char b) { return a ^ b; }

void prt(const string& S) {
  for (int j = 0; j < S.size(); ++j)
    cout << (S[j] == 0x01 ? "R" : S[j] == 0x02 ? "Y" : S[j] == 0x04 ? "B" :
             S[j] == 0x05 ? "V" : S[j] == 0x03 ? "O" : S[j] == 0x06 ? "G" : "?");
}

bool print(string& S, int N, vector<pair<char, int> > D, int n) {
  //cout << n << " --> "; prt(S); cout << endl;
  if (n == N) {
    if (!ok(S[N - 1], S[0])) return false;
    prt(S); return true;
  }
  sort(D.begin(), D.end(), Compare);
  for (int i = 0; i < D.size(); ++i) {
    if (D[i].second) {
      D[i].second -= 1;
      S[n] = D[i].first;
      if ((n == 0 || ok(S[n], S[n - 1])) && print(S, N, D, 1 + n)) return true;
      S[n] = 0;
      D[i].second += 1;
    }
  }
  return false;
}

void solve(int N, int R, int O, int Y, int G, int B, int V) {
  if (V > Y) { cout << "IMPOSSIBLE"; return; }
  if (O > B) { cout << "IMPOSSIBLE"; return; }
  if (G > R) { cout << "IMPOSSIBLE"; return; }
  if (R > (Y + B + G)) { cout << "IMPOSSIBLE"; return; }
  if (Y > (R + B + V)) { cout << "IMPOSSIBLE"; return; }
  if (B > (R + Y + O)) { cout << "IMPOSSIBLE"; return; }
  string S(N, 0);
  vector<pair<char, int> > D;
  D.push_back(make_pair(0x01, R));
  D.push_back(make_pair(0x02, Y));
  D.push_back(make_pair(0x04, B));
  D.push_back(make_pair(0x05, V));
  D.push_back(make_pair(0x03, O));
  D.push_back(make_pair(0x06, G));
  bool res = print(S, N, D, 0); assert (res);
}

int main() {
  int T; cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N, R, O, Y, G, B, V; cin >> N >> R >> O >> Y >> G >> B >> V;
    cout << "Case #" << i << ": "; solve(N, R, O, Y, G, B, V); cout << endl;
  }
  return 0;
}

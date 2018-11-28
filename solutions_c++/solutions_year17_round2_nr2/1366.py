#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

struct horse {
  int c;
  string l;

  horse(int cc, string ll) : c(cc), l(ll) {}
  horse(const horse&) = default;

  bool operator<(const horse& hh) const { return c < hh.c; }
};

bool check(string s) {
  if (s[0] == s[s.size()-1])
    return false;
  for (int i = 1; i < s.size(); ++i) {
    if (s[i-1] == s[i] || s[i] == '_')
      return false;
  }
  return true;
}

string tryy(vector<horse> hh, int N, int step) {
  string s(N, '_');
 

  for (int i = 0; i < N; i += step) {
    if (hh[0].c > 0) {
      s[i] = hh[0].l[0];
      hh[0].c--;
    }
  }

  for (int i = 0; i < N; ++i) {
    if (s[i] == '_') {

      if (hh[1].c > hh[2].c && s[i-1] != hh[1].l[0]) {
        s[i] = hh[1].l[0];
        hh[1].c--;
      } else if (hh[2].c > 0) {
        s[i] = hh[2].l[0];
        hh[2].c--;
      }
    }
  }

  return s;
}

string doit() {
  int N;
  cin >> N;
  int R, O, Y, G, B, V;

  cin >> R >> O >> Y >> G >> B >> V;

  vector<horse> hh{horse(R, "R"), horse(Y, "Y"), horse(B, "B")};
 
  sort(hh.rbegin(), hh.rend());

  string s = tryy(hh, N, 2);

  
  if (s.size() == N && check(s))
    return s;

  s = tryy(hh, N, 3);

  return s.size() == N && check(s) ? s : "IMPOSSIBLE";
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
    cout << "Case #"<<t<<": " << doit() <<endl;
}

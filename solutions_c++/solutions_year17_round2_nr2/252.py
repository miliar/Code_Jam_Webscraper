#include <bits/stdc++.h>

using namespace std;

void output(pair <int, char> &x, string &s) {
  s += x.second;
  x.first--;
}

bool generate(int B, int R, int Y, string &s) {
  vector <pair <int, char> > now = {{R, 'R'}, {B, 'B'}, {Y, 'Y'}};
  sort(now.begin(), now.end());
  reverse(now.begin(), now.end());

  if (now[0].first - now[1].first - now[2].first >= 1) {
    return false;
  } else {
    while (now[1].first > now[2].first) {
      output(now[0], s);
      output(now[1], s);
    }
    int sw = 1;

    while (now[0].first > 0) {
      output(now[0], s);

      if (now[sw].first > 0) {
        output(now[sw], s);
      }
      sw = 3 - sw;
    }

    while (now[1].first > 0 || now[2].first > 0) {
      output(now[sw], s);
      sw = 3 - sw;
    }
    return true;
  }
}

void replace(string &s, char c, string t) {
  if (s.find(c) == string::npos) {
    return;
  }
  int pos = int(s.find(c));
  s.erase(s.begin() + pos);
  s.insert(s.begin() + pos, t.begin(), t.end());
}

string genelem(int n, char one, char two, bool par = true) {
  string res = "";

  for (int i = 0; i < n; i++) {
    res += one;
    res += two;
  }
  if (par) {
    res += one;
  }
  return res;
}

int main() {
  int T;
  cin >> T;

  for (int tst = 0; tst < T; tst++) {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    cout << "Case #" << tst + 1 << ": ";

    if ((O > 0 && O >= B) || (G > 0 && G >= R) || (V > 0 && V >= Y)) {
      if (O + B == N && O == B) {
        cout << genelem(O, 'B', 'O', false) << '\n';
      } else if (G + R == N && G == R) {
        cout << genelem(G, 'R', 'G', false) << '\n';
      } else if (V + Y == N && V == Y) {
        cout << genelem(V, 'Y', 'V', false) << '\n';
      } else {
        cout << "IMPOSSIBLE\n";
      }
    } else {
      string s;

      if (!generate(B - O, R - G, Y - V, s)) {
        cout << "IMPOSSIBLE\n";
      } else {
        replace(s, 'B', genelem(O, 'B', 'O'));
        replace(s, 'R', genelem(G, 'R', 'G'));
        replace(s, 'Y', genelem(V, 'Y', 'V'));
        cout << s << '\n';
      }
    }
  }
}

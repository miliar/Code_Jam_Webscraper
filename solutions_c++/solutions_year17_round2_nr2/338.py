#define NDEBUG
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
using namespace std;


const string POOL = "ROYGBV";
const string IMPOSSIBLE = "IMPOSSIBLE";
char forced(char ch) {
  if (ch == 'G') return 'R';
  if (ch == 'O') return 'B';
  if (ch == 'V') return 'Y';
  return 0;
}
char suggested(char ch) {
  if (ch == 'R') return 'G';
  if (ch == 'B') return 'O';
  if (ch == 'Y') return 'V';
  return 0;
}

bool allowed(char a, char b) {
  static const std::string allowed[] = {
    "RB", "RY", "BY", "BO", "RG", "VY"
  };
  for (const std::string& str : allowed) {
    if (a == str[0] && b == str[1] ||
        a == str[1] && b == str[0]) {
      return true;
    }
  }
  return false;
}

string tryit(int N, vector<int> c, char first, char last) {
  if (!allowed(first, last) || c[first]-- <= 0 || c[last]-- <= 0) {
    return "";
  }
  string out(N, '*');
  out[0] = first;
  out[N-1] = last;
  auto extend = [&](const int start, int di) {
    int i;
    for (i = start; out[i+di] == '*'; i += di) {
      if (char f = forced(out[i])) {
        if (c[f]-- <= 0) {
          throw 1;
        }
        out[i+di] = f;
        continue;
      } else {
        char s = suggested(out[i]);
        assert(s);
        if (c[s]-- <= 0) {
          return i;
        }
        out[i+di] = s;
        continue;
      }
    }
    return i;
  };
  int from = 0, to = extend(N-1, -1);
  // dbg(out, from, to);

  while (from + 1 != to) {
    from = extend(from, 1);
    char best = 0;
    for (char ch : POOL) {
      if (c[ch] > c[best] && allowed(out[from], ch)) {
        best = ch;
      }
    }
    if (best == 0) {
      return "";
    }
    assert(c[best] > 0);
    out[++from] = best;
    --c[best];
  }
  if (out[N-2] == out[N-1]) {
    bool fixed = false;
    for (int i = 0; !fixed && i < N - 2; ++i) {
      if (allowed(out[i], last) && allowed(last, out[i+1])) {
        out.erase(N-2, 1);
        out.insert(out.begin() + i + 1, last);
        fixed = true;
        break;
      }
    }
    if (!fixed) {
      return "";
    }
  }
  for (int i = 0; i < N-1; ++i) {
    assert(allowed(out[i], out[i+1]));
  }
  return out;
}

string solve() {
  int N;
  vector<int> c(256);
  cin >> N >> c['R'] >> c['O'] >> c['Y'] >> c['G'] >> c['B'] >> c['V'];
  // dbg(tryit(N, c, 'Y', 'B'));
  for (char first : POOL) {
    for (char last : POOL) {
      try {
        string out = tryit(N, c, first, last);
        if (!out.empty()) {
          // fprintf(stderr, "sol: %s\n", out.c_str());
          return out;
        }
      } catch(int) {
      }
    }
  }
  return IMPOSSIBLE;
}

int main() {
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    cout << "Case #" << tt << ": " << solve() << endl;
  }
}

#include <algorithm>
#include <cassert>
#include <cfloat>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

#define FOR(i,k,n) for (int (i)=(k); (i)<(n); ++(i))
#define rep(i,n) FOR(i,0,n)
#define all(v) begin(v), end(v)
#define debug(x) cerr<< #x <<": "<<x<<endl
#define debug2(x,y) cerr<< #x <<": "<< x <<", "<< #y <<": "<< y <<endl

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<ll> vll;
typedef vector<vector<ll> > vvll;
typedef deque<bool> db;
template<class T> using vv=vector<vector< T > >;

// cout pair
template<typename T1, typename T2> ostream& operator<<(ostream& s, const pair<T1, T2>& p) {
  s << p.first << " " << p.second << "\n"; return s;
}

// cout vector<pair>
template<typename T1, typename T2> ostream& operator<<(ostream& s, const vector<pair<T1, T2> >& vp) {
  int len = vp.size(); s << "\n";
  for (int i = 0; i < len; ++i) { s << vp[i]; }
    s << "\n"; return s;
}

// cout vector
template<typename T> ostream& operator<<(ostream& s, const vector<T>& v) {
  int len = v.size(); s << "\n";
  for (int i = 0; i < len; ++i) {
    s << v[i]; if (i < len - 1) s << "\t";
  }
  s << "\n"; return s;
}

// cout 2-dimentional vector
template<typename T> ostream& operator<<(ostream& s, const vector< vector<T> >& vv) {
  int len = vv.size();
  for (int i = 0; i < len; ++i) { s << vv[i]; }
  return s;
}

int testcase;
vector<string>  ans;
void output_ans() {
  rep (i, testcase) {
    printf("Case #%d: ", i+1);

    // output ans
    // e.g.) printf("%d\n", ans[i]);

    cout << ans[i];

    printf("\n");
  }
  exit(0);
}

string RYB(int R, int Y, int B) {
  string chr = "RYB";
  int maxi, mini, med;
  maxi = R; med = Y; mini = B;
  if (med < mini) {
    swap(med, mini); swap(chr[1], chr[2]);
  }
  if (maxi < med) {
    swap(maxi, med); swap(chr[0], chr[1]);
  }
  if (med < mini) {
    swap(med, mini); swap(chr[1], chr[2]);
  }

  string ret = "";
  int lp;
  lp = med - mini;
  rep (i, lp) {
    ret += chr[0];
    ret += chr[1];
    maxi -= 1;
    med -= 1;
  }
  lp = maxi / 2;
  rep (i, lp) {
    ret += chr[0];
    ret += chr[1];
    ret += chr[0];
    ret += chr[2];
    maxi -= 2;
    med -= 1;
    mini -= 1;
  }
  if (maxi > 0) {
    ret += chr[0];
    ret += chr[1];
    ret += chr[2];
    maxi -= 1;
    med -= 1;
    mini -= 1;
  }
  lp = med;
  rep (i, med) {
    ret += chr[1];
    ret += chr[2];
  }
  return ret;
}

int n, R, O, Y, G, B, V;
void get_input() {
  // Do not forget initialization or clear

  cin >> n >> R >> O >> Y >> G >> B >> V;
}

void solve(int index_testcase) {
  if (n == 1) {
    if (R == 1) {
      ans[index_testcase] = "R";
    }
    if (O == 1) {
      ans[index_testcase] = "O";
    }
    if (Y == 1) {
      ans[index_testcase] = "Y";
    }
    if (G == 1) {
      ans[index_testcase] = "G";
    }
    if (B == 1) {
      ans[index_testcase] = "B";
    }
    if (V == 1) {
      ans[index_testcase] = "V";
    }
    return;
  }

  if (R > n/2 || O > n/2 || Y > n/2 || G > n/2 || B > n/2 || V > n/2) {
    ans[index_testcase] = "IMPOSSIBLE";
    return;
  }
  if (O == 0 && G == 0 && V == 0) {
    ans[index_testcase] = RYB(R, Y, B);
    return;
  }

  string s = "";
  int remainR, remainY, remainB;
  remainR = remainY = remainB = 0;
  remainR = R - G;
  remainY = Y - V;
  remainB = B - O;

  if (V > 0) {
    if (Y < V) {
      ans[index_testcase] = "IMPOSSIBLE";
      return;
    } else if (Y == V) {
      if (n == Y + V) {
        rep (i, n/2) {
          ans[index_testcase] += "YV";
        }
        return;
      } else {
        ans[index_testcase] = "IMPOSSIBLE";
        return;
      }
    } else {
      rep (i, V) {
        s += "YV";
      }
      s += "Y";
      remainY -= 1;
    }
  }

  if (G > 0) {
    if (R < G) {
      ans[index_testcase] = "IMPOSSIBLE";
      return;
    } else if (R == G) {
      if (n == R + G) {
        rep (i, n/2) {
          ans[index_testcase] += "RG";
        }
        return;
      } else {
        ans[index_testcase] = "IMPOSSIBLE";
        return;
      }
    } else {
      rep (i, G) {
        s += "RG";
      }
      s += "R";
      remainR -= 1;
    }
  }

  if (O > 0) {
    if (B < O) {
      ans[index_testcase] = "IMPOSSIBLE";
      return;
    } else if (B == O) {
      if (n == B + O) {
        rep (i, n/2) {
          ans[index_testcase] += "BO";
        }
        return;
      } else {
        ans[index_testcase] = "IMPOSSIBLE";
        return;
      }
    } else {
      rep (i, O) {
        s += "BO";
      }
      s += "B";
      remainB -= 1;
    }
  }

  if (s == "") {
    if (remainR >= max(remainY, remainB)) {
      rep (i, remainR) {
        s += "R";
      }
      remainR = 0;
    } else
    if (remainY >= max(remainB, remainR)) {
      rep (i, remainY) {
        s += "Y";
      }
      remainY = 0;
    } else
    if (remainB >= max(remainR, remainY)) {
      rep (i, remainB) {
        s += "B";
      }
      remainB = 0;
    }
  }
  int remainR_, remainY_, remainB_;
  remainR_ = remainR;
  remainY_ = remainY;
  remainB_ = remainB;

  if (s.front() == s.back()) {
    if (s.front() == 'R') {
      if (remainY_ > 0) {
        s.insert(0, "Y");
        remainY_ -= 1;
      } else if (remainB_ > 0) {
        s.insert(0, "B");
        remainB_ -= 1;
      }
    } else
    if (s.front() == 'B') {
      if (remainY_ > 0) {
        s.insert(0, "Y");
        remainY_ -= 1;
      } else if (remainR_ > 0) {
        s.insert(0, "R");
        remainR_ -= 1;
      }
    } else
    if (s.front() == 'Y') {
      if (remainB_ > 0) {
        s.insert(0, "B");
        remainB_ -= 1;
      } else if (remainR_ > 0) {
        s.insert(0, "R");
        remainR_ -= 1;
      }
    }
  }

  rep (i, (int)s.length()-1) {
    if (s[i] == s[i+1]) {
      if (s[i] == 'R') {
        if (remainY_ > 0) {
          s.insert(i+1, "Y");
          remainY_ -= 1;
        } else if (remainB_ > 0) {
          s.insert(i+1, "B");
          remainB_ -= 1;
        }
      } else
      if (s[i] == 'B') {
        if (remainY_ > 0) {
          s.insert(i+1, "Y");
          remainY_ -= 1;
        } else if (remainR_ > 0) {
          s.insert(i+1, "R");
          remainR_ -= 1;
        }
      } else
      if (s[i] == 'Y') {
        if (remainB_ > 0) {
          s.insert(i+1, "B");
          remainB_ -= 1;
        } else if (remainR_ > 0) {
          s.insert(i+1, "R");
          remainR_ -= 1;
        }
      }
    }
  }

  while (remainR_ > 0 || remainY_ > 0 || remainB_ > 0) {
//    debug(index_testcase);
//    debug(remainR_);
//    debug(remainY_);
//    debug(remainB_);
    int len;
    len = s.length();
    if (remainR_ > 0 && s[0] != 'V' && s[0] != 'O' && s[0] != 'R' && s[len-1] != 'V' && s[len-1] != 'O' && s[len-1] != 'R') {
      s.insert(0, "R");
      remainR_ -= 1;
    }
    rep (i, (int)s.length() - 1) {
      if (remainR_ <= 0) { break; }
      if (s[i] != 'V' && s[i] != 'O' && s[i] != 'R' && s[i+1] != 'V' && s[i+1] != 'O' && s[i+1] != 'R') {
        s.insert(i+1, "R");
        remainR_ -= 1;
        i += 1;
      }
    }

    len = s.length();
    if (remainY_ > 0 && s[0] != 'O' && s[0] != 'G' && s[0] != 'Y' && s[len-1] != 'O' && s[len-1] != 'G' && s[len-1] != 'Y') {
      s.insert(0, "Y");
      remainY_ -= 1;
    }
    rep (i, (int)s.length() - 1) {
      if (remainY_ <= 0) { break; }
      if (s[i] != 'O' && s[i] != 'G' && s[i] != 'Y' && s[i+1] != 'O' && s[i+1] != 'G' && s[i+1] != 'Y') {
        s.insert(i+1, "Y");
        remainY_ -= 1;
        i += 1;
      }
    }

    len = s.length();
    if (remainB_ > 0 && s[0] != 'G' && s[0] != 'V' && s[0] != 'B' && s[len-1] != 'G' && s[len-1] != 'V' && s[len-1] != 'B') {
      s.insert(0, "B");
      remainB_ -= 1;
    }
    rep (i, (int)s.length() - 1) {
      if (remainB_ <= 0) { break; }
      if (s[i] != 'G' && s[i] != 'V' && s[i] != 'B' && s[i+1] != 'G' && s[i+1] != 'V' && s[i+1] != 'B') {
        s.insert(i+1, "B");
        remainB_ -= 1;
        i += 1;
      }
    }
  }

  ans[index_testcase] = s;
}

int main() {
  cin >> testcase;
  ans.assign(testcase, "");

  rep (i, testcase) {
    get_input();
    //ans[index_testcase] = solve();
    solve(i);
  }

  output_ans();

  return 0;
}

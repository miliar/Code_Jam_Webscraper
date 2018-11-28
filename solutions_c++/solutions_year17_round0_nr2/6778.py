#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
static const double EPS = 1e-8;
static const double PI = 4.0 * atan(1.0);
bool ISINT(double x){return fabs(x-(int)round(x))<EPS;}
bool ISEQ(double x,double y){return fabs(x-y)<EPS;}
string itos(ll x){stringstream ss;ss<<x;return ss.str();}
#define foreach(itr,c) for(__typeof(c.begin()) itr=c.begin();itr!=c.end();itr++)

int n;
string s;

string solve(int idx, int preDigit, bool isEqual) {
  if (idx == n) {
    return "0";
  }
  
  int digit = s[idx] - '0';

  if (isEqual && preDigit <= digit) {
    string tmp = solve(idx + 1, digit, true);
    if (!tmp.empty()) {
      tmp = (char)('0' + digit) + tmp;
      return tmp;
    }
  }

  for (int i = 9; i >= 0; i--) {
    if (isEqual && digit <= i || preDigit > i) {
      continue;
    }
    string tmp = solve(idx + 1, i, false);
    tmp = (char)('0' + i) + tmp;
    return tmp;
  }

  return "";
}

int main() {
  cin.tie(0);
  ios::sync_with_stdio(0);

  int T;
  cin >> T;

  for (int CASE = 1; CASE <= T; CASE++) {
    cout << "Case #" << CASE << ": ";
    cin >> s;
    n = s.size();
    
    string res = solve(0, 0, true);

    for (int i = 0; i < res.size(); i++) {
      if (res[i] == '0') continue;
      cout << res[i];
    }
    cout << endl;
  }
}

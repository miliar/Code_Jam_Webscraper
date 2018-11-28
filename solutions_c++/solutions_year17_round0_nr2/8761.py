#include <bits/stdc++.h>
using namespace std;

int C;
string curr, res;

inline int at(int idx) { return curr[idx]-'0'; }
inline char tochar(int i) { return (char)('0'+i); }

void printres() {
  bool print = false;
  for (int i=0; i<res.size(); ++i) {
    print |= (res[i]!='0');
    if (print) cout << res[i];
  }
  cout << endl;
}

bool tidy(string s) {
  for (int i=1; i<s.size(); ++i)
    if (s[i]<s[i-1]) return false;

  return true;
}

bool gteq(string a, string b) {
  for (int i=0; i<a.size(); ++i) {
    if (a[i]>b[i]) return true;
    if (b[i]>a[i]) return false;
  }
  return true;
}

bool test(string candidate) {
  //cout << candidate << endl;
  if (tidy(candidate) && gteq(candidate, res)) {
    res = candidate;
    return true; }
  return false;
}

bool f(string acc, bool lo) {
  int digit = acc.size();
  if (digit == curr.size()) {
    return test(acc);
  }

  if (lo) {
    string oops = res;
    for (int i=0; i<acc.size(); ++i)
      oops[i]=acc[i];
    for (int i=acc.size(); i<curr.size(); ++i)
      oops[i]= '9';
    test(oops);
  }

  int end = lo ? 9 : at(digit);

  bool res = false;
  string aux;
  for (int i=end; i>=0; --i) {
    //cout << "** " << acc << " " << i << endl;
    bool n_lo = (lo || (i < at(digit)));
    aux = acc; aux += tochar(i);
    if (tidy(aux))
      res |= f(aux, n_lo);

    if (res) goto locura;
  }
 locura:
  return res;
}

int main() {
  ios_base::sync_with_stdio(0); cin.tie(0);
  //cout << gteq("123", "099") << endl;
  cin >> C;
  for (int c=1; c<=C; ++c) {
    cin >> curr;
    res = curr; res[0] = '0';
    for (int i=1; i<res.size(); ++i) res[i] = '9';
    f("",false);
    cout << "Case #" << c << ": "; printres();
  }
  return 0;
}

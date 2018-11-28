#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using ll = long long;
using ld = long double;

template <typename T> T &chmin(T &a, const T &b) { return a = std::min(a, b); }
template <typename T> T &chmax(T &a, const T &b) { return a = std::max(a, b); }
template <typename T> int len(const T &x) { return x.size(); }

struct yes_no : std::numpunct<char> {
  string_type do_truename()  const { return "Yes"; }
  string_type do_falsename() const { return "No"; }
};

void solve();

int main() {
  std::locale loc(std::locale(), new yes_no);
  std::cout << std::boolalpha << std::setprecision(12) << std::fixed;
  std::cout.imbue(loc);
  solve();
  return 0;
}

using namespace std;

void output(const string &s) {
  static int c = 0;
  ++c;
  printf("Case #%d: %s\n", c, s.c_str());
}

const int ok[6][6] = {
  {0, 0, 1, 1, 1, 0},
  {0, 0, 0, 0, 1, 0},
  {1, 0, 0, 0, 1, 1},
  {1, 0, 0, 0, 0, 0},
  {1, 1, 1, 0, 0, 0},
  {0, 0, 1, 0, 0, 0}
};

int num[6];
int p1[6] = {1, 3, 5, 0, 2, 4};
const vector<int> v = {0, 2, 4};
const string mapsto = "ROYGBV";

void solve() {
  int T; cin >> T;
  while (T--) {
    int n;
    cin >> n;
    REP(i,6) cin >> num[i];
    vector<int> res;
    REP(i,6) {
      int p = p1[i];
      if (num[p] > 0) {
        res.push_back(p);
        --num[p];
        break;
      }
    }
    int r = -1;
    REP(c,n-1) {
      r = -1;
      if (num[1] > 0 && ok[res.back()][1]) r = 1;
      else if (num[3] > 0 && ok[res.back()][3]) r = 3;
      else if (num[5] > 0 && ok[res.back()][5]) r = 5;
      else {
        vector<tuple<int,int,int>> vec;
        for (int i: v) {
          if (num[i] > 0 && ok[i][res.back()])
            vec.emplace_back(-num[i], ok[res.front()][i], i);
        }
        sort(ALL(vec));
        if (!vec.empty()) r = get<2>(vec.front());
      }
      res.push_back(r);
      // for (int i: res) cout << i << " ";
      // cout << endl;
      num[r]--;
      if (r == -1) break;
    }
    if (!ok[res.front()][res.back()]) r = -1;
    if (r == -1) {
      output("IMPOSSIBLE");
    }
    else {
      string str;
      for (int i: res)
        str += mapsto[i];
      output(str);
    }
  }
  return;
}

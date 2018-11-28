
#include<bits/stdc++.h>

using namespace std;

#define all(c) (c).begin(), (c).end()
int ni() { int val; scanf("%i", &val); return val; }
pair<int, int> npi() { pair<int, int> val; scanf("%i %i", &val.first, &val.second); return val; }
int64_t nll() { int64_t val; scanf("%I64d", &val); return val; }
vector<int> nvi(int n, int corr = 0) { vector<int> a(n); for (int i = 0; i < n; ++i) a[i] = ni() + corr; return move(a); }
char nc() { char val; do { val = getchar(); } while (val == ' ' || val == '\r' || val == '\n'); return val; }
char ncs() { char val; do { val = getchar(); } while (false); return val; }
string ns() { static char buff[1024 * 4000]; scanf("%s", buff); return string{ buff }; }
int64_t gcd(int64_t a, int64_t b) { while (b) { auto tmp = a % b; a = b; b = tmp; } return a; }
int64_t tr2(int x1, int y1, int x2, int y2, int x3, int y3) { return 1LL * (x2 - x1) * (y3 - y1) - 1LL * (y2 - y1) * (x3 - x1); }

const string input_dir = "inputs\\";
string input_file = input_dir + "b-small.in";
string output_file = input_dir + "b-small_f.out";
void init_streams() {
  freopen(input_file.c_str(), "r", stdin);
  freopen(output_file.c_str(), "w", stdout);
}

int to_idx(char c) {
  if (c == 'R') return 0;
  if (c == 'O') return 1;
  if (c == 'Y') return 2;
  if (c == 'G') return 3;
  if (c == 'B') return 4;
  return 5;
}

bool cl_fit[6][6];
bool colors_ok(char c1, char c2) {
  return cl_fit[c1][c2];
}

struct State {  
  char first;
  char last;
  array<short, 6> free;
  const State * prev = nullptr;
  bool operator < (const State& other) const {
    if (first != other.first)
      return first < other.first;
    if (last != other.last)
      return last < other.last;
    return free < other.free;
  }
};

int main()
{
  init_streams();
  auto t = ni(), cs = 0;

  memset(cl_fit, true, sizeof(cl_fit));
  for (int i = 0; i < 6; ++i)
  {
    cl_fit[i][i] = false;
    if (i == 1) {
      cl_fit[i][0] = false;
      cl_fit[0][i] = false;
      cl_fit[i][2] = false;
      cl_fit[2][i] = false;
    }
    if (i == 3) {
      cl_fit[i][4] = false;
      cl_fit[4][i] = false;
      cl_fit[i][2] = false;
      cl_fit[2][i] = false;
    }
    if (i == 5) {
      cl_fit[i][0] = false;
      cl_fit[0][i] = false;
      cl_fit[i][4] = false;
      cl_fit[4][i] = false;
    }
  }

  while (cs < t) {
    printf("Case #%i: ", ++cs);

    auto n = ni();

    vector<char> color{ 'R', 'O', 'Y', 'G', 'B', 'Y' };
    const int ncolors = 6;
    vector<int> cnt(ncolors);
    vector<pair<int, int>> cn;
    for (int i = 0; i < ncolors; ++i) {
      cnt[i] = ni();
      cn.push_back(make_pair(cnt[i], i));
    }

    State ini_st;
    for (int i = 0; i < ncolors; ++i) {
      ini_st.free[i] = cnt[i];
    }

    set<State> sts[1001];

    sort(all(cn), greater<pair<int,int>>());
    // Go greedy!
    string res; res.resize(n);
    bool good = true;
    int offset = 0;
    if (n > 5)
    {
      for (int i = 0; i < 3 * n / 4; ++i) {
        auto f = false;
        for (int j = 0; j < cn.size(); ++j) if (cn[j].first && (i == 0 || colors_ok(res[i - 1], cn[j].second))) {
          --cn[j].first;
          res[i] = cn[j].second;
          f = true;
          break;
        }
        if (!f) {
          good = false;
          break;
        }
        if (i == 0) {
          ini_st.first = res[0];
          ini_st.last = res[0];
        }
        else {
          ini_st.last = res[i];
        }
        --ini_st.free[res[i]];
        ++offset;
        sort(all(cn), greater<pair<int, int>>());
      }

      if (!good) {
        printf("IMPOSSIBLE\n");
        continue;
      }      
    }

    // Go smart!
    for (int i = 0; i < ncolors; ++i) if (ini_st.free[i]) {
      if (offset == 0 || colors_ok(i, res[offset - 1])) {
        --ini_st.free[i];
        if (offset == 0)
          ini_st.first = i;
        ini_st.last = i;
        sts[offset].emplace(ini_st);
        ++ini_st.free[i];
      }
    }

    for (int i = offset; i + 1 < n; ++i) {
      for (auto& state : sts[i]) {
        auto new_st = state;
        for (int j = 0; j < ncolors; ++j) if (new_st.free[j] && colors_ok(state.last, j) && (i + 2 < n || colors_ok(state.first, j))) {
          --new_st.free[j];
          new_st.last = j;
          new_st.prev = &state;
          sts[i + 1].emplace(new_st);
          ++new_st.free[j];
        }
      }
    }

    if (sts[n - 1].empty()) {
      printf("IMPOSSIBLE\n");
    }
    else {
      auto* cur = &(*sts[n - 1].begin());
      int p = n - 1;
      while (cur != nullptr) {
        res[p] = color[cur->last];
        --p;
        cur = cur->prev;
      }

      for (int i = 0; i < n; ++i) if (res[i] <= 5) {
        res[i] = color[res[i]];
      }

      printf("%s\n", res.c_str());
    }

    fflush(stdout);
  }

  return 0;
}

//int main()
//{
//  init_streams();
//  auto t = ni(), cs = 0;
//
//  memset(cl_fit, true, sizeof(cl_fit));
//  for (int i = 0; i < 6; ++i)
//  {
//    cl_fit[i][i] = false;
//    if (i == 1) {
//      cl_fit[i][0] = false;
//      cl_fit[0][i] = false;
//      cl_fit[i][2] = false;
//      cl_fit[2][i] = false;
//    }
//    if (i == 3) {
//      cl_fit[i][4] = false;
//      cl_fit[4][i] = false;
//      cl_fit[i][2] = false;
//      cl_fit[2][i] = false;
//    }
//    if (i == 5) {
//      cl_fit[i][0] = false;
//      cl_fit[0][i] = false;
//      cl_fit[i][4] = false;
//      cl_fit[4][i] = false;
//    }
//  }
//
//  set<State> sts[1001];
//  while (cs < t) {
//    printf("Case #%i: ", ++cs);
//
//    auto n = ni();
//
//    vector<char> color{'R', 'O', 'Y', 'G', 'B', 'Y'};
//    const int ncolors = 6;
//    vector<int> cnt(ncolors);
//    vector<pair<int, int>> cn;
//    for (int i = 0; i < ncolors; ++i) {
//      cnt[i] = ni();
//      cn.push_back(make_pair(cnt[i], i));
//    }
//
//    State ini_st;
//    for (int i = 0; i < ncolors; ++i) {
//      ini_st.free[i] = cnt[i];
//    }
//
//    for (int i = 0; i < n; ++i)
//      sts[i].clear();
//
//    for (int i = 0; i < ncolors; ++i) if (ini_st.free[i]) {
//      --ini_st.free[i];
//      ini_st.first = i;
//      ini_st.last = i;
//      sts[0].emplace(ini_st);
//      ++ini_st.free[i];
//    }
//
//    for (int i = 0; i + 1 < n; ++i) {
//      for (auto& state : sts[i]) {
//        auto new_st = state;
//        for (int j = 0; j < ncolors; ++j) if (new_st.free[j] && colors_ok(new_st.last, j) && (i + 2 < n || colors_ok(new_st.first, j))) {
//          --new_st.free[j];
//          new_st.last = j;
//          new_st.prev = &state;
//          sts[i + 1].emplace(new_st);
//          ++new_st.free[j];
//        }
//      }
//    }
//
//    if (sts[n - 1].empty()) {
//      printf("IMPOSSIBLE\n");
//    }
//    else {
//      string res; res.resize(n);
//      auto* cur = &(*sts[n - 1].begin());
//      int p = n - 1;
//      while (cur != nullptr) {
//        res[p] = color[cur->last];
//        --p;
//        cur = cur->prev;
//      }
//      printf("%s\n", res.c_str());
//    }
//
//    fflush(stdout);
//    
//  }
//
//  return 0;
//}

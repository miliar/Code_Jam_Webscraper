#include <bits/stdc++.h>

using namespace std;

const int N = 1e3 + 10;
typedef pair<int, int> ii;
const int M = 1440;
bool DEBUG;

struct itv {
  int first, second;
  int owner;  // 0 <- C, 1 <- J
  int len() const {
    int ans = second - first;
    if (ans < 0) ans += M;
    return ans;
  }
  itv() : 
    first(0), second(0), owner(0) {}
  itv(int _x, int _y) : 
    first(_x), second(_y), owner(-1) {}
  itv(int _x, int _y, int _s) : 
    first(_x), second(_y), owner(_s) {}
};

inline bool comp(const itv &a, const itv &b) {
  if (a.first != b.first) return a.first < b.first;
  return a.second < b.second;
}

inline bool comp2(const itv &a, const itv &b) {
  return a.len() < b.len();
}

vector<itv> s_must, s_may, occ; 

int main2() {
  int ac, aj;
  cin >> ac >> aj;
  occ.clear();
  s_must.clear();
  s_may.clear();
  for (int i = 0, c, d; i < ac; ++i) {
    cin >> c >> d;
    occ.push_back({c, d, 0});
  }
  for (int i = 0, c, d; i < aj; ++i) {
    cin >> c >> d;
    occ.push_back({c, d, 1});
  }

  sort(occ.begin(), occ.end(), comp);
  for (int i = 1; i < ac + aj; ++i) {
    if (occ[i].owner != occ[i - 1].owner) {
      s_must.push_back({occ[i - 1].second, occ[i].first, -1});
    } else {
      s_may.push_back({occ[i - 1].second, occ[i].first, occ[i].owner});
    }
  }
  // midnight 
  if (occ[0].owner != occ[ac + aj - 1].owner) {
      s_must.push_back({occ[ac + aj - 1].second, occ[0].first, -1});
  } else {
      s_may.push_back({occ[ac + aj - 1].second, occ[0].first, occ[0].owner});
  }
  if (DEBUG) cerr << s_must.size() << " may " << s_may.size() << "\n"; 
  
  int j_time = 0, c_time = 0;
  for (itv &e : occ) {
    if (e.owner == 0) c_time += e.len();
    else j_time += e.len();
  }
  for (itv &e : s_may) {
    if (e.owner == 0) c_time += e.len();
    else j_time += e.len();
  }
  if (DEBUG) cerr << c_time << " j " << j_time << "\n";
  int gt = (j_time > c_time);
  int diff = abs(c_time - j_time); 
  int ans = 0;
  for (itv &e : s_must) diff -= e.len(), ++ans;
  if (diff <= 0) {
    // lol
  } else {
    // take from may
    sort(s_may.begin(), s_may.end(), comp2);
    reverse(s_may.begin(), s_may.end());
    for (itv &e : s_may) {
      if (DEBUG) cerr << e.len() << " ow " << e.owner << "\n";
    }
    int idx = 0;
    while (diff > 0) {
      if (s_may[idx].owner == gt) {
        diff -= 2*s_may[idx].len();
        ans += 2;
      }
      ++idx;
    }
  }
  cout << ans << "\n";

  return 0;
}

int main() {
  int T; cin >> T;
  for (int qq = 1; qq <= T; ++qq) {
    printf("Case #%d: ", qq);
    //if (qq == 4) DEBUG = true;
    //else 
      DEBUG = false;
    main2();
  }
  return 0;
}

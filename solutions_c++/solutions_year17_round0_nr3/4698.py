#include <iostream>
#include <cmath>
#include <vector>
#include <cassert>
#include <cstdio>
#include <limits>
#include <set>
#include <string>
#include <cstring>
#include <fstream>
#include <queue>

using namespace std;

void invert(string& s, int from, int cnt){
  while (cnt) {
    if (s[from] == '-') {
      s[from] = '+';
    }
    else {
      s[from] = '-';
    }
    from++;
    --cnt;
  }
}

int solve_1(int k, string str) {
  int ans = 0;
  for (int i = 0; i <= str.length()-k; ++i) {
    if (str[i] == '+') {
      continue;
    } else {
      invert(str, i, k);
      ans++;
    }
  }
  for (int i = 0; i < k; ++i) {
    if (str[str.length() - k + i] == '-') ans = -1;
  }
  return ans;
}

void f(uint64_t val, const uint64_t& n, uint64_t& mx) {
  if (val > n) return;
  if (val > mx) mx = val;
  for (int i = ((val % 10 == 0)?1: val % 10); i < 10; ++i) {
    f(val * 10 + i, n, mx);
  }
}
long long solve_2(uint64_t n) {
  uint64_t mx = 0;
  f(0, n, mx);
  return mx;
}

class p3_comparator {
public:
  bool operator () (const pair<int, int>& a, const pair<int, int>& b) {
    int len_a = a.second - a.first;
    int len_b = b.second - b.first;
    if (len_a == len_b) return a.first < b.first;
    return len_a > len_b;
  }
};
pair<int,int> solve_3(int n, int k) {
  set< pair<int, int>, p3_comparator> st;
  st.insert(std::make_pair(1, n));
  int ans = 0;
  pair<int, int> answer;
  for (int i = 1; i <= k; ++i) {
    auto otr = st.begin();
    ans = (otr->first + otr->second) / 2;
    answer.first = (otr->second - otr->first) / 2 + (otr->second - otr->first) % 2;
    answer.second = (otr->second - otr->first) / 2;
    pair<int, int> new_first_otr(otr->first, ans - 1);
    pair<int, int> new_second_otr(ans + 1, otr->second);
    st.erase(otr);
    if (new_first_otr.first <= new_first_otr.second) st.insert(new_first_otr);
    if (new_second_otr.first <= new_second_otr.second) st.insert(new_second_otr);
  }
  return answer;
}
int main() {
  ifstream in("input.txt");
  ofstream out("output.txt");
  int T;
  in >> T;
  for (int t_case = 1; t_case <= T; t_case++) {
    uint64_t n,k;
    in >> n >> k;
    auto sl = solve_3(n, k);
    out << "Case #" << t_case << ": " << sl.first <<" "<<sl.second << endl;
  }
  out.close();
  return 0;
}

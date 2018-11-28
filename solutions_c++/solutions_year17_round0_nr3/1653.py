#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

using ull = unsigned long long;

void find_min_max(const vector<bool>& v, ull i, ull *min, ull *max) {
  int j = i - 1;
  while (!v[j])
    --j;

  int k = i + 1;
  while (!v[k])
    ++k;

  *min = std::min(i - j, k - i);
  *max = std::max(i - j, k - i);
}

void slow(ull n, ull k, ull& min_out, ull& max_out) {
  vector<bool> v(n + 2, false);
  v[0] = true;
  v[n + 1] = true;

  ull ind = 0, ind_maxmin = 0, ind_max = 0;
  for (ull i = 0; i < k; ++i) {
    ind = 0, ind_maxmin = 0, ind_max = 0;
    for (ull j = 1; j < n + 1; ++j) {
      if (!v[j]) {
        ull min, max;
        find_min_max(v, j, &min, &max);

        if (min > ind_maxmin) {
          ind = j;
          ind_maxmin = min;
          ind_max = max;
        } else if (min == ind_maxmin) {
          if (max > ind_max) {
            ind = j;
            ind_maxmin = min;
            ind_max = max;
          } else if (max == ind_max) {
            if (j < ind) {
              ind = j;
              ind_maxmin = min;
              ind_max = max;
            }
          }
        }
      }
    }

    v[ind] = true;
  }

  max_out= ind_max - 1;
  min_out = ind_maxmin - 1;
}

void div(ull n, ull& a, ull& b) {
  if (n == 0) {
    a = 0;
    b = 0;
  } else {
    a = (n - 1) / 2;
    b = n - (n - 1) / 2 - 1;
    if (a > b)
      swap(a, b);
  }
}

void fast(ull n, ull k, ull& min_out, ull& max_out) {
  multiset<pair<ull, ull>> s;
  ull a, b;
  div(n, a, b);
  s.emplace(a, b);
  --k;

  while (k != 0) {
    ull min = s.rbegin()->first;
    ull max = s.rbegin()->second;
    --k;
    s.erase(--s.end());

    div(max, a, b);
    s.emplace(a, b);
    div(min, a, b);
    s.emplace(a, b);
  }

  min_out = s.rbegin()->first;
  max_out = s.rbegin()->second;
}

void fast2(ull n, ull k, ull& min_out, ull& max_out) {
  map<pair<ull, ull>, ull> s;
  ull a, b;
  div(n, a, b);
  s[make_pair(a, b)] = 1;
  --k;

  while (k != 0) {
    ull min = s.rbegin()->first.first;
    ull max = s.rbegin()->first.second;
    ull count = s.rbegin()->second;
    if (count > k) // !
      break;
    k -= count;
    s.erase(--s.end());

    div(max, a, b);
    s[make_pair(a, b)] += count;
    div(min, a, b);
    s[make_pair(a, b)] += count;
  }

  min_out = s.rbegin()->first.first;
  max_out = s.rbegin()->first.second;
}


int main() {
  int T=0;
  cin >> T;

  for (int test = 1; test <= T; ++test) {
    ull n, k;
    // ull min_out, max_out;
    ull min_out2, max_out2;

    cin >> n >> k;

    // slow(n, k, min_out, max_out);
    fast2(n, k, min_out2, max_out2);

    cout << "Case #" << test << ": " << max_out2 << " " << min_out2 << endl;
  }
  
}

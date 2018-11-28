#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <utility>
#include <queue>
#include <unordered_set>
#include <cstdlib>
#include <cassert>

using namespace std;

#define ULL unsigned long long

vector<ULL> read(ULL n) {
  vector<ULL> r;
  do {
    r.push_back(n % 10);
    n /= 10;
  } while (n != 0);
  return r;
}

ULL getInt(vector<ULL> v) {
  ULL val = 0;
  for (int i = 0; i < v.size(); i++) {
    val *= 10;
    val += v[i];
  }
  return val;
}

bool valid(vector<ULL> v) {
  for (int i = 1; i < v.size(); i++) {
    if (v[i] < v[i-1])
      return false;
  }

  return true;
}

bool valid(ULL v) {
  auto vec = read(v);
  reverse(vec.begin(), vec.end());
  return valid(vec);
}

bool getVec(ULL& lb, ULL& ub, vector<ULL>& ret, int idx = 0, ULL gt = 0) {
  // cout << idx << " " << gt << endl;
  if (idx == ret.size()) return true;
  for (int i = 9; i >= gt && i >= 0; i--) {
    ret[idx] = i;
    ULL val = getInt(ret);
    // cout << "Checking " << i << " at " << idx << ", val: " << val << endl;
    if (val < lb || val > ub) {
      continue;
    }
    if (getVec(lb, ub, ret, idx+1, i)) {
      return true;
    }
  }
  ret[idx] = 0;
  return false;
}

ULL gen(ULL lb, ULL ub) {
  vector<ULL> vu = read(ub), vl = read(lb);
  ULL extra = vu.size() - vl.size();
  vl.resize(vu.size());
  for (int i = vl.size()-1; extra > 0; extra--) vl[i] = 0;
  reverse(vl.begin(), vl.end());
  reverse(vu.begin(), vu.end());

  vector<ULL> ret;
  ret.resize(vl.size(), 0);
  /*
  for (int i = 0; i < vl.size(); i++)
    cout << vl[i] << " ";
  cout << endl;

  for (int i = 0; i < vl.size(); i++)
    cout << vu[i] << " ";
  */
  // cout << endl;


  if (getVec(lb, ub, ret)) {
    return getInt(ret);
  }

  return 0;
}

ULL bf(ULL lb, ULL ub) {
  for (ULL i = ub; i >= lb; i--) {
    if (valid(i))
      return i;
  }
  return 0;
}

int main() {
  int cases;
  cin >> cases;
  int i = 0;
  while (cases--) {
    i++;
    ULL n;
    cin >> n;
    ULL val = gen(0, n);
    // assert(val == bf(0, n));
    cout << "Case #" << i << ": " << gen(0, n) << endl;
  }
  return 0;
}

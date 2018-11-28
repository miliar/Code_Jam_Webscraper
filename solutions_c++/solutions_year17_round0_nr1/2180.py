#include <iostream>
#include <vector>

using namespace std;

int solve(vector<bool> &v,int k) {
  int count = 0;
  int len = 0;
  int pos = 0;
  int n = (int)v.size();
  int start = 0;
  while (pos <= n-k) {
    if (v[pos]) {
      pos++;
      continue;
    }
    start = pos;
    len = 1;
    while(len < k && start+len < n && v[start+len] == false) {
      len++;
    }
    for (int i = start;i < start+k;i++) {
      v[i] = !v[i];
    }
    //debug
//    printf("flip at %4d, v = ",pos);
//    for (auto x : v)
//      cout << (x ? '+' : '-');
//    cout << endl;
//    //
    pos += (len - 1);
    len = 0;
    count++;
  }
  for (int i = n-k+1;i < n;i++) {
    if (v[i] == false) return -1;
  }
  return count;
}

int main() {
  int T;
  cin >> T;
  for (int cn = 1;cn <= T;cn++) {
    string s; int k;
    cin >> s >> k;
    vector<bool> v;
    v.clear();
    for (auto &c : s) {
      v.push_back(c == '+');
    }
    int res = solve(v,k);
    if (res >= 0) {
      printf("Case #%d: %d\n",cn,res);
    } else {
      printf("Case #%d: IMPOSSIBLE\n",cn);
    }
  }
}


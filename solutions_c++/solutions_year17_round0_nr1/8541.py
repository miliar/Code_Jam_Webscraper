#include <stdio.h>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;


void print_vector(vector<string> v) {
  for (int i=0; i < v.size(); i++) {
    cout << v[i] << ' ';
  } cout << endl;
}


bool all_same(string s) {
  set<char> chars;
  for (int i=0; i < s.size(); i++) {
    chars.insert(s[i]);
  }
  return chars.size() == 1;
}

int k;
string flip_s(string s, int i) {
  for (int j = i; j < i + k; j++) {
    s[j] = s[j] == '+' ? '-' : '+';
  }
  return s;
}

int solve(string s, int i) {
  // cout << s << endl;
  if (all_same(s) && s[0] == '+') {
    return 0;
  }
  if (i + k - 1 == s.size()) {
    return 1e9;
  }

  return min(solve(s, i + 1), 1 + solve(flip_s(s, i), i + 1));
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt1.in","r", stdin);
	freopen("code.out","w", stdout);
#endif
  int t; cin >> t;
  for (int i=1; i <= t; i++) {
    string s;
    cin >> s >> k;
    printf("Case #%d: ", i);
    int res = solve(s, 0);
    if (res == 1e9) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", res);
    }
  }
	return 0;
}

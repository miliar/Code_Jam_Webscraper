#include <bits/stdc++.h>

using namespace std;

const int N = 1010;

char s[10] = "ROYGBV";
int c[10], n;

string getss(char bf, char nw) {
  vector<char> v;
  if (bf == nw) {
    for (int i = 0; i < 6; i += 2) if (s[i] != bf) {
      v.push_back(s[i]);
    }
    return string(1, v[0]) + string(1, bf) + string(1, v[1]);
  } else {
    for (int i = 0; i < 6; i += 2) if (s[i] != bf && s[i] != nw) {
      v.push_back(s[i]);
    }
    return string(1, nw) + string(1, v[0]) + string(1, bf);
  }
}

void gets2(vector<string> &v3, char *s) {
  int k = 0;
  for (string i : v3) {
    for (char j : i) {
      s[k++] = j;
    }
  }
  s[k] = 0;
}

char getback(const string &a) {
  return a[a.length() - 1];
}

bool check(char *s) {
  int n = strlen(s);
  if (s[0] == s[n - 1]) return 0;
  for (int i = 1; i < n; ++i) {
    if (s[i] == s[i - 1]) return 0;
  }
  return 1;
}

void go(const vector<pair<int, char> > &v, int _) {
  vector<string> v2;
  for (int i = 0; i < v[0].first - v[1].first; ++i) {
    v2.push_back(string(1, v[0].second));
  }
  for (int i = 0; i < v[1].first - v[2].first; ++i) {
    v2.push_back(string(1, v[1].second) + string(1, v[0].second));
  }
  //for (string i : v2) printf("%s ", i.c_str()); puts("");
  vector<string> v3;
  int cnt = 0;
  for (int i = 0; i < v2.size(); ++i) {
    char bf = i ? getback(v2[i - 1]) : getback(v2.back());
    char nw = v2[i][0];
    if (cnt < v[2].first) {
      v3.push_back(getss(bf, nw));
      ++cnt;
    }
    v3.push_back(v2[i]);
  }
  //for (string i : v3) printf("%s ", i.c_str()); puts("");
  while (cnt < v[2].first) {
    v3.push_back(string(1, v[1].second) + string(1, v[2].second) + string(1, v[0].second));
    ++cnt;
  }
  //for (string i : v3) printf("%s ", i.c_str()); puts("");
  char s2[N];
  gets2(v3, s2);
  //puts(s2);
  if (check(s2)) printf("Case #%d: %s\n", _, s2);
  else {
    if (v[1].first + v[2].first >= v[0].first) {
      assert(0);
    }
    printf("Case #%d: IMPOSSIBLE\n", _);
  }
}

int main() {
  int t;
  scanf("%d", &t);
  for (int _ = 1; _ <= t; ++_) {
    scanf("%d", &n);
    for (int i = 0; i < 6; ++i) {
      scanf("%d", c + i);
    }
    vector<pair<int, char> > v;
    for (int i = 0; i < 6; i += 2) {
      v.push_back({c[i], s[i]});
    }
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    go(v, _);
  }
  return 0;
}

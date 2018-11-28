#include <cstdio>
#include <set>
#include <stack>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <iostream>
#include <cassert>
#include <cmath>
#include <algorithm>
#include <climits>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;


set<string> next_rows(string s, int K) {
  set<string> res;
  int T = s.length();
  for (int i = 0; i + K <= T; i++) {
    string flipped = s;
    for (int j = i; j < i + K; j++) {
      flipped[j] = (flipped[j] == '+')?'-':'+';
    }
    res.insert(flipped);
  }
  return res;
}

bool is_plus(string s) {
  for (char c : s) {
    if (c == '-') return false;
  }
  return true;
}

struct mypair {
  string s;
  int n;
};

int bfs(string s, int k) {
  queue<mypair> next;
  next.push({s,0});
  set<string> visited;
  visited.insert(s);

  while (!next.empty()) {
    mypair current = next.front();
    next.pop();
    if (is_plus(current.s)) {
      return current.n;
    }

    for (auto n : next_rows(current.s, k)) {
      if (visited.find(n) != visited.end()) {
        continue;
      }
      visited.insert(n);
      next.push({n,current.n+1});
    }

  }
  return -1;
}

int main(int nargs, char **argv) {
    int N;
    std::ios::sync_with_stdio(false);
    cin >> N;
    for (int i = 0; i < N; i++) {
      string S;
      int K;
      cin >> S;
      cin >> K;
      int res = bfs(S, K);
      cout << "Case #" << i+1 << ": ";
      if (res == -1) {
        cout << "IMPOSSIBLE";
      } else {
        cout << res;
      }
      cout << endl;
    }

    return 0;
}


#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct st {
  int id, ls, rs;
  st() {}
  st(int a, int b, int c) : id(a), ls(b), rs(c) {}
};

bool cmp(const st &a, const st &b) {
  if (min(a.ls, a.rs) == min(b.ls, b.rs)) {
    if (max(a.ls, a.rs) == max(b.ls, b.rs)) {
      return a.id < b.id;
    } else {
      return max(a.ls, a.rs) > max(b.ls, b.rs);
    }
  } else {
    return min(a.ls, a.rs) > min(b.ls, b.rs);
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int T; cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    cout << "Case #" << tc << ": ";

    int N, K; cin >> N >> K;
    vector<int> stalls(N+2);
    stalls[0] = stalls[N+1] = 1;
    for (int i = 1; i <= K; i++) {
      vector<st> tmp;
      for (int pos = 1; pos <= N; pos++) {
        if (stalls[pos]) continue;
        int ls = 0, rs = 0;
        for (int j = pos-1; j >= 1; j--) {
          if (stalls[j]) break; ls++;
        }
        for (int j = pos+1; j <= N; j++) {
          if (stalls[j]) break; rs++;
        }
        tmp.push_back({pos, ls, rs});
      }
      sort(tmp.begin(), tmp.end(), cmp);
      stalls[tmp[0].id] = 1;
      if (i == K) {
        cout << max(tmp[0].ls, tmp[0].rs) << " " << min(tmp[0].ls, tmp[0].rs) << endl;
      }
    }
  }
}

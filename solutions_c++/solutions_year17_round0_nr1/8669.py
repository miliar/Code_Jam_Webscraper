#include <iostream>
#include <queue>
#include <map>
using namespace std;


int main() {
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    string s;
    int k;
    cin >> s >> k;
    map<string, int> dist;
    dist[s] = 0;
    queue<string> Q;
    Q.push(s);
    while (!Q.empty()) {
      string t = Q.front();
      Q.pop();
      int d = dist[t];

      for (int i = 0; i < t.size() - k + 1; i++) {
        string new_t = t;
        for (int j = 0; j < k; j++) {
          if (new_t[i + j] == '+') new_t[i + j] = '-';
          else new_t[i + j] = '+';
        }
        if (!dist.count(new_t)) {
          dist[new_t] = d + 1;
          Q.push(new_t);
        }
      }

    }
    
    cout << "Case #" << tt << ": ";
    string ans = s;
    for (int i = 0; i < s.size(); i++) ans[i] = '+';
    if (dist.count(ans)) {
      cout << dist[ans] << endl;
    } else {
      cout << "IMPOSSIBLE" << endl;
    }

  }
  return 0;
}

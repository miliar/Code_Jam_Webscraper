#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>

using namespace std;

bool HappySideUp(const string& S) {
  for (const char c : S) {
    if (c == '-') return false;
  }
  return true;
}

string ReversePancake(string step, int l, int r) {
  for (int i = l; i <= r; ++i) {
    if (step[i] == '+') step[i] = '-';
    else step[i] = '+';
  }
  return step;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    string S;
    cin >> S;
    int K;
    cin >> K;
    queue<string> q;
    q.push(S);
    unordered_map<string, int> visited;
    visited[S] = 0;
    string step;
    while (!q.empty()) {
      step = q.front();
      if (HappySideUp(step)) {
        cout << "Case #" << i + 1 << ": " << visited[step] << endl;
        break;
      } else {
        q.pop();
		string t;
        for (int j = 0; j <= S.size() - K; ++j) {
          t = ReversePancake(step, j, j + K - 1);
          if (visited.count(t) != 0) continue;
          q.push(t);
          visited[t] = visited[step] + 1;
        }
      }
    }
    if (q.empty()) cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
  }
  return 0;
}
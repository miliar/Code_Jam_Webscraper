#include <bits/stdc++.h>
#include <sys/wait.h>
#include <unistd.h>
using namespace std;

#define int long long

int n, q;
vector<int> limit, speed;
int dist[200][200];

vector<int> start, finish;
void readinput() {
  cin >> n >> q;
  limit.resize(n);
  speed.resize(n);
  start.resize(q);
  finish.resize(q);
  for (int i = 0; i < n; ++i) {
    cin >> limit[i] >> speed[i];
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      cin >> dist[i][j];
    }
  }
  for (int i = 0; i < q; ++i) {
    cin >> start[i] >> finish[i];
    start[i] -= 1;
    finish[i] -= 1;
  }
}

using State = tuple<double, int, int, int, array<bool, 105>>;

void solve() {
  for (int i = 0; i < q; ++i) {
    queue<State> qu;
    qu.push({0, start[i], limit[start[i]], speed[start[i]], array<bool, 105>()});
    double ans = 9e99;
    double bestcity[200];
    for (int i = 0; i < n; ++i)
      bestcity[i] = 9e99;
    while (qu.size()) {
      //if (qu.size() == 0) brea
      State s = qu.front();
      qu.pop();

      double t = get<0>(s);
      int c = get<1>(s);
      int lim = get<2>(s);
      int spd = get<3>(s);
      array<bool, 105> visited = get<4>(s);
      visited[c] = true;

      //if (lim == limit[c] && spd == speed[c] && t > bestcity[c]) continue;

      if (c == finish[i] && t < ans) ans = t;

      for (int j = 0; j < n; ++j) {
        if (!visited[j] && dist[c][j] != -1 && dist[c][j] <= lim) {
          double nt = t + (double)dist[c][j]/spd;
          qu.push({nt, j, lim-dist[c][j], spd, visited});
          if (bestcity[j] > nt) {
            qu.push({nt, j, limit[j], speed[j], visited});
            bestcity[j] = nt;
          }
        }
      }
    }

    cout << fixed << setprecision(16) << ans << " ";
  }
  cout << endl;
}







bool multiprocess(int i);

void solveinternal(int case_num) {
  readinput();
  //if (multiprocess(case_num)) return;
    cout << "Case #" << case_num << ": ";
  solve();
  //exit(0);
}

int multiprocess_qtd = 0;
bool multiprocess(int i) {
  multiprocess_qtd += 1;
  int32_t status;
  if (multiprocess_qtd > 5) {
    wait(&status);
    multiprocess_qtd -= 1;
  }
  int pid = fork();
  if (pid == 0) {
    stringstream ss;
    ss << "/tmp/socubdsou" << i;
    ofstream* out = new ofstream(ss.str());
    cout.rdbuf(out->rdbuf());
    cout << "Case #" << i << ": ";
    return false;
  }
  return true;
}

int32_t main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    solveinternal(i);
  }
/*
  int32_t status;
  for (int i = 1; i <= multiprocess_qtd; ++i) wait(&status);

  stringstream ss;
  ss << "cat";
  for (int i = 1; i <= n; ++i) {
    ss << " /tmp/socubdsou" << i;
  }
  system(ss.str().c_str());
  */
}

#include <bits/stdc++.h>
#include <sys/wait.h>
#include <unistd.h>
using namespace std;

int d, n;
vector<int> k, s;
void readinput() {
  cin >> d >> n;
  k.resize(n);
  s.resize(n);
  for (int i = 0; i < n; ++i) {
    cin >> k[i] >> s[i];
  }
}

void solve() {
  long double tend = 0;
  for (int i = 0; i < n; ++i) {
    long double t = (long double)(d - k[i]) / s[i];
    tend = max(t, tend);
  }

  cout << fixed << setprecision(16) << (long double)d / tend << endl;
}







bool multiprocess(int i);

void solveinternal(int case_num) {
  readinput();
  if (multiprocess(case_num)) return;
  solve();
  exit(0);
}

int multiprocess_qtd = 0;
bool multiprocess(int i) {
  multiprocess_qtd += 1;
  int status;
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

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    solveinternal(i);
  }

  int status;
  for (int i = 1; i <= multiprocess_qtd; ++i) wait(&status);

  stringstream ss;
  ss << "cat";
  for (int i = 1; i <= n; ++i) {
    ss << " /tmp/socubdsou" << i;
  }
  system(ss.str().c_str());
}

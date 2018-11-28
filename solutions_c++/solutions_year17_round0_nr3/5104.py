#include <bits/stdc++.h>

using namespace std;

void Solve() {
  int64_t K, N;
  cin >> N >> K;

  priority_queue<int64_t> q;
  q.push(N);

  int64_t l, r;

  for (int i = 0; i < K; i++) {
    int64_t a = q.top(); q.pop();
    

    if (a % 2 == 0) {
      l = a / 2;
      r = a / 2 - 1;
      q.push(a / 2);
      q.push(a / 2 - 1);
    } else {
      l = a / 2;
      r = a / 2;
      q.push(a / 2);
      q.push(a / 2);
    }
  }

  cout << l << " " << r;
}

int main(int argc, char **argv) {
  (void)argc;
  (void)argv;

  const string problem = "small"; // practice, small, large
  const bool redirectStdoutToFile = true;
  const bool redirectStderrToFile = true;

  string inputFile = "";
  string stdoutFile = "";
  string stderrFile = "./output/C.stderr";

  if (problem == "practice") {
    inputFile  = "./input/C-practice.in";
    stdoutFile = "./output/C-practice.out";
  } else if (problem == "small") {
    inputFile  = "./input/C-small-2-attempt0.in";
    stdoutFile = "./output/C-small-2-attempt0.out";
  } else if (problem == "large") {
    inputFile  = "./input/C-large.in";
    stdoutFile = "./output/C-large.out";
  }

  fprintf(stderr, "Read from input: %s\n", inputFile.c_str());
  if (redirectStdoutToFile) fprintf(stderr, "Redirect stdout: %s\n", stdoutFile.c_str());
  if (redirectStdoutToFile) fprintf(stderr, "Redirect stderr: %s\n", stderrFile.c_str());

  assert(freopen(inputFile.c_str(), "r", stdin) != nullptr);
  if (redirectStdoutToFile) freopen(stdoutFile.c_str(), "w", stdout);
  if (redirectStderrToFile) freopen(stderrFile.c_str(), "w", stderr);

  int T = 0;
  string line;
  {
    getline(cin, line);
    istringstream is(line);
    is >> T;
  }

  cerr << T << endl;

  for (int testCase = 1; testCase <= T; ++testCase) {
    printf("Case #%d: ", testCase);
    Solve();
    printf("\n");

    fprintf(stderr, "Finished: #%d\n\n", testCase);
  }

  cerr << "Finished all test cases\n\n";

  return 0;
}

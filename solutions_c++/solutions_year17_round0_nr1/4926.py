#include <bits/stdc++.h>

using namespace std;

void Solve() {
  string S;
  int K;
  cin >> S >> K;

  bool canSolve = true;
  int countReverse = 0;
  for (int i = 0; i < S.length(); i++) {
    if (S[i] == '+') continue;

    if (i + K - 1 >= S.length()) {
      canSolve = false;
      break;
    }

    for (int j = 0; j < K; j++) {
      S[i + j] = (S[i + j] == '+') ? '-' : '+';
    }
    countReverse++;
  }

  if (canSolve) {
    printf("%d", countReverse);
  } else {
    printf("IMPOSSIBLE");
  }
}

int main(int argc, char **argv) {
  (void)argc;
  (void)argv;

  const string problem = "large"; // practice, small, large
  const bool redirectStdoutToFile = true;
  const bool redirectStderrToFile = true;

  string inputFile = "";
  string stdoutFile = "";
  string stderrFile = "./output/A.stderr";

  if (problem == "practice") {
    inputFile  = "./input/A-practice.in";
    stdoutFile = "./output/A-practice.out";
  } else if (problem == "small") {
    inputFile  = "./input/A-small-attempt0.in";
    stdoutFile = "./output/A-small-attempt0.out";
  } else if (problem == "large") {
    inputFile  = "./input/A-large.in";
    stdoutFile = "./output/A-large.out";
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

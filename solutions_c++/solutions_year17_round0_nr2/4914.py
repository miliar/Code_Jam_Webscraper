#include <bits/stdc++.h>

using namespace std;

void Solve() {
  string s;
  cin >> s;

  string t;
  for (int i = s.length() - 2; i >= 0; i--) {
    if (s[i] > s[i + 1]) {
      s[i]--;
      for (int j = i + 1; j < s.length(); j++) {
        s[j] = '9';
      }
    }
  }

  stringstream ss;
  ss << s;

  int64_t res;
  ss >> res;

  cout << res;
}

int main(int argc, char **argv) {
  (void)argc;
  (void)argv;

  const string problem = "large"; // practice, small, large
  const bool redirectStdoutToFile = true;
  const bool redirectStderrToFile = true;

  string inputFile = "";
  string stdoutFile = "";
  string stderrFile = "./output/B.stderr";

  if (problem == "practice") {
    inputFile  = "./input/B-practice.in";
    stdoutFile = "./output/B-practice.out";
  } else if (problem == "small") {
    inputFile  = "./input/B-small-attempt0.in";
    stdoutFile = "./output/B-small-attempt0.out";
  } else if (problem == "large") {
    inputFile  = "./input/B-large.in";
    stdoutFile = "./output/B-large.out";
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

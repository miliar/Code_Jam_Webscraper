#include <bits/stdc++.h>

using namespace std;

double D;
double N;

double K[1010];
double S[1010];

void Input() {
  cin >> D;
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> K[i] >> S[i];
    cerr << K[i] << " " << S[i] << endl;
  }
}

void Solve() {
  double l = 0.0, r = 1e29;

  for (int i = 0; i < 4000; i++) {
    double m = (l + r) / 2;

    double t = D / m;

    bool ok = true;
    for (int j = 0; j < N; j++) {
      double pos = K[j] + S[j] * t;
      if (pos < D) {
        ok = false;
        break;
      }
    }

    if (ok) {
      l = m;
    } else {
      r = m;
    }
  }

  printf("%8f", l);
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
    inputFile = "./input/A-practice.in";
    stdoutFile = "./output/A-practice.out";
  } else if (problem == "small") {
    inputFile = "./input/A-small-attempt1.in";
    stdoutFile = "./output/A-small-attempt1.out";
  } else if (problem == "large") {
    inputFile = "./input/A-large.in";
    stdoutFile = "./output/A-large.out";
  }

  fprintf(stderr, "Read from input: %s\n", inputFile.c_str());
  if (redirectStdoutToFile)
    fprintf(stderr, "Redirect stdout: %s\n", stdoutFile.c_str());
  if (redirectStdoutToFile)
    fprintf(stderr, "Redirect stderr: %s\n", stderrFile.c_str());

  assert(freopen(inputFile.c_str(), "r", stdin) != nullptr);
  if (redirectStdoutToFile)
    freopen(stdoutFile.c_str(), "w", stdout);
  if (redirectStderrToFile)
    freopen(stderrFile.c_str(), "w", stderr);

  int T = 0;
  string line;
  {
    getline(cin, line);
    istringstream is(line);
    is >> T;
  }

  cerr << T << endl;

  for (int testCase = 1; testCase <= T; ++testCase) {
    Input();
    printf("Case #%d: ", testCase);
    Solve();
    printf("\n");

    fprintf(stderr, "Finished: #%d\n\n", testCase);
  }

  cerr << "Finished all test cases\n\n";

  return 0;
}

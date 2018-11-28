#include <bits/stdc++.h>

using namespace std;

int N, K;
vector<pair<int64_t, int64_t>> RH;

int64_t dp[1100][1100];

void Input() {
  cin >> N >> K;
  RH.clear();
  RH.resize(N);
  for (int i = 0; i < N; i++) {
    cin >> RH[i].first >> RH[i].second;
  }
  sort(RH.begin(), RH.end());
}

void Solve() {
  memset(dp, 0LL, sizeof(dp));
  long double res = 0;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j <= K; j++) {
      dp[i + 1][j + 1] = dp[i][j + 1];
    }
    for (int j = 0; j <= min(i, K - 1); j++) {
      int64_t now = dp[i][j] + RH[i].first * RH[i].second * 2;
      if (now > dp[i + 1][j + 1]) {
        dp[i + 1][j + 1] = now;
      }
      if (j + 1 == K) {
        res = max(res, (long double)now + RH[i].first * RH[i].first);
      }
    }
    assert(dp[i][0] == 0);
  }
  printf("%.8Lf", res * M_PI);
}

int main(int argc, char **argv) {
  (void)argc;
  (void)argv;

  const string problem            = "large";  // practice, small, large
  const bool redirectStdoutToFile = true;
  const bool redirectStderrToFile = true;

  string inputFile  = "";
  string stdoutFile = "";
  string stderrFile = "./output/A.stderr";

  if (problem == "practice") {
    inputFile  = "./input/A-practice.in";
    stdoutFile = "./output/A-practice.out";
  } else if (problem == "small") {
    inputFile  = "./input/A-small-attempt2.in";
    stdoutFile = "./output/A-small-attempt2.out";
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
    Input();
    printf("Case #%d: ", testCase);
    Solve();
    printf("\n");

    fprintf(stderr, "Finished: #%d\n\n", testCase);
  }

  cerr << "Finished all test cases\n\n";

  return 0;
}

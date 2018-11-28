#include <bits/stdc++.h>

using namespace std;

int H;
int W;
string A[30];
string childs;
vector<int> xs;
vector<int> ys;

void Input() {
  cin >> H >> W;
  for (int i = 0; i < H; i++) {
    cin >> A[i];
  }

  childs = "";
  xs.clear();
  ys.clear();
  for (int y = 0; y < H; y++) {
    for (int x = 0; x < W; x++) {
      if (A[y][x] != '?') {
        childs += A[y][x];
        xs.push_back(x);
        ys.push_back(y);
      }
    }
  }
}

void Solve() {
  for (int y = 0; y < H; y++) {
    for (int x = 0; x < W; x++) {
      char c = A[y][x];
      if (c == '?') continue;
      for (int x2 = x - 1; x2 >= 0; x2--) {
        if (A[y][x2] == '?') {
          A[y][x2] = c;
        } else {
          break;
        }
      }
      for (int x2 = x + 1; x2 < W; x2++) {
        if (A[y][x2] == '?') {
          A[y][x2] = c;
        } else {
          break;
        }
      }
    }
  }
  for (int y = 0; y < H; y++) {
    char c = A[y][0];
    if (c == '?') continue;
    for (int y2 = y - 1; y2 >= 0; y2--) {
      if (A[y2][0] != '?') break;
      A[y2] = A[y];
    }
    for (int y2 = y + 1; y2 < H; y2++) {
      if (A[y2][0] != '?') break;
      A[y2] = A[y];
    }
  }

  for (int y = 0; y < H; y++) {
    cout << A[y] << endl;
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
    Input();
    printf("Case #%d:\n", testCase);
    Solve();

    fprintf(stderr, "Finished: #%d\n\n", testCase);
  }

  cerr << "Finished all test cases\n\n";

  return 0;
}

//============================================================================
// Name        : gcj.cpp
// Author      : Boleyn Su
// Version     :
// Copyright   : All Rights Reserved
// Description : Hello World in C++, Ansi-style
//============================================================================

// BEGIN gcj.h
#ifdef CLOUD
#include <mpi.h>
#include <cassert>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using namespace MPI;
using namespace std;

template <typename S>
void run(string in, string out) {
  ifstream cin(in);
  static char buf[1 << 25];
  Init();
  int nodes = COMM_WORLD.Get_size();
  int id = COMM_WORLD.Get_rank();

  int T;
  cin >> T;
  vector<string> ans(T);
  for (int t = 0; t < T; t++) {
    S::read(cin);
    if (t % nodes == id) {
      stringstream sout;
      sout << "Case #" << t + 1 << ":";
      S::solve(sout);
      ans[t] = sout.str();
    }
  }

  for (int t = 0; t < T; t++) {
    if (t % nodes == id) {
      if (id != 0) {
        int sz = ans[t].size();
        for (int i = 0; i < sz; i++) {
          buf[i] = ans[t][i];
        }
        assert(sz < sizeof(buf) / sizeof(*buf));
        COMM_WORLD.Send(&sz, 1, MPI_INT, 0, 0);
        COMM_WORLD.Send(buf, sz, MPI_CHAR, 0, 0);
      }
    } else {
      if (id == 0) {
        int sz;
        COMM_WORLD.Recv(&sz, 1, MPI_INT, t % nodes, 0);
        COMM_WORLD.Recv(buf, sz, MPI_CHAR, t % nodes, 0);
        ans[t] = string(buf, buf + sz);
      }
    }
  }
  if (id == 0) {
    ofstream cout(out);
    for (int t = 0; t < T; t++) {
      cout << ans[t];
    }
  }
  Finalize();
}

#else
#include <fstream>
#include <string>

using namespace std;

template <typename S>
void run(string in, string out) {
  ifstream cin(in);
  ofstream cout(out);
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    S::read(cin);
    cout << "Case #" << t << ":";
    S::solve(cout);
  }
}
#endif
// END gcj.h

#include <algorithm>
#include <cassert>
#include <iomanip>
#include <limits>
#include <set>
#include <utility>
#include <vector>

using namespace std;

int n, p;
int g[1 << 20];
int cnt[1 << 20];
int dp3[102][102];
int dp4[102][102][102];
int gao3() {
  for (int i = 0; i <= 100; i++) {
    for (int j = 0; j <= 100; j++) {
      dp3[i][j] = 0;
    }
  }
  for (int i = 0; i <= 100; i++) {
    for (int j = 0; j <= 100; j++) {
      for (int ii = 0; ii <= 3; ii++) {
        for (int jj = 0; jj <= 3; jj++) {
          if ((ii + jj != 0) && (ii + jj * 2) % 3 == 0 && i >= ii && j >= jj) {
            dp3[i][j] = max(dp3[i][j], dp3[i - ii][j - jj] + 1);
          }
        }
      }
    }
  }
  int ans = 0;
  for (int i = 0; i <= cnt[1]; i++) {
    for (int j = 0; j <= cnt[2]; j++) {
      ans = max(ans, dp3[i][j] + (i != cnt[1] || j != cnt[2]));
    }
  }
  return ans;
}
int gao4() {
  for (int i = 0; i <= 100; i++) {
    for (int j = 0; j <= 100; j++) {
      for (int k = 0; k <= 100; k++) {
        dp4[i][j][k] = 0;
      }
    }
  }
  for (int i = 0; i <= 100; i++) {
    for (int j = 0; j <= 100; j++) {
      for (int k = 0; k <= 100; k++) {
        for (int ii = 0; ii <= 4; ii++) {
          for (int jj = 0; jj <= 4; jj++) {
            for (int kk = 0; kk <= 4; kk++) {
              if ((ii + jj + kk != 0) && (ii + jj * 2 + kk * 3) % 4 == 0 &&
                  i >= ii && j >= jj && k >= kk) {
                dp4[i][j][k] =
                    max(dp4[i][j][k], dp4[i - ii][j - jj][k - kk] + 1);
              }
            }
          }
        }
      }
    }
  }
  int ans = 0;
  for (int i = 0; i <= cnt[1]; i++) {
    for (int j = 0; j <= cnt[2]; j++) {
      for (int k = 0; k <= cnt[3]; k++) {
        ans = max(ans,
                  dp4[i][j][k] + (i != cnt[1] || j != cnt[2] || k != cnt[3]));
      }
    }
  }
  return ans;
}

struct Solver {
  static void read(istream& cin) {
    cin >> n >> p;
    for (int i = 0; i < p; i++) {
      cnt[i] = 0;
    }
    for (int i = 0; i < n; ++i) {
      cin >> g[i];
      cnt[g[i] % p]++;
    }
  }
  static void solve(ostream& cout) {
    int ans;
    if (p == 2) {
      ans = cnt[0] + (cnt[1] + 1) / 2;
    } else if (p == 3) {
      ans = cnt[0] + gao3();
    } else if (p == 4) {
      ans = cnt[0] + gao4();
    } else {
      assert(false);
    }
    cout << " " << ans << endl;
  }
};

int main() {
  run<Solver>("in.txt", "out.txt");
  return 0;
}

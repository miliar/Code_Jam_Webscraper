#include <cstdio>
#include <ctime>
#include <iostream>
#include <vector>

using namespace std;

typedef long long int64;

#define DPRINT(x) cerr << __LINE__ << ": " << #x << " = " << x << endl;

template <class T1, class T2>
ostream& operator <<(ostream& os, const pair<T1, T2>& v);

template <class T>
ostream& operator <<(ostream& os, const vector<T>& v) {
    os << "[";
    for (typename vector<T>::const_iterator ii = v.begin(); ii != v.end(); ++ii) {
        if (ii != v.begin()) os << " ";
        os << *ii;
    }
    os << "]";
    return os;
}

template <class T1, class T2>
ostream& operator <<(ostream& os, const pair<T1, T2>& v) {
    os << "(" << v.first << " " << v.second << ")";
    return os;
}

const int kMinutes = 24*60;
const int kInf = 1e+9;

struct Test {
  int num_activities[2];
  vector<pair<int, int>> activities[2];
  bool free[2][kMinutes];
  int min_change[2][kMinutes/2 + 1][2][2];
  int ans;

  void read() {
    for (int i = 0; i < 2; i++) {
      scanf("%d", &num_activities[i]);
      activities[i].resize(num_activities[i]);
    }
    for (int i = 0; i < 2; i++)
      for (int j = 0; j < num_activities[i]; j++)
        scanf("%d %d", &activities[i][j].first, &activities[i][j].second);
  }

  void clear(int ind) {
    for (int i = 0; i <= kMinutes/2; i++) {
      min_change[ind][i][0][0] = kInf;
      min_change[ind][i][0][1] = kInf;
      min_change[ind][i][1][0] = kInf;
      min_change[ind][i][1][1] = kInf;
    }
  }

  // void print(int ind, int total_t) {
  //   printf("\nprinting for total_t=%d ind=%d\n", total_t, ind);
  //   for (int t = 0; t <= kMinutes/2; t++)
  //     for (int start = 0; start <= 1; start++)
  //       for (int last = 0; last <= 1; last++)
  //         if (min_change[ind][t][start][last] < kInf) {
  //           printf("seq_begin=%d seq_end=%d first_t=%d second_t=%d  ->  min_change=%d\n",
  //                  start, last, t, total_t - t, min_change[ind][t][start][last]);
  //         }
  // }

  void relax(int& dest, int src) {
    if (dest > src)
      dest = src;
  }

  void solve() {
    for (int i = 0; i < 2; i++)
      for (int j = 0; j < kMinutes; j++)
        free[i][j] = true;
    for (int i = 0; i < 2; i++)
      for (auto pii : activities[i])
        for (int j = pii.first; j < pii.second; j++)
          free[i][j] = false;

    int cur = 0;

    clear(cur);

    if (free[0][0]) min_change[cur][1][0][0] = 0;
    if (free[1][0]) min_change[cur][0][1][1] = 0;

    for (int t = 1; t < kMinutes; t++) {
      int prev = cur;
      cur ^= 1;

      clear(cur);

      for (int i = 0; i <= kMinutes/2; i++) {
        for (int j = 0; j < 2; j++) {
          int first = i, second = t - i;

          if (first < kMinutes/2 && free[0][t]) {
            relax(min_change[cur][first+1][j][0], min_change[prev][first][j][0]);
            relax(min_change[cur][first+1][j][0], min_change[prev][first][j][1] + 1);
          }
          if (second < kMinutes/2 && free[1][t]) {
            relax(min_change[cur][first][j][1], min_change[prev][first][j][0] + 1);
            relax(min_change[cur][first][j][1], min_change[prev][first][j][1]);
          }
        }
      }
    }

    ans = kInf;
    relax(ans, min_change[cur][kMinutes/2][0][0]);
    relax(ans, min_change[cur][kMinutes/2][1][1]);
    relax(ans, min_change[cur][kMinutes/2][0][1] + 1);
    relax(ans, min_change[cur][kMinutes/2][1][0] + 1);
  }

  void print(int num_test) {
    printf("Case #%d: %d\n", num_test, ans);
  }
};


int main() {
  //freopen("input.txt", "rt", stdin);
  freopen("B-large.in", "rt", stdin);
  freopen("B-large.out", "wt", stdout);

  int T;
  scanf("%d", &T);
  vector<Test> tests(T);
  for (int i = 0; i < T; i++)
    tests[i].read();

  #pragma omp parallel for
  for (int i = 0; i < T; i++) {
    clock_t start = clock();
    tests[i].solve();
    fprintf(stderr, "Solved test %d in %.3fs\n", i+1, float(clock() - start) / CLOCKS_PER_SEC);
  }

  for (int i = 0; i < T; i++)
    tests[i].print(i+1);

  return 0;
}

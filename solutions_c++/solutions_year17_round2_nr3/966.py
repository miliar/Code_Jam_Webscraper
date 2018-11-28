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

const int64 kInf = 1e+14;

struct Test {
  int N, Q;
  vector<int> max_dist, speed;
  vector<vector<int64>> dist;
  vector<int> src, dst;
  vector<double> ans;

  void read() {
    scanf("%d %d", &N, &Q);
    max_dist.resize(N);
    speed.resize(N);
    for (int i = 0; i < N; i++)
      scanf("%d %d", &max_dist[i], &speed[i]);

    dist.assign(N, vector<int64>(N, kInf));
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++) {
        int d;
        scanf("%d", &d);
        if (d >= 0)
          dist[i][j] = d;
      }

    src.resize(Q);
    dst.resize(Q);
    for (int i = 0; i < Q; i++) {
      scanf("%d %d", &src[i], &dst[i]);
      src[i]--;
      dst[i]--;
    }
  }

  void solve() {
    for (int k = 0; k < N; k++)
      dist[k][k] = 0;

    for (int k = 0; k < N; k++)
      for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
          if (dist[i][j] > dist[i][k] + dist[k][j])
            dist[i][j] = dist[i][k] + dist[k][j];

    vector<vector<double>> t(N, vector<double>(N, kInf));
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++)
        if (dist[i][j] <= max_dist[i])
          t[i][j] = static_cast<double>(dist[i][j]) / speed[i]; else
          t[i][j] = kInf;

    for (int k = 0; k < N; k++)
      for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
          if (t[i][j] > t[i][k] + t[k][j])
            t[i][j] = t[i][k] + t[k][j];

    for (int i = 0; i < Q; i++)
      ans.push_back(t[src[i]][dst[i]]);
  }

  void print(int num_test) {
    printf("Case #%d:", num_test);
    for (int i = 0; i < Q; i++)
      printf(" %lf", ans[i]);
    puts("");
  }
};


int main() {
  //freopen("input.txt", "rt", stdin);
  freopen("C-large.in", "rt", stdin);
  freopen("C-large.out", "wt", stdout);

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

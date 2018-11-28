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

struct Test {
  int D, N;
  vector<int> pos, speed;
  double ans;

  void read() {
    scanf("%d %d", &D, &N);
    pos.resize(N);
    speed.resize(N);
    for (int i = 0; i < N; i++)
      scanf("%d %d", &pos[i], &speed[i]);
  }

  void solve() {
    double last = 0;
    for (int i = 0; i < N; i++)
      last = max(last, double(D-pos[i])/speed[i]);
    ans = D / last;
  }

  void print(int num_test) {
    printf("Case #%d: %lf\n", num_test, ans);
  }
};


int main() {
  //freopen("input.txt", "rt", stdin);
  freopen("A-large.in", "rt", stdin);
  freopen("A-large.out", "wt", stdout);

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

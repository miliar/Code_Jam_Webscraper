#include <cstdio>
#include <ctime>
#include <cmath>
#include <iostream>
#include <vector>
#include <queue>

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
  int N, K;
  double U;
  priority_queue<pair<double, int>> Q;
  double ans;

  void read() {
    scanf("%d %d %lf", &N, &K, &U);
    for (int i = 0; i < N; i++) {
      double p;
      scanf("%lf", &p);
      Q.push(make_pair(-p, 1));
    }
  }

  void solve() {
    while (true) {
      auto least = Q.top();
      Q.pop();

      if (Q.empty()) {
        least.first = -(-least.first + U / least.second);
        U = 0;
        Q.push(least);
        break;
      }

      auto next = Q.top();
      double delta = -next.first - (-least.first);
      if (delta * least.second > U) {
        least.first = -(-least.first + U / least.second);
        U = 0;
        Q.push(least);
        break;
      } else {
        U -= delta * least.second;
        Q.pop();
        next.second += least.second;
        Q.push(next);
      }
    }

    ans = 1.0;
    while (!Q.empty()) {
      auto least = Q.top();
      Q.pop();
      ans *= pow(-least.first, least.second);
    }
  }

  void print(int num_test) {
    printf("Case #%d: %.9lf\n", num_test, ans);
  }
};


int main() {
  //freopen("input.txt", "rt", stdin);
  freopen("C-small-1-attempt1.in", "rt", stdin);
  freopen("C-small-1-attempt1.out", "wt", stdout);

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

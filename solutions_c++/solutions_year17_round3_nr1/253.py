#include <cstdio>
#include <cmath>
#include <ctime>
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const double kPi = 2.0 * acos(0);

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

bool cmp(const pair<int, int>& a, const pair<int, int>& b) {
  if (a.first != b.first)
    return a.first < b.first;
  return a.second < b.second;
}

struct Test {
  int N, K;
  vector<pair<int, int>> pancake;
  double ans;

  void read() {
    scanf("%d %d", &N, &K);
    pancake.resize(N);
    for (int i = 0; i < N; i++)
      scanf("%d %d", &pancake[i].first, &pancake[i].second);
  }

  void solve() {
    sort(pancake.begin(), pancake.end(), cmp);
    ans = 0;
    double in_q = 0;
    priority_queue<double> Q;

    for (int i = 0; i < N; i++) {
      double cur = 2*kPi*pancake[i].first*pancake[i].second;
      if (Q.size() == K-1) {
        ans = max(ans, in_q + kPi * pancake[i].first * pancake[i].first + cur);
      }
      Q.push(-cur);
      in_q += cur;
      if (Q.size() == K) {
        in_q += Q.top();
        Q.pop();
      }
    }
  }

  void print(int num_test) {
    printf("Case #%d: %.9lf\n", num_test, ans);
  }
};


int main() {
  // freopen("input.txt", "rt", stdin);
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

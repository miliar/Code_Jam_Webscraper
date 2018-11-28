#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
const ld PI = acosl(-1.);

mutex cerr_lock;
class LOG {
public:
  template<class T>
    LOG& operator<<(const T& value) {
      ss_ << value;
      return *this;
    }

  ~LOG() {
    lock_guard<mutex> lock(cerr_lock);
    cerr << ss_.str() << '\n';
    cerr.flush();
  }
private:
  stringstream ss_;
};

const double eps = 1e-15;
class TestImpl {
public:
  void Input() {
    cin >> n >> k;
    cin >> u;
    for (int i = 0; i < n; ++i) {
      double x; cin >> x;
      p.push_back(x);
    }
  }

  void Solve() {
    sort(begin(p), end(p));
    p.push_back(1.);

    while (u > eps) {
      int count = 1;
      for (int i = 1; i < n; ++i) {
        if (fabsl(p[i] - p[0]) < eps) {
          ++count;
        } else {
          break;
        }
      }
      double dx = min(p[count] - p[0], u / count);
      double result = p[0] + dx;
      for (int i = 0; i < count; ++i) {
        p[i] = result;
      }
      u -= dx * count;
    }

    answer = 1.;
    for (int i = 0; i < n; ++i) {
      //answer += logl(p[i]);
      answer *= p[i];
    }
  }

  void Output() {
    cout.precision(20);
    cout << fixed;
    //cout << expl(answer) << endl;
    cout << answer << endl;
  }

private:
  int n, k;
  double u;
  vector<double> p;
  double answer = 0;
};

class Test {
public:
  void Input(int testNo) {
    testNo_ = testNo;
    impl_.reset(new TestImpl);
    impl_->Input();

    LOG() << "Test #" << testNo_ << " is inputted";
  }

  void Solve() {
    impl_->Solve();
    LOG() << "Test #" << testNo_ << " is solved";
  }

  void Output() {
    printf("Case #%d: ", testNo_);
    impl_->Output();
    LOG() << "Test #" << testNo_ << " is outputted";
  }

private:
  int testNo_;
  unique_ptr<TestImpl> impl_;
};

int main() {
  constexpr int N_THREADS = 4;
  vector<Test> tests;
  queue<int> not_solved;

  int T;
  scanf("%d\n", &T);
  tests.resize(T);
  for (int i = 0; i < T; ++i) {
    tests[i].Input(i + 1);
    not_solved.push(i);
  }

  mutex test_mutex;
  vector<thread> threads;
  for (int i = 0; i < N_THREADS; ++i) {
    threads.emplace_back(
        [&](){
        bool done = false;
        do {
        int next_test = -1;
        test_mutex.lock();
        if (not_solved.empty()) {
        done = true;
        } else {
        next_test = not_solved.front();
        not_solved.pop();
        }
        test_mutex.unlock();
        if (!done) {
        tests[next_test].Solve();
        }
        } while (!done);
        });
  }

  for (auto& thread : threads) {
    thread.join();
  }

  for (auto& test : tests) {
    test.Output();
  }

  return 0;
}

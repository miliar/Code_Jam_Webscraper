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

class TestImpl {
public:
  void Input() {
    scanf("%d%d", &n, &k);
    pancakes.reserve(n);
    for (int i = 0; i < n; ++i) {
      int x, y;
      scanf("%d%d", &x, &y);
      pancakes.emplace_back(x, y);
    }
  }

  void Solve() {
    sort(begin(pancakes), end(pancakes));
    answer = 0;
    priority_queue<ll> q;
    ll qsum = 0;
    for (int i = 0; i < n; ++i) {
      ll r = pancakes[i].first;
      ll h = pancakes[i].second;
      if (int(q.size()) >= k - 1) {
        answer = max(answer, r * r + qsum + r * h * 2);
      }
      q.push(-r * h * 2);
      qsum += r * h * 2;
      while (int(q.size()) > k - 1) {
        ll x = q.top(); q.pop();
        qsum += x;
      }
    }
  }

  void Output() {
    cout.precision(20);
    cout << fixed;
    cout << ld(answer) * PI << endl;
  }

private:
  int n, k;
  vector<pair<int, int>> pancakes;
  long long answer = 0;
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

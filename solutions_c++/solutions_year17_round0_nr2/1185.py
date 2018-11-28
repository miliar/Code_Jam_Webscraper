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
    cin >> n;
  }

  ll calc(const vector<int>& d) {
    ll result = 0;
    for (size_t i = 1; i < d.size(); ++i)
      if (d[i] < d[i - 1]) return -1;
    for (size_t i = 0; i < d.size(); ++i) {
      result = result * 10 + d[i];
    }
    return result;
  }

  void Solve() {
    ans = 0;
    if (n < 10) {
      ans = n;
      return;
    }

    vector<int> d;
    ll m = n;
    while (m) {
      d.push_back(m % 10);
      m /= 10;
    }
    reverse(begin(d), end(d));

    ans = max(ans, calc(d));
    for (size_t who = 0; who < d.size(); ++who) {
      if (d[who] == 0) continue;
      vector<int> dd = d;
      dd[who]--;
      for (size_t j = who + 1; j < dd.size(); ++j) {
        dd[j] = 9;
      }
      ans = max(ans, calc(dd));
    }
  }

  void Output() {
    cout << ans << endl;
  }

private:
  ll n;
  ll ans;
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

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
    scanf("%d%d", &ac, &aj);
    for (int i = 0; i < ac; ++i) {
      int from, to;
      cin >> from >> to;
      acs.emplace_back(from, to);
    }
    for (int i = 0; i < aj; ++i) {
      int from, to;
      cin >> from >> to;
      ajs.emplace_back(from, to);
    }
  }

  void Solve() {
    vector<int> who(SECONDS + 20);
    for (size_t i = 0; i < who.size(); ++i) {
      who[i] = 3;
    }
    for (size_t i = 0; i < acs.size(); ++i) {
      int from = acs[i].first;
      int to = acs[i].second;
      for (int j = from; j < to; ++j) {
        assert(who[j] & 1);
        who[j] -= 1;
      }
    }
    for (size_t i = 0; i < ajs.size(); ++i) {
      int from = ajs[i].first;
      int to = ajs[i].second;
      for (int j = from; j < to; ++j) {
        assert(who[j] & 2);
        who[j] -= 2;
      }
    }

    memset(f, 63, sizeof(f));
    bool can_first_0 = who[0] & 1;
    bool can_second_0 = who[0] & 2;
    bool can_first_last = who[SECONDS - 1] & 1;
    bool can_second_last = who[SECONDS - 1] & 2;

    f[0][1][0][0] = (can_first_0 && can_first_last) ? 0 : 1e9;
    f[0][1][0][1] = (can_first_0 && can_second_last) ? 1 : 1e9;
    f[0][0][1][0] = (can_second_0 && can_first_last) ? 1 : 1e9;
    f[0][0][1][1] = (can_second_0 && can_second_last) ? 0 : 1e9;
    for (int t = 1; t < SECONDS; ++t) {
      for (int current_spend = 0; current_spend <= SECONDS; ++current_spend) {
        if (current_spend > t + 2) continue;

        for (int last = 0; last < 2; ++last) {
          for (int current = 0; current < 2; ++current) {
            if (!(who[t] & (1 << current))) continue;

            for (int previous = 0; previous < 2; ++previous) {
              int add = (previous == current ? 0 : 1);
              int previous_spend = (current == 0 ? current_spend - 1 : current_spend);
              if (previous_spend < 0) continue;
              f[t][current_spend][current][last] = min(f[t][current_spend][current][last], f[t - 1][previous_spend][previous][last] + add);
            }
          }
        }
      }
    }

    answer = 1e9;
    if (can_first_last) answer = min(answer, f[SECONDS - 1][SECONDS / 2][0][0]);
    if (can_second_last) answer = min(answer, f[SECONDS - 1][SECONDS / 2][1][1]);
  }

  void Output() {
    cout << answer << endl;
  }

private:
  const static int SECONDS = 60 * 24;
  int ac, aj;
  vector<pair<int, int>> acs;
  vector<pair<int, int>> ajs;
  int answer;
  int f[SECONDS + 2][SECONDS + 2][2][2];
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

#include <iostream>
#include <string>
#include <vector>
#include <sstream>

int max_side(int n) {
  if (n % 2) {
    return n / 2;
  }
  return (n - 1) / 2 + 1;
}

int min_side(int n) {
  return (n - 1) / 2;
}

#include <queue>
class ProblemBF {
  std::priority_queue<unsigned long long> n_;
  unsigned long long k_;
public:
  ProblemBF(unsigned long long n, unsigned long long k):n_(), k_(k) {
    n_.push(n);
  }

  std::string solve() {
    if (k_ <= 1) {
      std::ostringstream oss;
      oss << max_side(n_.top()) << " " << min_side(n_.top());
      return oss.str();
    }
    --k_;
    unsigned long long t = n_.top();
    n_.pop();
    n_.push(max_side(t));
    n_.push(min_side(t));
    return solve();
  }
};

class Problem {
  unsigned long long n_;
  unsigned long long k_;
public:
  Problem(unsigned long long n, unsigned long long k):n_(n), k_(k) {
  }
  ~Problem() {}

  std::string solve() {
    if (k_ <= 1) {
      std::ostringstream oss;
      oss << max_side(n_) << " " << min_side(n_);
      return oss.str();
    }
    if (k_ & 1) {
      n_ = min_side(n_);
    } else {
      n_ = max_side(n_);
    }
    k_ /= 2;
    return solve();
  }
};

Problem parse(const std::string& s) {
  unsigned long long n, k;
  std::istringstream iss(s);
  iss >> n;
  iss >> k;
  return Problem(n, k);
}

int main() {
  int n_input;
  {
    std::string ln;
    std::getline(std::cin, ln);
    std::istringstream(ln) >> n_input;
  }
  for (int i=1;i <= n_input;++i) {
    std::string ln;
    std::getline(std::cin, ln);
    std::cout << "Case #" << i << ": " << parse(ln).solve() << std::endl;
  }
}

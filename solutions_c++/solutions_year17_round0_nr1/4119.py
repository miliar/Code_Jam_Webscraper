#include <iostream>
#include <string>
#include <vector>
#include <sstream>

class Problem {
  int flipper_size_;
  std::vector<bool> pancakes_;

 public:
  Problem(int flipper_size, const std::string& pancakes):
      flipper_size_(flipper_size),
      pancakes_() {
    for (std::string::const_iterator it = pancakes.begin(); it != pancakes.end(); ++it) {
      pancakes_.push_back(*it == '+');
    }
  }
  ~Problem() {}

  std::string solve() {
    size_t flipcount = 0;
    for (size_t i=0;i <= pancakes_.size() - flipper_size_;++i) {
      if (!pancakes_[i]) {
        for (size_t j=0;j < flipper_size_; ++j) {
          pancakes_[i+j] = !pancakes_[i+j];
        }
        flipcount++;
      }
    }
    for (size_t i=pancakes_.size() - flipper_size_;i<pancakes_.size();++i) {
      if (!pancakes_[i]) {
        return std::string("IMPOSSIBLE");
      }
    }
    std::ostringstream oss;
    oss << flipcount;
    return oss.str();
  }

};

Problem parse(const std::string& s) {
  std::istringstream is(s);
  std::string pans;
  int flip;
  is >> pans;
  is >> flip;
  return Problem(flip, pans);
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

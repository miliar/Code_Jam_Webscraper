#include <iostream>
#include <string>
#include <vector>
#include <sstream>

class Problem {
  std::vector<int> digits_;
public:
  Problem(const std::string& s):digits_() {
    for (std::string::const_iterator iter = s.begin(); iter != s.end(); ++iter) {
      digits_.push_back(static_cast<int>((*iter) - '0'));
    }
  }
  ~Problem() {}

  std::string solve() {
    for (size_t i=digits_.size()-1;i>0;--i) {
      if (digits_[i] < digits_[i-1]) {
        digits_[i-1]--;
        for (size_t j=i;j < digits_.size(); ++j) {
          digits_[j] = 9;
        }
      }
    }
    bool leading = true;
    std::ostringstream oss;
    for (std::vector<int>::iterator it=digits_.begin();it!=digits_.end(); ++it) {
      if (leading) {
        if (*it > 0) {
          leading = false;
          oss << *it;
        }
      } else {
        oss << *it;
      }
    }
    return oss.str();
  }
};

Problem parse(const std::string& s) {
  return Problem(s);
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

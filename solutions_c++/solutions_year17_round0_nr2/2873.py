#include <iostream>
#include <vector>
#include <sstream>

using std::vector;

int main() {
  int nTests;
  std::cin >> nTests;
  std::string line;
  std::getline(std::cin, line);

  for (size_t nTest = 0; nTest < nTests; ++nTest) {
    std::getline(std::cin, line);

    std::vector<int> digits;
    for (auto digit : line) {
      digits.push_back(digit - '0');
    }

    int last_asc_idx = 0;
    int first_desc_idx = -1;
    for (int cursor = 0; cursor < digits.size(); cursor++) {
      if (cursor == (digits.size() - 1)) {
	break;
      } else {
	int digit = digits[cursor];
	int next_digit = digits[(cursor + 1)];
	if (digit == next_digit) {
	  // nothing
	} else if (digit < next_digit) {
	  if (first_desc_idx == -1) {
	    last_asc_idx = cursor + 1;
	  }
	} else /* digit > next_digit */ {
	  if (first_desc_idx == -1) {
	    first_desc_idx = cursor + 1;
	  }
	}
      }
    }
    
    if (first_desc_idx == -1) {
      // Do nothing, its good
    } else {
      digits[last_asc_idx] = digits[last_asc_idx] - 1;
      for (size_t edit = (last_asc_idx+1); edit < digits.size(); ++edit) {
	digits[edit] = 9;
      }
    }

    std::cout << "Case #" << (nTest + 1) << ": ";

    for (auto digit : digits) {
      if (digit == 0) {
	// leading only
      } else {
	std::cout << digit;
      }
    }
    std::cout << std::endl;
  }
}

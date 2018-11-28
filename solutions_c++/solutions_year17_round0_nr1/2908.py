#include <iostream>

int main() {
  int nTests;
  std::cin >> nTests;
  for (size_t nTest = 0; nTest < nTests; ++nTest) {
    std::string pancakes;
    int K;
    std::cin >> pancakes >> K;

    auto happy = [](const char& c) { return c == '+'; };
    auto flip = [](char& c) { 
      c = (c == '+' ? '-' : '+');
    };

    size_t i = 0;
    int flips = 0;
    for (; i < (pancakes.size() - (K - 1)); ++i) {
      if (!happy(pancakes[i])) {
	flips++;
	for (size_t j = i; j < (i + K); ++j) {
	  flip(pancakes[j]);
	}
      }
    }
    
    bool valid = true;
    for (; i < pancakes.size(); ++i) {
      if (!happy(pancakes[i])) {
	valid = false;
	break;
      }
    }
    
    std::cout << "Case #" << (nTest + 1) << ": ";
    if (valid) {
      std::cout << flips;
    } else {
      std::cout << "IMPOSSIBLE";
    }
    std::cout << std::endl;
  }
}


#include <cstdint>
#include <iostream>
#include <vector>

using namespace std;

uint64_t MAX = 1e18;
std::vector<uint64_t> tidyNumbers;

bool isTidyNumber(uint64_t num) {
  // TODO optimize
  uint64_t lastDigit = num % 10;
  uint64_t remaining = num / 10;
  uint64_t tempDigit = lastDigit;
  while (remaining > 0) {
    tempDigit = remaining % 10;
    if (tempDigit > lastDigit) {
      return false;
    }
    lastDigit = tempDigit;
    remaining /= 10;
  }
  return true;
}

uint64_t lastTidyNumber(uint64_t num) {
  if (isTidyNumber(num)) {
    return num;
  }
  vector<uint64_t>::iterator candidate = tidyNumbers.begin();
  while (*candidate < num) candidate++;
  return *(candidate - 1);
}

int main() {
  // Compute all possibilities
  tidyNumbers.reserve(1e7);
  for (uint64_t i = 1; i < 10; i++) tidyNumbers.push_back(i);

  vector<uint64_t>::iterator front = tidyNumbers.begin();
  vector<uint64_t>::iterator back = tidyNumbers.end();

  // digit loop
  for (uint64_t i = 10; i <= MAX; i *= 10) {
    // 1xx-9xx loop    
    for (uint64_t d = i; d < i * 10; d += i) {
      for (vector<uint64_t>::iterator here = front; here != back; ++here) {
        uint64_t candidate = d + *here;
        if (isTidyNumber(candidate)) { // TODO optimize just look at first digits, rest is guaranteed.
          tidyNumbers.push_back(candidate);
        }
      }
    }
    front = back++;
    back = tidyNumbers.end();
  }

  int attempt;
  uint64_t line;
  cin >> attempt;
  for (int i = 1; i <= attempt; i++) {
    cin >> line;
    cout << "Case #" << i << ": " << lastTidyNumber(line) << endl;
  }

  return 0;
}
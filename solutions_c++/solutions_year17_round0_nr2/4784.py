#include <iostream>
#include <algorithm>

using namespace std;

bool isTidy(const std::string& num) {
  for (int i = 0; i < num.size() - 1; ++i) {
    if (num[i+1] < num[i]) {
      return false;
    }
  }
  return true;
}

std::string findHighestTidyNumber(/* in/out */std::string& numberString) {
  // convert to vector of ints
  std::vector<unsigned> num(numberString.size());
  for (unsigned i = 0; i < num.size(); ++i) {
    num[i] = numberString[i] - '0';
  }

  // operate on vector of ints
  for (unsigned index = 0; index < num.size() - 1; ++index) {
    if (num[index + 1] < num[index]) {
      num[index]--;
      std::fill(num.begin() + index + 1, num.end(), 9);
      break;
    }
  }

  // convert back to string
  std::string result;
  for (unsigned i = 0; i < num.size(); ++i) {
    if (result.size() == 0 && num[i] == 0) {
      continue;
    }
    result += '0' + num[i];
  }

  if (!isTidy(result)) {
    return findHighestTidyNumber(result);
  } else {
    return result;
  }
}

int main() {
  unsigned int numCases;
  std::cin >> numCases;
  for (unsigned int i = 0; i < numCases; ++i) {
    std::string number;
    std::cin >> number;

    std::string highestTidyNumber = findHighestTidyNumber(number);

    cout << "Case #" << i + 1 << ": " << highestTidyNumber;
    cout << endl;
  }
  return 0;
}

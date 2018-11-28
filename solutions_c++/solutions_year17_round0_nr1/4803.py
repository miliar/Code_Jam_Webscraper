#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

static const char* HAPPY = "+";
static const char* SAD = "-";

static const int IMPOSSIBLE = -1;

inline bool areAllPancakesHappy(const vector<bool>& pancakeStates) {
  for (auto state: pancakeStates) {
    if (!state) {
      return false;
    }
  }
  return true;
}

inline void flip(vector<bool>::iterator it, unsigned flipperSize) {
  for (int i=0; i<flipperSize; ++i) {
    *it = !*it;
    it++;
  }
}

void printPancakeStates(const vector<bool>& pancakeStates) {
  cout << "Pancake states: ";
  for (auto state: pancakeStates) {
    cout << state ? "+" : "-";
  }
  cout << endl;
}

int calculateNumFlips(vector<bool>& pancakeStates, unsigned flipperSize) {
  // if (pancakeStates.size() == flipperSize) {
  //   // Only possible if they are all happy to begin with
  //   return areAllPancakesHappy(pancakeStates) ? 0 : IMPOSSIBLE;
  // }

  bool evenNumFlipsRequired = true;
  for (auto pancakeState: pancakeStates) {
    evenNumFlipsRequired = pancakeState ? evenNumFlipsRequired : !evenNumFlipsRequired;
  }

  // Now need to calculate actual num of flips required then divide by flipper size - calculate actual num of
  // flips required by lowest number of flips divisible by flipper size
  unsigned pancakeIndex = 0;
  unsigned numPancakes = pancakeStates.size();
  int numFlips = 0;
  while (pancakeIndex <= numPancakes - flipperSize) {
    // check if pancake under index is already happy, flip if not
    // printPancakeStates(pancakeStates);
    if (!pancakeStates[pancakeIndex]) {
      flip(pancakeStates.begin() + pancakeIndex, flipperSize);
      numFlips++;
    }
    pancakeIndex++;
  }
  return areAllPancakesHappy(pancakeStates) ? numFlips : IMPOSSIBLE;
}

int main() {
  unsigned int numCases;
  std::cin >> numCases;
  for (unsigned int i = 0; i < numCases; ++i) {
    std::string pancakeInputStates;
    std::cin >> pancakeInputStates;
    unsigned flipperSize;
    std::cin >> flipperSize;
    vector<bool> pancakeStates(pancakeInputStates.size());
    for (int j = 0; j < pancakeInputStates.size(); ++j) {
      pancakeStates[j] = (pancakeInputStates[j] == '+') ? true : false;
    }
    int numFlips = calculateNumFlips(pancakeStates, flipperSize);
    if (numFlips == IMPOSSIBLE) {
      cout << "Case #" << i + 1 << ":" << " " << "IMPOSSIBLE";
    } else {
      cout << "Case #" << i + 1 << ":" << " " << numFlips;
    }
    cout << endl;
  }
  return 0;
}

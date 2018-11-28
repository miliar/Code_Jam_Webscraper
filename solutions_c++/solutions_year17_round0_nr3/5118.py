#include <algorithm>
#include <iostream>
#include <list>
#include <vector>

#include <cstdint>

struct Spaces {
  int64_t spaces;
  int64_t num;
};

struct LR {
  int64_t left;
  int64_t right;
};

int64_t maxLR(const LR& lr) {
  return std::max(lr.left, lr.right);
}

int64_t minLR(const LR& lr) {
  return std::min(lr.left, lr.right);
}

void dumpPos(const std::vector<int64_t> &pos) {
  for (auto p: pos) {
    std::cerr << p << " ";
  }
  std::cerr << std::endl;
}

LR solve(int64_t numStalls, int64_t numPeople) {
  std::list<Spaces> spaces;
  spaces.push_front(Spaces{numStalls, 1});
  LR lr = {-1, -1};
  for (int64_t i = 0; i < numPeople; ++i) {
    auto &curSpaces = spaces.front();
    const auto pos = (curSpaces.spaces - 1)/2;
    const auto left = pos;
    const auto right = curSpaces.spaces - pos - 1;
    lr.left = left;
    lr.right = right;

    if (curSpaces.num == 1) {
      // remove it
      spaces.pop_front();
    } else {
      --curSpaces.num;
    }

    // add left
    {
      auto curSpaces = spaces.begin();
      while (curSpaces != spaces.end() && curSpaces->spaces > left) {
        ++curSpaces;
      }
      if (curSpaces != spaces.end()) {
        if (curSpaces->spaces == left) {
          ++curSpaces->num;
        } else {
          spaces.insert(curSpaces, Spaces{left, 1});
        }
      } else {
        spaces.push_back(Spaces{left, 1});
      }
    }
    // add right
    {
      auto curSpaces = spaces.begin();
      while (curSpaces != spaces.end() && curSpaces->spaces > right) {
        ++curSpaces;
      }
      if (curSpaces != spaces.end()) {
        if (curSpaces->spaces == right) {
          ++curSpaces->num;
        } else {
          spaces.insert(curSpaces, Spaces{right, 1});
        }
      } else {
        spaces.push_back(Spaces{right, 1});
      }
    }

  }
  return lr;
}

int main() {
  int numCases = 0;
  std::cin >> numCases;
  for (int i = 0; i < numCases; i++) {
    int64_t n, k;
    std::cin >> n;
    std::cin >> k;

    auto result = solve(n, k);
    std::cout << "Case #" << i + 1 << ": " << maxLR(result) << " " << minLR(result) << std::endl;
  }
  return 0;
}

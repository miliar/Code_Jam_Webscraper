// 2017 Round 1B, Problem B. Stable Neigh-bors
// Copyright 2017 Christian Brechbuehler alias Quigi
// using gcc version 4.8.2 (Ubuntu 4.8.2-19ubuntu1)

#include <iostream>
#include <string>
#include <cassert>


class In {                      // const long, initialized from std::cin
public:
  In() {std::cin >> i_;}
  operator long() {return i_;}
private:
  long i_;
};


static bool place(int mane, int* count, std::string *stall) {
  stall->push_back("ROYGBV"[mane]);
  // std::cerr << "place a " << mane << " of " << count[mane] << std::endl;
  return count[mane]--;
}


static std::string do_case() {
  In N;
  int uni[6];
  for (int &u: uni) std::cin >> u;
  std::string stall;            // will grow to length N

  const int first = uni[0] ? 0 : uni[2] ? 2 : 4;
  place(first, uni, &stall);    // leaving N-1 to place
  int mane = first;

  for (int j = N-1; j--;) {
    const int complement = (mane+3)%6;
    if ((mane % 1) || (uni[complement]>0) ) {
      //      std::cerr << "mane was " << mane << "; uni[" << complement << "] == "
      //          << uni[complement] << std::endl;
      mane = complement;
    } else {
      int pick = first + 2*(mane == first);
      for (int col = 0; col < 6; col += 2)
        if (col != mane && uni[col] > uni[pick])
          pick = col;
      mane = pick;
    }
    if (!place(mane, uni, &stall)) {
      std::cerr << "at " << j << "; placed \"" << stall << "\"" << std::endl;
      return "IMPOSSIBLE";
    }
  }
  assert(!uni[0]);
  assert(!uni[1]);
  assert(!uni[2]);
  assert(!uni[3]);
  assert(!uni[4]);
  assert(!uni[5]);
  if (mane == first) return "IMPOSSIBLE";
  return stall;
}

int main() {
  In T;
  for (int j = 1; j <= T; ++j) {
    std::cout << "Case #" << j << ": "
              << do_case()
              << std::endl;
  }
  return 0;
}

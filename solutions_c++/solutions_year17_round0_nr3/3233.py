#include <iostream>
#include <cstdint>
#include <map>
#include <string>
#include <sstream>

using namespace std;

uint64_t largest_remaining_span(uint64_t num_stalls, uint64_t num_occupants) {
  if (num_occupants == 0) {
    return num_stalls;
  } else {
    --num_stalls;
    --num_occupants;
    if (num_stalls & 0x1) {
      if(num_occupants & 0x1) {
        return max(largest_remaining_span(num_stalls/2 + 1,
                                          num_occupants/2 + 1),
                   largest_remaining_span(num_stalls/2, 
                                          num_occupants/2));
        } else {
          return largest_remaining_span(num_stalls/2 + 1,
                                        num_occupants/2);
        }
    } else {
      return largest_remaining_span(num_stalls/2, num_occupants/2);
    }
  }

}

string solve(uint64_t num_stalls, uint64_t num_occupants) {
  uint64_t largest_span = largest_remaining_span(num_stalls, num_occupants - 1);
  uint64_t min, max;
  stringstream solution;
  if (largest_span & 0x1) {
    max = min = (largest_span - 1) / 2;
  } else {
    max = (largest_span - 1) / 2 + 1;
    min = max - 1;
  }
  solution << max << " " << min;
  return solution.str();
}

int main(int argc, char **argv) {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    uint64_t n, k;
    cin >> n >> k;
    cout << "Case #" << i + 1 << ": " << solve(n, k) << endl;
  }
  return 0;
}
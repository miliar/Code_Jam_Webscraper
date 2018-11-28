#include <iostream>
#include <string>

using namespace std;

namespace {

string Flip(const string& to_flip) {
  string result;
  for (char c : to_flip) {
    if (c == '+') {
      result += '-';
    } else {
      result += '+';
    }
  }
  return result;
}

int Solve(const string& pancakes, size_t range, int flips) {
  if (range  > pancakes.size()) {
    return -1;
  }
  string flipped_prefix = Flip(pancakes.substr(0, range));
  flips++;
  string suffix = pancakes.substr(range);
  string new_pancakes = flipped_prefix + suffix;
  int first_sad_index = new_pancakes.find('-');
  if (first_sad_index == string::npos) {
    return flips;
  }
  return Solve(new_pancakes.substr(first_sad_index), range, flips);
}

int Solve(const string& pancakes, size_t range) {
  int first_sad_index = pancakes.find('-');
  if (first_sad_index == string::npos) {
    return 0;
  }
  return Solve(pancakes.substr(first_sad_index), range, 0);
}

}  // namespace

int main() {
  size_t cases, range;
  string pancakes;

  cin >> cases;
  for (size_t i = 1; i <= cases; i++) {
    cin >> pancakes >> range;
    int result = Solve(pancakes, range);
    cout << "Case #" << i << ": ";
    if (result >= 0) {
      cout << result;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << '\n';
  }
  return 0;
}

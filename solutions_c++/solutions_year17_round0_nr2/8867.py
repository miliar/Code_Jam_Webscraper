#include <iostream>
#include <cmath>

using namespace std;

int main () {
  int N, n, num_digits, i, prev, current_digit, index;
  long long num, ans;

  cin >> N;

  for(n = 1; n <= N; n++) {
    cin >> num;
    num_digits = (int) log10(num) + 1;

    // find first dec digit
    prev = 0; // change to 1?
    index = -1;
    for(i = num_digits - 1; i >= 0; i--) {
      current_digit = num/(long long)pow(10, i) % 10;

      if(current_digit < prev) {
        index = i + 1;
        break;
      } else {
        prev = current_digit;
      }
    }

    if(index == -1) {
      ans = num;
    } else {
      // loop back up number to find the next strickyly increaseing pair
      // prev = current_digit; // ?
      for(i = index; i < num_digits; i++) {
        current_digit = num/(long long)pow(10, i) % 10;

        if(current_digit != prev) {
          // index = i + 1;
          break;
        } else {
          prev = current_digit;
        }
      }

      ans = ((num/(long long)pow(10, i-1)) * pow(10, i-1));
      ans--;
    }
    cout << "Case #" << n << ": " << ans << endl;
  }
}

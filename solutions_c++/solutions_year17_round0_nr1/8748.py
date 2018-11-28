#include <iostream>
#include <string>

using namespace std;

int main () {
  int N, k, length, i, j, n, flip_count, flip_index;
  string temp, pancakes;
  char prev;

  getline(cin, temp);
  N = stoi(temp);

  for(n = 0; n < N; n++) {
    getline(cin, temp);
    // split the pancakes and k
    length = temp.length();
    for(i = length - 1; i >= 0; i--) {
      if(temp[i] == ' ') {
        k = stoi(temp.substr(i+1, length));
        pancakes = temp.substr(0, i);
        length = i;
        break;
      }
    }

    // cout << pancakes << endl;
    // cout << k << endl;
    // cout << length << endl;
    // just look through and flip when you get to - and if end does not work then impossible
    // k_count = 0;
    // flip_count = 0;
    // flip_index = 0;
    // prev = '+';
    // for(i = 0; i < length; i++) {
    //   // if(k_count == k) {
    //   //   // you need to start a new flip...
    //   // }
    //   if(i - flip_index >= k) {
    //     prev = '+';
    //   }
    //
    //   cout << "prev: " << prev << " pan[i]: " << pancakes[i] << endl;
    //   if(pancakes[i] != prev) {// almost like you pluss k to i?
    //     // we need to flip the next k (need to invert prev?) -- maybe change pancakes to 1's and 0's so you can xor
    //     prev = pancakes[i];
    //     flip_index = i;
    //     flip_count++;
    //     if(i > length - k) { // this isn't the only thing I need to take into accont with the whole k business
    //       // it is impossible
    //       flip_count = -1;
    //       break;
    //     }
    //   }
    // }
    //
    // if(flip_count >= 0)
    //   cout << "Case #" << (n + 1) << ": " << flip_count << endl;
    // else
    //   cout << "Case #" << (n + 1) << ": IMPOSSIBLE" << endl;

    flip_count = 0;
    // cout << "BF:" << endl;
    for(i = 0; i < length; i++) {
      if(flip_count == -1)
        break;

      if(pancakes[i] != '+') {
        flip_count++;
        for(j = 0; j < k; j++) {
          if(j + i >= length) {
            flip_count = -1;
            break;
          }

          if(pancakes[i+j] == '+') {
            pancakes[i+j] = '-';
          } else {
            pancakes[i+j] = '+';
          }
        }
      }
    }
    if(flip_count >= 0)
      cout << "Case #" << (n + 1) << ": " << flip_count << endl;
    else
      cout << "Case #" << (n + 1) << ": IMPOSSIBLE" << endl;
  }

  return 0;
}

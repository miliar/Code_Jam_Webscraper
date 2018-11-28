#include <iostream>

using namespace std;

void flipPancakes(string& pArray, unsigned int startIdx, unsigned int flipperSize) {
  // cout << "startIdx: " << startIdx << endl;
  for (unsigned int idx = 0; idx < flipperSize; ++idx) {
    if (pArray[startIdx + idx] == '-')
      pArray[startIdx + idx] = '+';
    else
      pArray[startIdx + idx] = '-';
  }
}

int main(int argc, char* argv[]) 
{
  int t;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    unsigned int K;
    string pancakeArray;
    cin >> pancakeArray >> K;  // read n and then m.
    // cout << "Case #" << i << ": " << pancakeArray << " length: " << pancakeArray.length() << " flipperSize:" << K << endl;
    if (K > pancakeArray.length()) { 
      cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
      continue;
    }
    unsigned int curr = 0;
    int numberOfTimesFlipped = 0;
    bool impossible = false;
    for (;curr < pancakeArray.length(); ++curr) {
      // cout << "curr: " << curr << " " << pancakeArray[curr] << endl;
      if (pancakeArray[curr] == '-') {
        if ((pancakeArray.length() - curr) >= K) {
          flipPancakes(pancakeArray, curr, K);
          // cout << "FLIPPED: " << pancakeArray << endl;
          numberOfTimesFlipped++;
        }
        else {
          impossible = true;
          break;
        }
      }
    }
    if (impossible)
      cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
    else
      cout << "Case #" << i << ": " << numberOfTimesFlipped << endl;
  }
  return 0;
}

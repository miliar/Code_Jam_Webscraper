#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;


//------------------------------------------------------
/*
  Thoughts:
  1. Flipping operations commute (Abelian).
  2. Two same flippeing cancels each other (Z2).

  So ordering of the flipping operations does not matter.
  For an optimal solution, the flipping operation at any
  location can occur at most once.
*/

/*
  O(N) solution:
  1. Start from the leftmost (1st) sign of the string.

  2. There is only one flipping operation that can
  affect it, and it is applied at most once. So,
  (a) if it is initially '-', we have to lip the
  first K signs, just to turn the 1st sign to '+';
  (b) if it is initially '+', nothing should be done
  about it.

  3. Move to the next site.

  4. Now there is only one flipping operation left that can
  affect it. So, (a) if it is initially '-', we have to
  flip the first K signs, just to turn the 1st
  sign to '+'; (b) if it is initially '+', nothing
  should be done about it.

  5. Repeat 3,4 until we get to the last K signs.

  6. Check if we can flip the last k signs and make the entire
  string into "++++++....++". If yes, report number of flipps;
  if no, report IMPOSSIBLE.
*/

//------------------------------------------------------

// helper function
char flip_sign(char c) {
  if (c == '+')
    return '-';
  else
    return '+';
}

/*
  Inputs:
  K always assumed to be >= 2. (not checked!)
  S's length always assumed to be be >= 2 && > K. (not checked!)

  Return values:
  If the string can be flipped to "++++...+++", this function
  returns the optimal number of flips.
  If the string cannot be flipped to "++++...+++", this function
  returns -1.
*/
int flip_string(string S, int K) {
  int num_flips = 0;
  int L = S.size();

  for (int i = 0; i <= L-K; i++) {
    if (S[i]=='-') {
      // flip the K signs starting from i
      for (int j = 0; j < K; j++) {
        S[i+j] = flip_sign(S[i+j]);
      }
      ++num_flips;
    }
    // check if it is the last site
    if (i == L-K) {
      for (int j = 0; j < K; j++) {
        // check if failed to find solution
        if (S[i+j] == '-') {
          num_flips = -1;
          break;
        }
      }
    }
  }

  return num_flips;
}

//------------------------------------------------------

int main(int argc, char const *argv[]) {
  int T, K, num_flips;
  string S;
  cin >> T;  // number of test cases
  for (int i = 1; i <= T; ++i) {
    cin >> S;  // read string
    cin >> K;

    num_flips = flip_string(S, K);

    if (num_flips == -1) {
      cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
    }else
    {
      cout << "Case #" << i << ": " << num_flips << endl;
    }

  }
  return 0;
}

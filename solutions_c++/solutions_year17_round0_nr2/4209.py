#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

//------------------------------------------------------
// helper functions

/*
  Description:
  Convert a positive integer string to a vector which stores
  all the digits of integer from high to low.
  The integer string is assumed to have no leading zeros.

  Input:
  S: integer string, length always assumed to be >= 1

  Output:
  v: always overwritten
*/
void str2vec(const string& S, vector<int>& v) {
  v.clear();
  int num_digits = S.size();

  for (int i = 0; i < num_digits; i++) {

    v.push_back(int(S[i] - '0'));
  }
}

/*
  Description:
  Convert a vector which stores all the digits of an
  integer from high to low, to a positive integer string.
  The vector might have leading zeros.

  Input:
  v: integer stored as vector, length always assumed to be >= 1

  Output:
  S: integer stored as string
*/
string vec2str(const vector<int>& v) {
  string S;
  bool is_leading_zero = true;
  for (auto i : v) {
    if(i != 0) is_leading_zero = false;
    if(!is_leading_zero) S += to_string(i);
  }
  return S;
}

/*
  Description:
  Given a vector which represents a positive integer,
  find a vector that might represent a smaller tidy integer.
  The vectors might have leading zeros.

  1. check if v is tidy
  2. if not, start with leftmost nonzero digit of v
  3. if the next digit is smaller, then decrease the current digit
  by 1 and set all following digit to 9.
  4. go back to step 1

  Input:
  v: integer stored as vector, always assumed to be >= 1

  Output:
  v: integer stored as string, modified in place
*/
void find_largest_tidy_int(vector<int>& v) {
  int N = v.size();
  while(!is_sorted(v.begin(), v.end())) {
    // v is not tidy, do backtrack
    for (int i = 0; i < N-1; i++) {
      if(v[i]>v[i+1] && v[i+1]>=0) {
        v[i] -= 1;
        for (int j = i+1; j < N; j++) v[j] = 9;
        break;
      }
    } // for
  } // while
}
//------------------------------------------------------



//------------------------------------------------------

int main(int argc, char const *argv[]) {
  int T;
  string N_str;
  vector<int> v;

  cin >> T;  // number of test cases
  for (int i = 1; i <= T; ++i) {
    cin >> N_str;  // read string
    str2vec(N_str, v);
    find_largest_tidy_int(v);
    cout << "Case #" << i << ": " << vec2str(v) << endl;

  }
  return 0;
}

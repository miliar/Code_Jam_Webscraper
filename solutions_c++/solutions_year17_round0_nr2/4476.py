/* GCJ 2017 Qualifier Problem B */

#include <iostream>
#include <vector>

using namespace std;

// #define DEBUG

// Samples:
// 132 -> 129
// 1000 -> 999
// 7 -> 7
// 111111111111111110 -> 111111111111111109 -> 111111111111111099 -> ...
// 9990 -> 9989 -> 9899 -> 8999
// 8880 -> 8879 -> 8799 -> 7999
// 9123 -> 8999
// 132 -> 129
// 123 -> 123

void testcase(int case_no) {
  string num; cin >> num;
#ifdef DEBUG
  cout << "NUM[initial]: " << num << endl;
#endif

  // Basic algorithm:
  // - scan from right to left
  // - when encountering inversion xyzzz... where x > y,
  //   - change number to (x-1)9999... and continue scanning
  //   - computing (x-1) requires carrying digits
  int first_nine = num.size(); // -- avoid redundant work
  for (int i = num.size()-2; i >= 0; i--) {
    // check nondecreasing
    int d1 = num[i] - '0';
    int d2 = num[i+1] - '0';
#ifdef DEBUG
    cout << "compare " << d1 << " <= " << d2 << endl;
#endif
    if (d1 <= d2) continue;

    // subtract one from num[i]
    int j = i;
    if (num[j] == '0') cout << "[BUG]";
    num[j] = num[j] - 1;

    // set nines from num[i+1]..end
    for (j = i+1; j < first_nine; j++)
      num[j] = '9';
    first_nine = i+1;

#ifdef DEBUG
    cout << "NUM[final]: " << num << endl;
#endif
  }

  cout << "Case #" << case_no << ": ";
  int i = 0;
  while (num[i] == '0') i++; // skip leading zeroes
  if (i >= num.size()) cout << "0 [BUG]"; // -- should not result in zero!
  for (; i < num.size(); i++) cout << num[i];
  cout << endl;
}

int main()
{
  int T; cin >> T;
  for (int i = 0; i < T; i++)
    testcase(i+1);
  return 0;
}

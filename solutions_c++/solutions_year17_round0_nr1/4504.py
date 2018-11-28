/* GCJ 2017 Qualifier Problem A */

#include <iostream>
#include <vector>

using namespace std;

// #define DEBUG

#ifdef DEBUG
void print_cakes(vector<bool> &cakes) {
  for (unsigned i = 0; i < cakes.size(); i++)
    cout << (cakes[i] ? "+" : "-");
}
#endif

void testcase(int case_no) {
  string S_str; cin >> S_str; // TODO: read only +-!
  int K; cin >> K;
  int N = S_str.size();
#ifdef DEBUG
  cout << "ROW OF PANCAKES[raw]: " << S_str << endl;
#endif
  vector<bool> cakes;
  for (unsigned i = 0; i < N; i++) {
    if (S_str[i] == '+') cakes.push_back(true); // happy-side
    if (S_str[i] == '-') cakes.push_back(false); // -- blank side
  }
#ifdef DEBUG
  cout << "ROW OF PANCAKES[initial]: "; print_cakes(cakes); cout << endl;
#endif
  N = cakes.size();

  // Basic algorithm:
  // - leftmost sad cake MUST be flipped; happy cakes before it MUST NOT.
  // - flip starting from leftmost sad cake, and repeat
  // - if leftmost sad cake is too far right, output IMPOSSIBLE
  int flip_count = 0; bool impossible = false;
  int left_sad = 0;
  for (;;) {
    // advance left_sad
    while (left_sad < cakes.size() && cakes[left_sad]) left_sad++;
    if (left_sad >= cakes.size()) break; // -- done flipping
    if (left_sad + K > cakes.size()) { impossible = true; break; }

    // flip left_sad..left_sad + K
    for (unsigned i = 0; i < K; i++)
      cakes[left_sad+i] = !cakes[left_sad+i];
    flip_count++;
#ifdef DEBUG
    cout << "ROW OF PANCAKES[#" << flip_count << "]: "; print_cakes(cakes); cout << endl;
#endif
  }

  cout << "Case #" << case_no << ": ";
  if (impossible)
    cout << "IMPOSSIBLE";
  else
    cout << flip_count;
  cout << endl;
}

int main()
{
  int T; cin >> T;
  for (int i = 0; i < T; i++)
    testcase(i+1);
  return 0;
}

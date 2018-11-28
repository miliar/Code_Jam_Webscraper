#include <iostream>
#include <string>
// #include <ctime>

using namespace std;


int main() {
  // clock_t begin = clock();

  int t, k;
  string s, toFile = "", result = "";
  cin >> t;

  for (int i = 1; i <= t; i++) {
    cin >> s;
    cin >> k;

    int counter = 0;

    int next = 0;
    while (next <= s.length() - k) {
      if (s[next] == '-') {
        int start = next;
        bool isNextSet = false;

        for (int l = start; l < start + k; l++) {
          if (s[l] == '+') {
            s[l] = '-';
            if (!isNextSet) {
              next = l;
              isNextSet = true;
            }
          } else {
            s[l] = '+';
            if (!isNextSet) {
              next++;
            }
          }
        }
        counter++;
      } else  {
        next++;
      }
    }

    // for (int j = 0; j <= s.length() - k; j++) {
    //   if (s[j] == '-') {
    //     for (int l = j; l < j + k; l++) {
    //       s[l] = s[l] == '-' ? '+' : '-';
    //     }
    //     counter++;
    //   }
    // }

    result = s.find_first_of('-', s.length() - k) != string::npos ? "IMPOSSIBLE" : to_string(counter);
    toFile += "Case #" + to_string(i) + ": " + result + "\n";
  }

  cout << toFile;

  // clock_t end = clock();
  // double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
  //
  // cout << elapsed_secs;

  return 0;
}

#include <string>
#include <fstream>
#include <iostream>
#include <istream>
#include <sstream>
#include <functional>
#include <numeric>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 0; t != T; ++t) {
    unsigned long long N, K;
    cin >> N >> K;

    if (N == K)
    {
      cout << "Case #" << t + 1 << ": 0 0" << endl;
      continue;
    }

    unsigned long long num[3] = { 0, };
    unsigned long long count[3] = { 0, };

    num[0] = N;
    count[0] = 1;

    unsigned long long c, n, nn, nn1, nn2;
    while (1) {
      c = count[0];
      n = num[0];

      num[0] = num[1];
      num[1] = num[2];
      num[2] = 0;
      count[0] = count[1];
      count[1] = count[2];
      count[2] = 0;

      if (K <= c) break;
      K -= c;
      //Update queue
      if (n % 2) {
        // K odd => 2 x K/2
        // next number
        nn = (n - 1) / 2;

        if (num[0] == 0 || num[0] == nn) {
          num[0] = nn;
          count[0] += 2 * c;
        }
        else if (num[1] == 0 || num[1] == nn) {
          num[1] = nn;
          count[1] += 2 * c;
        }
        else {
          num[2] = nn;
          count[2] += 2 * c;
        }
      }
      else {
        // K even => K/2 ceil & K/2 floor
        nn1 = n / 2;
        nn2 = nn1 - 1;

        if (num[0] == 0 || num[0] == nn1) {
          num[0] = nn1;
          count[0] += c;
        }
        else if (num[1] == 0 || num[1] == nn1) {
          num[1] = nn1;
          count[1] += c;
        }

        if (num[1] == 0 || num[1] == nn2) {
          num[1] = nn2;
          count[1] += c;
        }
        else if (num[2] == 0 || num[2] == nn2) {
          num[2] = nn2;
          count[2] += c;
        }
      }
    }

    cout << "Case #" << t + 1 << ": ";

    if (n % 2)
      cout << (n - 1) / 2 << " " << (n - 1) / 2;
    else
      cout << n / 2 << " " << n / 2 - 1;

    cout << endl;
  }

  return 0;
}
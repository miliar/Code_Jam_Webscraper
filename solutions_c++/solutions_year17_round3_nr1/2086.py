#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <iterator>

struct pancake {
  int r;
  int h;

  bool operator<(const pancake& other) const {
    double other_area = (2 * M_PI * other.r * other.h) + (M_PI * other.r * other.r);
    double my_area = (2 * M_PI * this->r * this->h) + (M_PI * this->r * this->r);
    return my_area < other_area;
  }
};

using namespace std;

string FILENAME = "A-small-attempt4";

int main () {
  setvbuf(stdout, NULL, _IONBF, 0);
  freopen((FILENAME + ".in").c_str(), "r", stdin);
  freopen((FILENAME + ".out").c_str(), "w", stdout);
  int testcases;
  scanf("%d", &testcases);
  for (int case_id = 1; case_id <= testcases; case_id++) {
    printf("Case #%d: ", case_id);
    int n, k;
    scanf("%d %d", &n, &k);
    vector<pancake> pancakes;
    for (int i = 0; i < n; i++) {
      pancake p;
      int r, h;
      scanf("%d %d", &r, &h);
      p.r = r;
      p.h = h;
      pancakes.push_back(p);
    }
    vector<bool> mask(n);
    for (int i = 0; i < n; i++) {
      if (i < k) {
        mask[i] = 0;
      } else {
        mask[i] = 1;
      }
    }

    double biggest = 0;
    do {
      int biggest_radius = 0;
      double total_area = 0;
      for (int i = 0; i < n; i++) {
        if (!mask[i]) {
          total_area += pancakes[i].h * 2 * M_PI * pancakes[i].r;
          biggest_radius = max(biggest_radius, pancakes[i].r);
        }
      }
      double total = ((double) biggest_radius * (double) biggest_radius * M_PI) + total_area;
      if (total > biggest) {
        biggest = total;
      }
    } while (next_permutation(mask.begin(), mask.end()));

    cout.precision(50);
    cout << biggest << endl;
  }
  fflush(stdout);
}

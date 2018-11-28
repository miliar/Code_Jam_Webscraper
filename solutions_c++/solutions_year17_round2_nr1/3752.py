#include <iostream>
#include <vector>
#include <limits>


using namespace std;

int main(int argc, char **argv) {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    int d, n;
    cin >> d >> n;
    double longest_travel_time = 0;
    int k, s;
    for (int j = 0; j < n; ++j) {
      cin >> k >> s;
      double travel_time = (double)(d - k) / (double)s;
      if (travel_time > longest_travel_time) {
        longest_travel_time = travel_time;
      }
    }
    double cruising_speed = (double)d / longest_travel_time;
    printf("Case #%d: %.6f\n", i + 1, cruising_speed);
  }
  return 0;
}
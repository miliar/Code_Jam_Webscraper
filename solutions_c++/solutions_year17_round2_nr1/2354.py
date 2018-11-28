#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

void solve(int kase) {
      cout << "Case #" << kase + 1 << ": ";
          int d, n;
              cin >> d >> n;
                  double maxTime = 0;
                      for (int i = 0; i < n; i++) {
                                int k, s;
                                        cin >> k >> s;
                                                maxTime = max(maxTime, (double)(d - k) / s);
                                                    }
                                                        printf("%.6f\n", d / maxTime);
}

int main() {
      int t;
          cin >> t;
              for (int i = 0; i < t ; i++) {
                        solve(i);
                            }
}


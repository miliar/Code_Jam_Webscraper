#include <iostream>
#include <string>
#include <vector>
#include <queue>


long xmax(long m, long r) {
  return (100*m)/(90*r);
}

long xmin(long m, long r) {
  return (100*m + 110*r-1)/(110*r);
}

int main() {
  int T;
  std::cin >> T;
  for (int t = 0; t < T; ++t) {
    int n, p;
    std::cin >> n >> p;
    std::vector<long> r(n);
    for (auto& ri : r)
      std::cin >> ri;
    std::vector<std::priority_queue<long>> pq(n);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < p; ++j) {
        long qij;
        std::cin >> qij;
        pq[i].push(qij);
      }
    long res = 0;
    while (true) {
      bool flag = false;
      for (int i = 0; i < n; ++i)
        if (pq[i].empty())
          flag = true;
      if (flag)
        break;
      int min_of_max = 2000000L;
      for (int i = 0; i < n; ++i) {
        const long maxi = xmax(pq[i].top(), r[i]);
        if (min_of_max > maxi)
          min_of_max = maxi;
      }
      int max_of_min = 0L;
      for (int i = 0; i < n; ++i) {
        const long mini = xmin(pq[i].top(), r[i]);
        if (max_of_min < mini)
          max_of_min = mini;
      }
      if (min_of_max == 0)
        break;
      if (min_of_max < max_of_min) {
        for (int i = 0; i < n; ++i) {
          const long mini = xmin(pq[i].top(), r[i]);
          if (mini > min_of_max)
            pq[i].pop();
        }
      }
      else {
        ++res;
        for (int i = 0; i < n; ++i)
          pq[i].pop();
      }
    }

    std::cout << "Case #" << t+1 << ": " << res << std::endl;
  }
  return EXIT_SUCCESS;
}

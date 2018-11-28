#include <algorithm>
#include <cstdio>
#include <memory>
#include <utility>
#include <vector>
using namespace std;

int main() {
  int cases;
  scanf("%d", &cases);
  for (int c = 0; c < cases; ++c) {
    int d, n;
    scanf("%d%d", &d, &n);
    vector<pair<double, double>> horses;
    for (int i = 0; i < n; ++i) {
      int k, s;
      scanf("%d%d", &k, &s);
      horses.push_back(make_pair(k, s));
    }
    sort(horses.begin(), horses.end());

    double total_time = 0;
    for (size_t i = 0; i < horses.size(); ++i) {
      bool useless = false;
      for (size_t j = 1; j < horses.size(); ++j) {
        if (horses[i].second < horses[j].second) {
          continue;
        }
        double t_catch = (horses[j].first - horses[i].first) / (horses[i].second - horses[j].second);
        double t_end = (d - horses[j].first) / horses[j].second;
        if (t_catch < t_end) {
          useless = true;
          break;
        }
      }
      if (useless == false) {
        total_time = (d - horses[i].first) / horses[i].second;
        break;
      }
    }



    // double total_time = 0;
    // while (true) {
    //   vector<pair<double, int>> pair_time;
    //   for (size_t i = 1; i < horses.size(); ++i) {
    //     if (horses[i - 1].second <= horses[i].second) {
    //       continue;
    //     }
    //     double t_catch = (horses[i].first - horses[i - 1].first) / (horses[i - 1].second - horses[i].second);
    //     double t_end = (d - horses[i].first) / horses[i].second;
    //     pair_time.push_back(make_pair(min(t_catch, t_end), i));
    //   }
    //   if (pair_time.size() == 0) {
    //     break;
    //   }
    //   auto&& m = min_element(pair_time.begin(), pair_time.end());
    //   total_time += m->first;
    //   horses.erase(horses.begin() + m->second - 1);
    //   for (auto&& horse : horses) {
    //     horse.first += horse.second * m->first;
    //   }
    //   horses.erase(find_if(horses.begin(), horses.end(), [d](auto&& horse) {
    //       return d <= horse.first;
    //       }), horses.end());
    // }
    // if (horses.size() != 0) {
    //   total_time += (d - horses[0].first) / horses[0].second;
    // }
    printf("Case #%d: %f\n", c + 1, d / total_time);
  }
  return 0;
}

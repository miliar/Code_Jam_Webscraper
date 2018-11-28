#include <iomanip> 
#include <vector>
#include <iostream>
#include <map>

using namespace std;

void get_max_speed(std::map<int, int> hourse, int D) {
  std::vector<double> time_to_reach;
  for (auto it = hourse.rbegin(); it != hourse.rend(); it++) {
    time_to_reach.push_back(double(D - it->first)/double(it->second));
  }
  double min_time = time_to_reach[0];
  for (int i = 1, j = time_to_reach.size() - 2; i < time_to_reach.size(), j >= 0; i++, j--) {
     if (time_to_reach[i] < time_to_reach[i-1]) {
        std::map<int, int>::iterator it = (hourse.begin());
        for (int k = 0; k < j; k++) it++;
        double top_speed = (D - (it->first)) / min_time;
        time_to_reach[i] = (D - it->first) / top_speed;
     }
     min_time = time_to_reach[i];
  }
  cout << std::setprecision(8) << D / min_time << endl;;
}

int main(int argc, char **args) {
  int test_cases = 0;
  cin >> test_cases;
  for(int i = 1; i <= test_cases; i++) {
    std::map<int, int> hourse;
    int D, N;
    cin >> D;
    cin >> N;
    for (int i = 0; i < N; i++) {
      int x, y;
      cin >> x;
      cin >> y;
      hourse[x] = y;
    }
    cout << "Case #" << i << ": ";
    get_max_speed(hourse, D);
  }
  return 0;
}

#include <iostream>
#include <sstream>
#include <string>
#include <queue>
#include <vector>
#include <map>

using namespace std;
/*
5
3
1 0 0 1 0 0 1

4
2
1 0 1 0 0 1
 */
std::pair<long, long> minmax2(long num_stalls, long num_users) {
  priority_queue<long> spaces;
  map<long, long> counts;
  spaces.push(num_stalls);
  counts[num_stalls] = 1;
  long min;
  long max;
  while (num_users > 0) {
    long largest = spaces.top();
    while (spaces.top() == largest && !spaces.empty()) {
      spaces.pop();
    }
    long count = counts[largest];
    counts[largest] = 0;

    long stall = (largest / 2) + (largest % 2);
    long L = largest - stall;
    long R = stall - 1;
    spaces.push(L);
    spaces.push(R);
    min = L > R ? R : L;
    max = L < R ? R : L;
    if (counts.find(L) != counts.end()) {
      counts[L] = counts[L] + count;
    } else {
      counts[L] = count;
    }
    if (counts.find(R) != counts.end()) {
      counts[R] = counts[R] + count;
    } else {
      counts[R] = count;
    }
    num_users -= count;
    //cerr << num_users << " " << count << endl;
    //cerr << max << " " << min << endl;
  }
  return make_pair(max, min);
}

int main() {
  int tc;
  cin >> tc;
  for (int i = 0; i < tc; i++) {
    long num_stalls;
    long num_users;

    cin >> num_stalls;
    cin >> num_users;
    std::pair<long, long> result = minmax2(num_stalls, num_users);

    cout << "Case #" << i + 1 << ": " << result.first << " " << result.second
         << endl;
  }
}

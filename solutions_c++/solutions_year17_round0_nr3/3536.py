#include <iostream>
#include <queue>
using namespace std;

int main() {
  int n_case;
  priority_queue<unsigned long long> pq;

  cin >> n_case;
  for (int i_case = 1; i_case <= n_case; ++i_case) {
    int n, k;
    cin >> n >> k;

    // initialize
    while(!pq.empty()) {
        pq.pop();
    }
    pq.push(n);

    // process
    for(int i=1; i<k; ++i) {
        unsigned long long top = pq.top();
        pq.pop();
        top--;
        pq.push(top/2);
        pq.push(top/2+top%2);
    }
    unsigned long long final_top = pq.top()-1;
    unsigned long long ans_max = final_top/2+final_top%2;
    unsigned long long ans_min = final_top/2;

    // display result
    cout << "Case #" << i_case << ": " << ans_max << " " << ans_min << "\n";
  }
  return 0;
}
#include <iostream>
#include <queue>
using namespace std;

void output(int t, unsigned long long x, unsigned long long y) {
  cout << "Case #" << t + 1<< ": " << x << " " << y << endl;
}

int main() {
  int t;
  cin >> t;
  for (int tt = 0; tt < t; tt++) {
    unsigned long long n, k;
    cin >> n >> k;
    priority_queue<unsigned long long> q;
    q.push(n);
    for (int i=0; i<k-1; i++) {
      unsigned long long tmp =  q.top();
      q.pop();
      if (tmp % 2 == 1) {
        q.push(tmp/2);
        q.push(tmp/2);
      } else {
        q.push(tmp/2);
        q.push(tmp/2-1);
      }
    }
    if (q.top() % 2 == 1) {
      output(tt, q.top() / 2, q.top() / 2);
    } else {
      output(tt, q.top() / 2, q.top() / 2 - 1);
    }
  }
  return 0;
}

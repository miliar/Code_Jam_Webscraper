#include<iostream>
#include<queue>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    long n;
    cin >> n;
    long k;
    cin >> k;
    priority_queue<long> q;
    q.push(n);
    long l1 = n;
    long l2 = n;
    for (long i = 0; i < k; i++) {
      long x = q.top();
      q.pop();
      l1 = x / 2;
      l2 = l1;
      if (x % 2 == 0) {
        l2--;
      }
      if (l1 != 0) {
        q.push(l1);
      }
      if (l2 != 0) {
        q.push(l2);
      }
    }
    cout << "Case #" << t << ": " << l1 << " " << l2 << endl;
  }
}

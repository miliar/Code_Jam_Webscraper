#include <iostream>
#include <fstream>
#include <queue>
#include <stdio.h>
#include <utility>
#include <vector>

using namespace std;

struct interval {
  long left;
  long right;
  interval(int left, int right) : left(left), right(right) {}
  bool operator<(const interval &other) const {
    long diff = (right - left) - (other.right - other.left);
    if (diff == 0 && left < other.left)
      return 1;
    return (right - left) < (other.right - other.left);
  }
};

int main(void) {
  int t;
  long long n;
  long long k;

  vector<long long> v;

  ifstream in;
  in.open("C-small-2-attempt0.in");
  in >> t;

  ofstream out;
  out.open("C-small.out");

  for (int tt = 0; tt < t; tt++) {
    priority_queue<interval> pq;
    in >> n >> k;
    pq.push(interval(0, n + 1));

    long long ll, lr, mid;
    for (long long i = 0; i < k; i++) {
      auto largest = pq.top();
      pq.pop();
      ll = largest.left;
      lr = largest.right;
      mid = (largest.left + largest.right) / 2;
      // cout << "pushed " << ll << "," << mid << endl;
      // cout << "pushed " << mid << "," << lr << endl;
      pq.push(interval(ll, mid));
      pq.push(interval(mid, lr));
    }
    long ans1 = max(mid - ll - 1, lr - mid - 1);
    long ans2 = min(mid - ll - 1, lr - mid - 1);

    cout << "Case #"<<tt+1<<": "<<ans1 << " " << ans2 << endl;
    out << "Case #"<<tt+1<<": "<<ans1 << " " << ans2 << endl;
  }
  in.close();
  out.close();
  // cout<<(one<two)<<endl;
  // cout<<"first el "<<pq.top().left<<endl;
  return 0;
}
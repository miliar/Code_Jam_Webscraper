#include<iostream>
#include<cstdio>
#include <queue>

using namespace std;

struct bath {
  unsigned long long int  len;
  unsigned long long int  count;
};

bool operator<(const bath& a, const bath& b) {
  return a.len < b.len;
}

int main(){
  ios_base::sync_with_stdio(true);

  int t; cin >> t;
  for (int tid = 1; tid <= t; tid ++) {
    unsigned long long int  n; cin >> n; 
    unsigned long long int  k; cin >> k;
    priority_queue<bath> q;
    bath start; start.len = n; start.count = 1;
    q.push(start);
    for (unsigned long long int  i = 0; i < k;) {
      bath opt = q.top(); q.pop();
//      cout << "opt "<< opt.len << " " << opt.count << endl;
      while (!q.empty() && q.top().len == opt.len) {
        bath tmp = q.top(); q.pop();
        opt.count += tmp.count;
//        cout << "tmp " << tmp.len << " " << tmp.count << endl;
//        cout << "opt "<< opt.len << " " << opt.count << endl;
      }
      bath left, right; left.len = (opt.len)/2; right.len = (opt.len-1)/2;
      left.count = right.count = opt.count;
      q.push(left);
      q.push(right);
      if (i < k && i + opt.count >= k) {
        cout << "Case #" << tid << ": " << (unsigned long long int )(opt.len/2) << " " << (unsigned long long int )((opt.len-1)/2) << endl;
      }
      i += opt.count;
    }
  }
}

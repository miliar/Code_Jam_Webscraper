#include <iostream>
#include <vector>
#include <queue>

struct solution{
  unsigned int max;
  unsigned int min;
};

solution find_my_stall(unsigned int n, unsigned int k){
  std::priority_queue<unsigned int> q;
  q.push(n);
    
  for (unsigned int i = 0; i < k; i++) {
    unsigned int _n = q.top();
    q.pop();

    unsigned int stall = (_n+1)/2;

    unsigned int ls = stall - 1;
    unsigned int rs = _n - stall;

    if (ls >= rs) {
      q.push(ls);
      q.push(rs);
    } else {
      q.push(rs);
      q.push(ls);
    }
  }

  unsigned int _n = q.top();
  q.pop();

  unsigned int stall = (_n+1)/2;

  unsigned int ls = stall - 1;
  unsigned int rs = _n - stall;
  
  return (struct solution){std::max(ls, rs), std::min(ls, rs)};

}



int main() {
  int t, n, k;
  std::cin >> t;
  for (int i = 1; i <= t; ++i) {
    std::cin >> n >> k;

    solution s = find_my_stall(n, k - 1);
    std::cout << "Case #" << i << ": " << s.max  << " " << s.min << std::endl;
  }

  return 0;
}

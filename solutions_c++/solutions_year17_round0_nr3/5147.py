#include <iostream>
#include <queue>
#include <utility>
#define mp std::make_pair
#define X first
#define Y second

class Compare {
public:
  bool operator() (std::pair<int,int> l, std::pair<int,int> r) {
    //is l < r ?
    int sl = l.Y - l.X;
    int sr = r.Y - r.X;
    if (sl < sr) return true;
    if (sl > sr) return false;
    return (l.X < r.X);
  }
};

void print (std::pair<int,int> p) {
  std::cout << p.X << " " << p.Y << std::endl;
}
int main () {
  int t; 
  std::cin >> t;
  for (int j = 1; j <= t; j++) {
    std::priority_queue<std::pair<int,int>, std::vector<std::pair<int,int> >, Compare > pq;
    int n,k;
    std::cin >> n >> k;
    pq.push(mp(0,n+1));
    while (k>1) {
      std::pair<int,int> stp = pq.top();
      pq.pop();
      int loc = stp.X + ((stp.Y - stp.X)/2);
      pq.push(mp(stp.X, loc));
      pq.push(mp(loc,stp.Y));
      k--;
    }
    std::pair<int,int> stp = pq.top();
    int loc = stp.X + ((stp.Y - stp.X)/2);
    std::cout << "Case #" << j << ": " << stp.Y - loc - 1 << " " << loc - stp.X - 1 << std::endl;
  }
}

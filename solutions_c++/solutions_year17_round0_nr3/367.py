#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <tuple>

using std::vector;
using std::string;
using std::cout;
using std::cin;
using std::endl;
using std::pair;
using std::make_pair;

typedef pair<int, int> IP;

int main ()
{
  int T;
  std::cin >> T;
  string buf;

  for (int t=1; t<=T; t++)
  {
    int N,K;
    std::cin >> N >> K;
    std::vector<IP> stack;
    stack.push_back(make_pair(N,1));
    int head = 0;
    int gap = 0;
    while (K > 0) {
      int num;
      std::tie(gap, num) = stack[head];
      head ++;

      K -= num;
      if (K <= 0) break;
      std::vector<IP> substack;
      if (gap % 2 == 1) {
        substack.push_back(IP(gap/2,2*num));
      } else {
        substack.push_back(IP(gap/2,num));
        substack.push_back(IP(gap/2-1,num));
      }

      for (IP p : substack) {
        if (p.first > 0) {
          if (p.first == stack.back().first) {
            stack.back().second += p.second;
          } else {
            stack.push_back(p);
          }
        }
      }
    }

    std::cout << "Case #" << t << ": ";
    std::cout << gap/2 << " " << (gap-1)/2;
    std::cout << endl;
  }
  return 0;
}

#include <iostream>
#include <queue>

using std::cin;
using std::cout;

typedef std::pair<unsigned long long, unsigned long long> p_ull;


std::priority_queue<unsigned long long> q;
std::priority_queue<unsigned long long> q_aux;

p_ull f(unsigned long long k)
{
  while (k > 0)
  {
    unsigned long long x = q.top(); q.pop();
    if (x == 0)
      return std::make_pair(0, 0);
    if (x % 2 == 1)
    {
      unsigned long long m = (x - 1) / 2;
      k--;
      if (k == 0)
        return std::make_pair(m, m);
      q_aux.push(m);
      q_aux.push(m);
    }
    else
    {
      unsigned long long m = (x - 1) / 2;
      k--;
      if (k == 0)
        return std::make_pair(m+1, m);
      q_aux.push(m+1);
      q_aux.push(m);
    }
    if (q.empty())
    {
      q.swap(q_aux);
    }
  }
}
int main()
{
  int T;
  unsigned long long N, K;
  cin >> T;
  for (int i = 0; i < T; ++i) 
  {
    cin >> N >> K;
    q = std::priority_queue<unsigned long long>();
    q_aux = std::priority_queue<unsigned long long>();
    q.push(N);
    auto pair = f(K);
    //cout << pair.first << " " << pair.second << std::endl;
    cout << "Case #" << (i+1) << ": " << pair.first << " " << pair.second << std::endl;
  }
}

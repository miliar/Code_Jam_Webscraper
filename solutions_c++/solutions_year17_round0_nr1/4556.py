#include <iostream>
#include <string>
#include <queue>

struct QueueItem {
  std::string S;
  long flip;
  QueueItem(const std::string &S, long flip)
    : S(S), flip(flip) {}
};

std::string flip(const std::string &S, unsigned K, unsigned n)
{
  std::string T = S;
  for (unsigned i = n; i < n + K; ++i) {
    T[i] = (T[i] == '+') ? '-' : '+';
  }
  return T;
}

bool goal(const std::string &S)
{
  for (unsigned i = 0; i < S.size(); ++i) {
    if (S[i] == '-') return false;
  }
  return true;
}

bool condition(const std::string &S, unsigned n)
{
  for (unsigned i = 0; i <= n; ++i) {
    if (S[i] == '-') return false;
  }
  return true;
}

long solve(const std::string &S, unsigned K)
{
  std::queue<QueueItem> q;
  q.emplace(S, 0);
  
  long minimum = -1;
  
  for (unsigned i = 0; i <= S.size() - K; ++i) {
    std::queue<QueueItem> nq;
    
    while (!q.empty()) {
      QueueItem item = q.front(); q.pop();
      if (condition(item.S, i)) {
        nq.emplace(item.S, item.flip);
      }
      
      std::string T = flip(item.S, K, i);
      if (condition(T, i)) {
        nq.emplace(T, item.flip + 1);
      }
    }
    
    q = nq;
  }
  
  while (!q.empty()) {
    QueueItem item = q.front();
    
    if (goal(item.S)) {
      if (minimum < 0) minimum = item.flip;
      minimum = std::min(minimum, item.flip);
    }
    
    q.pop();
  }
  
  return minimum;
}

int main()
{
  unsigned T;
  std::cin >> T;

  for (unsigned t = 0; t < T; ++t) {
    std::string S;
    unsigned K;
    std::cin >> S >> K;

    long result = solve(S, K);

    std::cout << "Case #" << (t + 1) << ": ";
    if (result < 0) {
      std::cout << "IMPOSSIBLE" << std::endl;
    } else {
      std::cout << result << std::endl;
    }
  }

  return 0;
}

#include <iostream>
#include <queue>

template<typename T, typename U, char Delim = ' '>
std::ostream& operator<<(std::ostream &os, const std::pair<T, U> &pair)
{
  os << pair.first << Delim << pair.second;
  return os;
}

struct Tuple
{
  uint64_t L, R;
  
  Tuple(uint64_t L, uint64_t R) : L(L), R(R) {}
  uint64_t operator()() const { return R - L; }
  bool operator<(const Tuple &t) const { 
    return ((*this)() == t()) ? (L > t.L) : ((*this)() < t()); 
  }
};

std::ostream& operator<<(std::ostream &os, const Tuple &tuple)
{
  os << tuple.L << ' ' << tuple.R;
  return os;
}

std::pair<uint64_t, uint64_t> solve(uint64_t N, uint64_t K)
{
  std::priority_queue<Tuple> q;
  q.emplace(0, N + 1);
  
  uint64_t last_S = -1;
  for (unsigned k = 0; k < K; ++k) {
    Tuple tuple = q.top(); q.pop();
    while (tuple() <= 1) { tuple = q.top(); q.pop(); }
    
    uint64_t middle = (tuple.L + tuple.R) >> 1;
    
    //std::cerr << (k + 1) << '\t' << '(' << tuple << ')' << ',' << tuple() << '\t' << middle << std::endl;
    
    if (k == K - 1) last_S = middle;
    q.emplace(tuple.L, middle);
    q.emplace(middle, tuple.R);
  }
  
  uint64_t L = -1, R = -1;
  while (!q.empty()) {
    Tuple tuple = q.top(); q.pop();
    //std::cerr << '(' << tuple << ')' << std::endl;
    
    if (tuple.L == last_S) R = tuple() - 1;
    if (tuple.R == last_S) L = tuple() - 1;
  }
  
  //if (L > 0) --L;
  //if (R > 0) --R;
  
  return std::pair<uint64_t, uint64_t>(std::max(L, R), std::min(L, R));
}

int main()
{
  unsigned T;
  std::cin >> T;

  for (unsigned t = 0; t < T; ++t) {
    uint64_t N, K;
    std::cin >> N >> K;

    std::cout << "Case #" << (t + 1) << ": " << solve(N, K) << std::endl;
  }

  return 0;
}

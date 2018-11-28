// g++ -std=c++0x -o C2 C2.cpp
// requires Boost 1.46 on Ubuntu 12.04

#include <iostream>
#include <boost/multi_index_container.hpp>
#include <boost/multi_index/key_extractors.hpp>
#include <boost/multi_index/ordered_index.hpp>

/// a span of empty stalls
class StallSpan
{
public:
  int
  size() const
  {
    return right - left + 1;
  }

public:
  int left; ///< index of leftmost stall, inclusive
  int right; ///< index of rightmost stall, inclusive
};

typedef boost::multi_index_container<
  StallSpan,
  boost::multi_index::indexed_by<
    boost::multi_index::ordered_unique<
      boost::multi_index::composite_key<
        StallSpan,
        boost::multi_index::const_mem_fun<StallSpan, int, &StallSpan::size>,
        boost::multi_index::member<StallSpan, int, &StallSpan::left>
      >,
      boost::multi_index::composite_key_compare<
        std::greater<int>,
        std::less<int>
      >
    >
  >
> Container;
typedef Container::nth_index<0>::type Stalls;

std::pair<int, int>
occupy(Stalls& stalls)
{
  auto spanIt = stalls.begin(); // take the largest span
  StallSpan span = *spanIt;
  stalls.erase(spanIt);

  int spanSize = span.size();
  if (spanSize == 1) { // span is fully occupied
    return {0, 0};
  }

  if (spanSize == 2) { // occupy left stall
    stalls.insert({span.left + 1, span.right});
    return {1, 0};
  }

  if (spanSize % 2 == 1) { // occupy center stall
    int halfSize = spanSize / 2;
    stalls.insert({span.left, span.left + halfSize - 1});
    stalls.insert({span.right - halfSize + 1, span.right});
    return {halfSize, halfSize};
  }
  else { // occupy center-left stall
    int halfSize = spanSize / 2;
    stalls.insert({span.left, span.left + halfSize - 2});
    stalls.insert({span.right - halfSize + 1, span.right});
    return {halfSize, halfSize - 1};
  }
}

void
solve()
{
  int N, K;
  std::cin >> N >> K;

  Container container;
  Stalls& stalls = container.get<0>();
  stalls.insert({1, N});

  int max, min;
  for (int person = 0; person < K; ++person) {
    std::tie(max, min) = occupy(stalls);
  }

  std::cout << max << ' ' << min;
}

int
main()
{
  int T;
  std::cin >> T;
  for (int CASE = 1; CASE <= T; ++CASE) {
    std::cout << "Case #" << CASE << ": ";
    solve();
    std::cout << '\n';
  }
}

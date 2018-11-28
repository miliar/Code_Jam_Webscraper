#include <iostream>
#include <utility>

using namespace std;

// returns x, where i == 2^n && integer(n) && 2^n-1 <= k < 2^(n+1)-1
template<typename T>
T largest_pow_2(T k) {
  int c = 0;
  while (k > 0) {
    ++c;
    k >>= 1;
  }
  k = 1;
  while(--c > 0) k <<= 1;
  return k;
}

template<typename T>
T calc_range_size(T n, T k) {
  T p2 = largest_pow_2(k);
  T placed = p2 - 1;
  T left_stalls = n - placed;
  T left_people = k - placed;
  if (left_stalls <= p2) return 1;
  T min_range_size = left_stalls / p2;
  T max_range_size = min_range_size + 1;
  T max_range_num = left_stalls % p2;
  return left_people <= max_range_num
    ? max_range_size
    : min_range_size;
}

template<typename T>
pair<T, T> min_max(T range_size) {
  T l = range_size/2;
  return pair<T, T>(l, range_size - 1 - l);
}

template<typename T>
void print_result(T t, pair<T, T> ls) {
  cout << "Case #" << t << ": " << ls.first << " " << ls.second << endl;
}

int main() {
  typedef unsigned long long N;
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    N n, k;
    cin >> n >> k;
    print_result<N>(t, min_max<N>(calc_range_size<N>(n, k)));
  }
  return 0;
}

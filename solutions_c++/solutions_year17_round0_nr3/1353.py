#include <cstdint>
#include <utility>
#include <cstdio>
#include <vector>
#include <map>

typedef std::pair<uint64_t, uint64_t> Result;

Result get_stall_map(uint64_t N, uint64_t K) {
  std::map<uint64_t, uint64_t, std::greater<uint64_t> > gaps;
  gaps[N] = 1;
  uint64_t Ls, Rs;
  while (K > 0) {
    N = gaps.begin()->first;
    uint64_t num = gaps.begin()->second;
    gaps.erase(gaps.begin());
    Ls = (N-1)/2;
    Rs = N/2;
    gaps[Ls] += num;
    gaps[Rs] += num;
    if (K <= num) break;
    K -= num;
  }
  return {Rs, Ls};
}

std::vector<Result > read_input(char * filename) {
  FILE * f = fopen(filename, "r");
  std::vector<Result > ret;
  int num;
  uint64_t N, K;
  fscanf(f, "%d\n", &num);
  for (int i = 0; i < num; i++) {
    fscanf(f, "%zu %zu\n", &N, &K);
    ret.push_back({N, K});
  }
  fclose(f);
  return ret;
}

int main(int argc, char ** argv) {
  std::vector<Result > input = read_input(argv[1]);
  for (int i = 0; i < input.size(); i++) {
    Result sol = get_stall_map(input[i].first, input[i].second);
    printf("Case #%d: %zu %zu\n", i+1, sol.first, sol.second);
  }
}

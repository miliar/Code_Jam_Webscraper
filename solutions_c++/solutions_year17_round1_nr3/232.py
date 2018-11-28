#include <functional>
#include <iostream>
#include <queue>
#include <set>
#include <string>
#include <tuple>
#include <vector>


namespace {

std::string Solve(int Hd, int Ad, int Hk, int Ak, int B, int D) {
  const std::string kImpossible = "IMPOSSIBLE";
  auto attack = [](const std::vector<int>& state) {
    std::vector<int> next_state = state;
    next_state[2] = std::max(0, next_state[2] - next_state[1]);
    return next_state;
  };
  auto buff = [=](const std::vector<int>& state) {
    std::vector<int> next_state = state;
    next_state[1] = std::min(Hk, next_state[1] + B);
    return next_state;
  };
  auto cure = [=](const std::vector<int>& state) {
    std::vector<int> next_state = state;
    next_state[0] = Hd;
    return next_state;
  };
  auto debuff = [=](const std::vector<int>& state) {
    std::vector<int> next_state = state;
    next_state[3] = std::max(0, next_state[3] - D);
    return next_state;
  };
  const std::vector<std::function<std::vector<int>(const std::vector<int>&)>>
      actions = {attack, buff, cure, debuff};
  std::vector<int> initial_state = {Hd, Ad, Hk, Ak};
  std::set<std::vector<int>> seen;
  seen.insert(initial_state);
  std::priority_queue<std::tuple<int, int, std::vector<int>>> queue;
  queue.emplace(0, (Hk + Ad - 1) / Ad, initial_state);
  while (!queue.empty()) {
    int turns = -std::get<0>(queue.top()) + 1;
    const std::vector<int> state = std::get<2>(queue.top());
    queue.pop();
    if (state[2] <= state[1]) return std::to_string(turns);
    for (const auto& action : actions) {
      auto next = action(state);
      next[0] -= next[3];
      if (next[0] <= 0) continue;
      if (seen.count(next)) continue;
      seen.insert(next);
      queue.emplace(-turns, (next[2] + next[1] - 1) / next[1], next);
    }
  }
  return kImpossible;
}

}  // namespace


int main(void) {
  int T;
  std::cin >> T;
  for (int i = 1; i <= T; ++i) {
    int Hd, Ad, Hk, Ak, B, D;
    std::cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
    std::cout << "Case #" << i << ": " << Solve(Hd, Ad, Hk, Ak, B, D)
              << std::endl;
  }

  return 0;
}

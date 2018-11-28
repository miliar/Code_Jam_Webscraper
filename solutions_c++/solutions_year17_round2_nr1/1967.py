#include <algorithm>
#include <cassert>
#include <cmath>
#include <deque>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <queue>
#include <vector>

ssize_t closestHorseAhead(size_t horseIdx, double curPosition,
                          const std::vector<double>& K) {
  double minDistance = 0;
  ssize_t closestHorseIdx = -1;
  for (size_t i = 0; i < K.size(); ++i) {
    if (i == horseIdx) continue;

    int distance = K[i] - curPosition;
    if (distance < 0) continue;
    if (distance < minDistance) {
      minDistance = distance;
      closestHorseIdx = i;
    }
  }
  return closestHorseIdx;
}

std::pair<double, ssize_t> nextInterestingTime(size_t horseIdx, size_t D,
                                               const std::vector<double>& K,
                                               const std::vector<size_t>& S) {
  if (K[horseIdx] >= D)  // past goal
    return {std::numeric_limits<double>::infinity(), -1};

  ssize_t closestIdx = closestHorseAhead(horseIdx, K[horseIdx], K);
  // std::cerr << "Closest for " << horseIdx << " is " << closestIdx << "\n";
  if (closestIdx == -1) {
    // std::cerr << "Next is goal in " << (D - K[horseIdx]) << ", going at "
    //          << S[horseIdx] << " km/h\n";
    // time when arriving at destination
    return {(D - K[horseIdx]) / S[horseIdx], -1};
  }

  // time when meeting next horse
  double thisHorseVel = S[horseIdx];
  double otherHorseVel = S[closestIdx];
  if (otherHorseVel >= thisHorseVel)
    return {std::numeric_limits<double>::infinity(), -1};

  return {(K[closestIdx] - K[horseIdx]) / (thisHorseVel - otherHorseVel),
          closestIdx};
}

bool allFinished(size_t D, std::vector<double>& K) {
  for (auto& k : K)
    if (k < D) return false;
  return true;
}

void simulate(std::vector<double>& K, std::vector<size_t>& S,
              double deltaTime) {
  for (size_t i = 0; i < K.size(); ++i) {
    K[i] += S[i] * deltaTime;
  }
}

void solve(int testcase, size_t D, size_t N, std::vector<double>& K,
           std::vector<size_t>& S) {
  double currentTime = 0.0;
  while (true) {
    if (allFinished(D, K)) {
      // std::cerr << "K: ";
      // for (auto k : K) std::cerr << k << ' ';
      // std::cerr << "\n";
      std::cout << "Case #" << testcase << ": " << std::fixed
                << ((double)D / currentTime) << "\n";
      return;
    }

    double smallestInterestingTime = std::numeric_limits<double>::infinity();
    size_t niH = 0;
    ssize_t niotherHorse = -1;
    for (size_t i = 0; i < N; ++i) {
      auto nitpair = nextInterestingTime(i, D, K, S);
      auto nit = nitpair.first;

      // std::cerr << "nit for " << i << " at " << nit << "\n";
      if (nit < smallestInterestingTime) {
        smallestInterestingTime = nit;
        niH = i;
        niotherHorse = nitpair.second;
      }
    }

    assert(smallestInterestingTime < std::numeric_limits<double>::infinity());
    currentTime += smallestInterestingTime;
    // std::cerr << "simulate to " << currentTime << "\n";
    simulate(K, S, smallestInterestingTime);

#if 1
    for (size_t i = 0; i < N; ++i) {
      auto cha = closestHorseAhead(i, K[i], K);
      if (cha == -1) continue;
      if (fabs(K[cha] - K[i]) < 1e-8) {
        // std::cerr << "Slow down of " << i << " " << cha << " to "
        //          << std::min(S[i], S[cha]) << "\n";
        S[cha] = S[i] = std::min(S[i], S[cha]);
      }
    }
#endif
    /*if (niotherHorse != -1) {
      S[niotherHorse] = S[niH] = std::min(S[niotherHorse], S[niH]);
    }*/
  }
}

int main() {
  std::cout.setf(std::ios::unitbuf);  // unbuffered output

  uint64_t numberOfTestcases;
  std::cin >> numberOfTestcases;
  for (size_t i = 1; i <= numberOfTestcases; ++i) {
    size_t D, N;
    std::cin >> D >> N;
    std::cerr << "D: " << D << " N: " << N << "\n";
    std::vector<double> K(N);
    std::vector<size_t> S(N);
    for (size_t j = 0; j < N; ++j) {
      std::cin >> K[j] >> S[j];
      std::cerr << "Input: " << j << " " << K[j] << " " << S[j] << "\n";
    }
    solve(i, D, N, K, S);
  }
  return 0;
}

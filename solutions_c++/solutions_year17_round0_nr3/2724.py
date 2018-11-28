#include <algorithm>
#include <iostream>
#include <tuple>
#include <utility>
#include <vector>

using ll = long long int;

void updateVec(std::vector<std::tuple<ll, ll>> &vec, ll firstHalf,
               ll firstHalfTimes, ll secondHalf, ll secondHalfTimes) {

  vec.erase(vec.begin());

  if (secondHalf > firstHalf) { // firstHalf should be greater than secondHalf
    std::swap(firstHalf, secondHalf);
  }

  auto found = std::find_if(vec.begin(), vec.end(),
                            [&](std::tuple<ll, ll> currentTuple) {
                              return std::get<0>(currentTuple) == firstHalf;
                            });

  if (found != vec.end()) {
    std::get<1>(*found) += firstHalfTimes;
  } else {
    vec.emplace_back(std::tuple<ll, ll>(firstHalf, firstHalfTimes));
  }

  found = std::find_if(vec.begin(), vec.end(),
                       [&](std::tuple<ll, ll> currentTuple) {
                         return std::get<0>(currentTuple) == secondHalf;
                       });

  if (found != vec.end()) {
    std::get<1>(*found) += secondHalfTimes;
  } else {
    vec.emplace_back(std::tuple<ll, ll>(secondHalf, secondHalfTimes));
  }

  //   for (auto &eachTuple : vec) {
  //     if (std::get<0>(eachTuple) == firstHalf) {
  //       std::get<1>(eachTuple)++;
  //     }
  //     if (std::get<0>(eachTuple) == secondHalf) {
  //       std::get<1>(eachTuple)++;
  //     }
  //   }
}

int main() {
  std::ios_base::sync_with_stdio(false);

  int t, totalCases;
  std::cin >> t;
  totalCases = t;

  while (t--) {
    ll n, k, tempk;
    std::cin >> n >> k;

    tempk = k;

    std::vector<std::tuple<ll, ll>> lenAndFreq;
    lenAndFreq.emplace_back(std::tuple<ll, ll>(n, 1));

    ll currentN, currentFreq, newN1, newN2;
    while (tempk > 0) {
      currentN = std::get<0>(*lenAndFreq.begin());
      currentFreq = std::get<1>(*lenAndFreq.begin());

      if (currentN & 1) {
        newN1 = newN2 = currentN / 2;
      } else {
        newN1 = currentN / 2;
        newN2 = (currentN / 2) - 1;
      }

      if (currentFreq <= tempk) {

        ll firstHalfTimes = currentFreq, secondHalfTimes = currentFreq;
        updateVec(lenAndFreq, newN1, firstHalfTimes, newN2, secondHalfTimes);
        tempk -= currentFreq;

      } else {
        break;
      }
    }

    std::cout << "Case #" << totalCases - t << ": " << std::max(newN1, newN2)
              << ' ' << std::min(newN1, newN2) << '\n';

    // long long int mini, maxi; // try to move this code in the above while
    // loop
    // if (currentN & 1) {
    //   maxi = mini = currentN / 2;
    // } else {
    //   maxi = currentN / 2;
    //   mini = (currentN / 2) - 1;
    // }
  }

  return 0;
}
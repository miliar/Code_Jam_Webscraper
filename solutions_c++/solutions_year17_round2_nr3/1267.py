#include <iostream>
#include <iomanip>
#include <cassert>
#include <vector>

struct Pony {
    double distance;
    double speed;
};

struct Problem {
    std::vector<double> distances;
    std::vector<Pony> ponies;
};


Problem ReadProblem(std::istream* istream) {
    Problem result;
    size_t n;
    double tmp;
    *istream >> n >> tmp;
    assert(tmp == 1);
    result.ponies.resize(n - 1);
    for (auto& pony : result.ponies) {
        *istream >> pony.distance >> pony.speed;
    }
    *istream >> tmp >> tmp;
    result.distances.resize(n - 1);
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) {
            *istream >> tmp;
            if (i + 1 == j) {
                assert (tmp >= 0.0);
                result.distances[i] = tmp;
            } else {
                assert (tmp < 0.0);
            }
        }
    }
    size_t a, b;
    *istream >> a >> b;
    assert (a == 1 && b == n);
    return result;
}

double Solve(const Problem& problem) {
    const auto distances = problem.distances;
    std::vector<Pony> ponies = problem.ponies;
    std::vector<double> times(ponies.size(), 1e100);
    times[0] = 0.0;
    for (size_t i = 0; i < distances.size(); ++i) {
        for (size_t j = 0; j < i; ++j) {
            if (times[i] > times[j]) {
                times[i] = times[j];
            }
        }
        const double distance = distances[i];
        for (size_t j = 0; j <= i; ++j) {
            if (ponies[j].distance < distance) {
                times[j] = 1e100;
            } else {
                ponies[j].distance -= distance;
                times[j] += distance / ponies[j].speed;
            }
        }
    }
    double result = 1e100;
    for (double time : times) {
        if (result > time) {
            result = time;
        }
    }
    return result;
}

int main() {
  int numberOfCases;
  std::cin >> numberOfCases;
  for (int caseNo = 0; caseNo < numberOfCases; ++caseNo) {
    const auto problem = ReadProblem(&std::cin);
    const auto result = Solve(problem);
    std::cout << "Case #" << caseNo + 1 << ": " << std::fixed
              << std::setprecision(10) << result << '\n';
  }
  return 0;
}

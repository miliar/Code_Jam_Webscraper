#include <iostream>
#include <vector>

struct Horse {
  int speed;
  int initialPos;
};

void doCase(int caseNum) {
  int dist, numHorses;
  std::vector<Horse> otherHorses;

  std::cin >> dist;
  std::cin >> numHorses;

  std::cerr << "dist " << dist << std::endl;

  for (int i = 0; i < numHorses; ++i) {
    int speed, pos;
    std::cin >> pos;
    std::cin >> speed;

    std::cerr << "speed " << speed << " pos " << pos << std::endl;
    otherHorses.push_back(Horse { speed, pos });
  }
  double minTime = 0;
  for (int i = 0; i < numHorses; ++i) {
    std::cerr << "speed2 " << otherHorses[i].speed << " pos2 " << otherHorses[i].initialPos << std::endl;
    const double time = ((double)(dist - otherHorses[i].initialPos))/otherHorses[i].speed;
    if (time > minTime) {
      minTime = time;
    }
  }
  std::cerr << "mintime " << minTime << std::endl;
  std::cout << "Case #" << caseNum + 1 << ": " << std::fixed << dist/minTime << std::endl;
}

int main() {
  int numCases = 0;
  std::cin >> numCases;
  for (int i = 0; i < numCases; ++i) {
    doCase(i);
  }
  return 0;
}

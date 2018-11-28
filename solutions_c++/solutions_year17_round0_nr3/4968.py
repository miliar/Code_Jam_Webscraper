#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <assert.h>

using namespace std;

using bigint = unsigned long long;

class Compare
{
public:
  bool operator() (bigint a, bigint b)
  {
    return a > b;  // smallest index at the top
  }
};

using Indices = std::priority_queue<bigint, std::vector<bigint>, Compare>;
using EmptyStallRuns = std::map<bigint, Indices*>;

std::vector<bool> initStallOccupancy(bigint numStalls) {
  auto occupancy = std::vector<bool>(numStalls + 2, false);
  occupancy[0] = true;
  occupancy[occupancy.size() - 1] = true;
  return occupancy;
}

void addStallRun(EmptyStallRuns& emptyStallRuns, bigint index, bigint length) {
  // cout << "adding run: " << index << ": " << length << endl;
  auto it = emptyStallRuns.find(length);
  if (it != emptyStallRuns.end()) {
    it->second->push(index);
  } else {
    emptyStallRuns[length] = new Indices();
    emptyStallRuns[length]->push(index);
  }
}

void chooseStall(std::vector<bool>& occupancy, EmptyStallRuns& emptyStallRuns) {
  // cout << "choose stall" << endl;

  assert(!emptyStallRuns.empty());

  auto bestRun = emptyStallRuns.rbegin(); // end of the map has the longest stall runs
  bigint bestRunLength = bestRun->first;
  // cout << "best run length: " << bestRunLength << endl;
  // cout << "num runs with best length: " << bestRun->second->size() << endl;
  Indices* bestRunIndices = bestRun->second;

  assert(!bestRunIndices->empty());

  bigint runIndex = bestRunIndices->top();
  bestRunIndices->pop();
  if (bestRunIndices->empty()) {  // remove from best run indices if empty
    // cout << "erasing run with length: " << bestRunLength << endl;
    // TODO actually delete the empty stall run list!
    assert(emptyStallRuns.erase(bestRunLength) == 1);
  }
  // cout << "best run index: " << runIndex << endl;

  // update occupancy
  bigint offsetIndex = (bestRunLength + 1) / 2;  // integer division gives floor
  occupancy[runIndex + offsetIndex] = true;

  // cout << "offset index: " << offsetIndex << endl;

  // add the two new runs
  addStallRun(emptyStallRuns, runIndex, offsetIndex - 1);
  addStallRun(emptyStallRuns, runIndex + offsetIndex, bestRunLength - offsetIndex);
}

void printOccupancy(const std::vector<bool>& occupancy) {
  cout << "Occupancy: ";
  for (auto occupied: occupancy) {
    cout << (occupied ? "0" : ".");
  }
  cout << endl;
}

std::vector<bool> calcStallOccupancy(EmptyStallRuns& emptyStallRuns, bigint numStalls, bigint numPooers) {
  std::vector<bool> occupancy = initStallOccupancy(numStalls);
  addStallRun(emptyStallRuns, 0, numStalls);
  while (numPooers > 1) {
    // cout << "num pooers left: " << numPooers << endl;
    // printOccupancy(occupancy);
    chooseStall(occupancy, emptyStallRuns);
    numPooers--;
  }
  return occupancy;
}

bigint getClosestPooerDistance(const EmptyStallRuns& emptyStallRuns) {
  auto bestRun = emptyStallRuns.rbegin(); // end of the map has the longest stall runs
  bigint bestRunLength = bestRun->first;
  bigint offsetIndex = (bestRunLength + 1) / 2;
  return offsetIndex - 1;
}

bigint getFurthestPooerDistance(const EmptyStallRuns& emptyStallRuns) {
  auto bestRun = emptyStallRuns.rbegin(); // end of the map has the longest stall runs
  bigint bestRunLength = bestRun->first;
  bigint offsetIndex = (bestRunLength + 1) / 2;
  return bestRunLength - offsetIndex;
}

int main() {
  unsigned int numCases;
  std::cin >> numCases;
  for (unsigned int i = 0; i < numCases; ++i) {
    bigint numStalls;
    std::cin >> numStalls;
    bigint numPooers;
    std::cin >> numPooers;

    EmptyStallRuns emptyStallRuns;
    auto occupancy = calcStallOccupancy(emptyStallRuns, numStalls, numPooers);
    // printOccupancy(occupancy);
    bigint closestPooerDistance = getClosestPooerDistance(emptyStallRuns);
    bigint furthestPooerDistance = getFurthestPooerDistance(emptyStallRuns);

    cout << "Case #" << i + 1 << ": " << furthestPooerDistance << " " << closestPooerDistance;
    cout << endl;
  }
  return 0;
}

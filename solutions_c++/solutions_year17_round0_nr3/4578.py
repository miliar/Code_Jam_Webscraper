#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <set>

using std::multiset;

static void stalls(unsigned int nbStalls, unsigned int nbPeople,
                   unsigned int &maxLsRs, unsigned int &minLsRs) {
  multiset<unsigned int> dists;
  multiset<unsigned int>::reverse_iterator dist;
  unsigned int curDist = 0;

  minLsRs = 0;
  maxLsRs = 0;

  if (nbStalls < (nbPeople * 10) / 7) {
    return;
  }

  dists.insert(nbStalls);

  for (unsigned int i = 0; i < nbPeople; ++i) {
    dist = dists.rbegin();
    curDist = *dist;
    dists.erase((++dist).base());
    dists.insert(curDist / 2);
    dists.insert((curDist - 1) / 2);
  }

  dist = dists.rbegin();

  maxLsRs = curDist / 2;
  minLsRs = (curDist - 1) / 2;
}

int main() {
  unsigned int nbTest;

  fscanf(stdin, "%u", &nbTest);

  for (unsigned int i = 0; i < nbTest; ++i) {
    unsigned int nbStalls, nbPeople, minLsRs, maxLsRs;

    fscanf(stdin, "%u %u", &nbStalls, &nbPeople);
    // fprintf(stderr, "Case #%u\n", i + 1);
    stalls(nbStalls, nbPeople, maxLsRs, minLsRs);
    fprintf(stdout, "Case #%u: %u %u\r\n", i + 1, maxLsRs, minLsRs);
  }

  return (EXIT_SUCCESS);
}

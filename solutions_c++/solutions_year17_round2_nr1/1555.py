#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cmath>
#include <climits>

using namespace std;

struct Horse {
  long double pos;
  long double speed;
};

const int MAX_HORSES = 1000;
Horse horse[MAX_HORSES];
int destination, horses;

struct SortHorsesByPosition {
  inline bool operator() (const Horse& h1, const Horse& h2) {
      return (h1.pos < h2.pos);
    }
};

long double solve() {
  sort(horse, horse + horses, SortHorsesByPosition());
  
  long double slowestTime = -1;
  for (int h = horses-1; h >= 0; h--) {
    if (horse[h].pos >= destination) continue;
    
    long double timeToDestination = (destination-horse[h].pos)/horse[h].speed;
    slowestTime = max(slowestTime, timeToDestination);
  }
  return destination/slowestTime;
}

int main() {
  int tcases;
  cin >> tcases;
  
  for (int c = 1; c <= tcases; c++) {
    cin >> destination >> horses;
    for (int h = 0; h < horses; h++) {
      cin >> horse[h].pos >> horse[h].speed;
    }
    cout << "Case #" << c << ": " << fixed << setprecision(6) << solve() << endl;
  }
  return 0;
}

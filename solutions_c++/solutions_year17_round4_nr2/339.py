#include <iostream>
#include <cassert>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define FORE(i,a,b) for(int i=(a);i<=(b);i++)
#define SET(A,p) memset(A,p,sizeof(A))

int N, C, M;
int P[1024], B[1024];

int cc[1024], pp[1024];

int can_manage(int min_rides) {
  int promotions = 0;
  int gap = 0;
  FORE(i,1,N) {
    if (pp[i] > min_rides) {
      int need = pp[i] - min_rides;
      if (gap < need) return -1;
      promotions += need;
      gap -= need;
    } else {
      gap += min_rides - pp[i];
    }
  }
  return promotions;
}

void do_case(int cn) {
  cin >> N >> C >> M;
  FOR(i,0,M) cin >> P[i] >> B[i];
  SET(cc,0);
  SET(pp,0);
  FOR(i,0,M) {
    cc[B[i]]++;
    pp[P[i]]++;
  }
  int min_rides = 0;
  FORE(i,1,C) min_rides = max(min_rides,cc[i]);
  int promotions = -1;
  while((promotions = can_manage(min_rides)) == -1) {
    ++min_rides;
  }
  cout << "Case #" << cn << ": " << min_rides << " " << promotions << endl;
}

int main() {
  int T;
  cin >> T;
  FORE(te,1,T) do_case(te);
  return 0;
}
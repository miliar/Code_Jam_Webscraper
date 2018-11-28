#include <iostream>
#include <string>
#include <vector>
using namespace std;

#define INF (1<<30)

int solve(int p, string plate, int S) {

  // printf("solve: %d %s %d\n", p, plate.c_str(), S);

  if(p == plate.length() - S + 1) {
    for(int i = 0; i < plate.length(); i++) {
      if(plate[i] == '-') return INF;
    }
    return 0;
  }

  int res = INF;
  if(plate[p] == '-') {
    string next(plate);
    for(int i = p; i < p + S; i++) next[i] = plate[i] == '-' ? '+' : '-';
    return min(res, solve(p + 1, next, S) + 1);
  }
  return min(res, solve(p + 1, plate, S));
}

int main() {

  int T;
  cin >> T;

  for(int t = 1; t <= T; t++) {
    
    string plate;
    cin >> plate;
    int S;
    cin >> S;

    int res = solve(0, plate, S);

    printf("Case #%d: ", t);
    if(res >= INF) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", res);
    }
  }

  return 0;
}

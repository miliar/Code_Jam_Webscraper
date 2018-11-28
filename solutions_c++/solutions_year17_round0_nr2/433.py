#include <bits/stdc++.h>

using namespace std;
typedef long long unsigned llu;

bool tidy(llu N) {
  if(N < 10)
    return true;

  return N%10 >= (N/10)%10 && tidy(N/10);
}

int main() {
  int T;
  llu N;

  cin >> T;
  for(int caso = 1; caso <= T; caso++) {
    cin >> N;

    llu pot = 1;
    while(!tidy(N)) {
      pot*=10;
      N -= N%pot + 1;
    }

    cout << "Case #" << caso << ": " << N << endl;
  }

  return 0;
}

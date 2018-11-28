#include <bits/stdc++.h>

using namespace std;

int main() {
  string s;
  int T, K;

  cin >> T;
  for(int caso = 1; caso <= T; caso++) {
    cin >> s >> K;
    int counter = 0;
    for(int i = 0; i <= (int) s.size()-K; i++) {
      if(s[i] == '-') {
        counter++;
        for(int j = i; j < i+K; j++)
          if(s[j] == '-')
            s[j] = '+';
          else
            s[j] = '-';
      }
    }

    bool possible = true;
    for(int i = s.size()-K+1; i < (int) s.size(); i++) {
      if(s[i] == '-')
        possible = false;
    }

    if(possible)
      cout << "Case #" << caso << ": " << counter << endl;
    else
      cout << "Case #" << caso << ": IMPOSSIBLE" << endl;
  }

  return 0;
}
